import streamlit as st
from PIL import Image
import torch
from torch import jit
from constant import transform, food_list

def load_model():
    model = jit.load('model.pt')
    return model

# Main function for Streamlit app
def main():
    model = load_model()
    st.title("Calorify")
    uploaded_image = st.file_uploader("Upload an image of food...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)
        image = Image.open(uploaded_image).convert('RGB')
        image_tensor = transform(image).unsqueeze(0)
        with torch.no_grad():
            logits = model(image_tensor)
        pred = torch.argmax(logits, dim=1).item()
        
        st.header(f"{food_list[pred][1]}")
        st.subheader(f"Prediction: {food_list[pred][0]}")


if __name__ == "__main__":
    main()
