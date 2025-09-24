import streamlit as st
import os

# Title
st.title("👗 Fashion Recommender App")
st.write("Based on the weather, place, and your company, we'll suggest what to wear and show you an example outfit!")

# User inputs
category = st.selectbox("Select Category", ["Women", "Men", "Children"], key="category")
child_gender = None
if category == "Children":
    child_gender = st.selectbox("Select Child Gender", ["Boy", "Girl"], key="child_gender")

weather = st.selectbox("Select Weather", ["Sunny", "Rainy", "Cold", "Hot"], key="weather")
place = st.selectbox("Select Place", ["Beach", "Park", "Restaurant", "City", "Mountains"], key="place")
companion = st.selectbox("Going With", ["Friends", "Family", "Couple"], key="companion")

# Default fashion tips
default_rules = {
    "Women": {"Hot": "Light dress, top with skirt or shorts, and sandals.",
              "Cold": "Coat, sweater, trousers, and boots.",
              "Rainy": "Waterproof jacket, trousers, and boots.",
              "Sunny": "Comfortable top, trousers or skirt, and sandals."},
    "Men": {"Hot": "T-shirt, shorts, and sandals or sneakers.",
            "Cold": "Jacket, sweater, trousers, and boots.",
            "Rainy": "Waterproof jacket, pants, and boots.",
            "Sunny": "Comfortable T-shirt, trousers or shorts, and sneakers."},
    "Children": {
        "Boy": {"Hot": "T-shirt, shorts, and sandals.",
                "Cold": "Jacket, sweater, pants, and boots.",
                "Rainy": "Raincoat, pants, and boots.",
                "Sunny": "T-shirt, shorts, and sneakers."},
        "Girl": {"Hot": "Dress or T-shirt with shorts, sandals.",
                 "Cold": "Jacket, sweater, pants, and boots.",
                 "Rainy": "Raincoat, leggings, and boots.",
                 "Sunny": "Top with skirt/shorts, and sneakers."}
    }
}

def find_image(filename_without_ext):
    """
    Search the images folder for a file matching the given name,
    allowing .jpg or .jpeg extension.
    """
    for ext in [".jpeg", ".jpg"]:
        path = os.path.join("images", filename_without_ext + ext)
        if os.path.exists(path):
            return path
    return None

# Button to get recommendation
if st.button("Get Recommendation"):
    # Fashion tip
    if category == "Children":
        recommendation = default_rules["Children"][child_gender][weather]
        filename_base = f"children_{child_gender.lower()}_{weather.lower()}_{place.lower()}"
    else:
        recommendation = default_rules[category][weather]
        filename_base = f"{category.lower()}_{weather.lower()}_{place.lower()}"

    st.success(f"👚 Fashion Tip: {recommendation}")

    # Display image
    image_path = find_image(filename_base)
    if image_path:
       st.image(image_path, caption="Example Outfit", use_container_width=True)
    else:
        st.warning("⚠️ No image available for this combination.")

