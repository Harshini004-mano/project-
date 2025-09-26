def calculator():
    weight = float(input("enter your weight(kg): "))
    height = float(input("enter your height(m): "))

    # Convert cm to meters if user enters a large number
    if height > 3:  
        height = height / 100  

    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")
    return bmi

def category(bmi):
    if bmi < 18.5:
        print("UNDERWEIGHT")
    elif 18.5 <= bmi < 24.9:
        print("NORMAL")
    elif 25 <= bmi < 29.9:
        print("OVERWEIGHT")
    else:
        print("OBESITY")

if __name__ == "__main__":
    bmi_value = calculator()
    category(bmi_value)
