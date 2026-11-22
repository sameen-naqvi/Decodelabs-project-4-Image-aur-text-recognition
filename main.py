
import streamlit as st
from PIL import Image
import pytesseract

# Windows Tesseract path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

st.title("Text Recognition System")
st.write("Upload an image to recognize text")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image")

    if st.button("Recognize Text"):

        text = pytesseract.image_to_string(
            image,
            lang="eng"
        )

        st.subheader("Recognized Text")

        if text.strip():
            st.text_area("Extracted Text", text)
        else:
            st.warning("No text found in image.")
