"""Real-time inference script. Run with: python realtime.py --model model.h5"""
import cv2
import argparse
import tensorflow as tf
import numpy as np
import pyttsx3
from utils import preprocess_frame, crop_hand_region

def load_labels_from_model(model):
    # Full set of labels (29 total)
    return [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'del', 'nothing', 'space'
    ]

def main(args):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print('Cannot open webcam')
        return
    
    if args.model:
        model = tf.keras.models.load_model(args.model)
        labels = load_labels_from_model(model)
    else:
        print('No model provided. Exiting.')
        return

    engine = pyttsx3.init()
    print('Starting real-time translation. Press q to quit.')

    while True:
        ret, frame = cap.read()
        if not ret:
            break   # ✅ this break is INSIDE the loop

        frame = cv2.flip(frame, 1)
        hand = crop_hand_region(frame)
        inp = preprocess_frame(hand, target_size=(64,64))
        preds = model.predict(inp)
        idx = int(np.argmax(preds[0]))
        label = labels[idx]
        conf = float(np.max(preds[0]))

        # Display prediction on screen
        cv2.putText(frame, f'{label} ({conf:.2f})', (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.imshow('Real-Time Sign Language Translator', frame)

        # Speak out loud
        engine.say(label)
        engine.runAndWait()

        # Exit if user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break   # ✅ also inside the loop

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, help='Path to trained model (.h5)')
    args = parser.parse_args()
    main(args)