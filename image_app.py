import streamlit as st
from PIL import Image
import cv2
import numpy as np
from streamlit_image_comparison import image_comparison
from skimage.util import random_noise
import io

st.set_page_config(page_title="🖼️ Image Processor", layout="wide")

# Custom Title Style
st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>🖼️ Image Processor App</h1>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img_np = np.array(image)

    # Sidebar
    st.sidebar.markdown("## 🎛️ Processing Options")
    option = st.sidebar.selectbox(
        "Choose Technique",
        [
            "Thresholding",
            "Brightness using Power Law Transformation",
            "Contrast Enhancement (Histogram Equalization)",
            "Gaussian Blur",
            "Edge Detection (Canny)",
            "Salt & Pepper Noise + Median Denoise",
            "Complement Image",
            "JPEG Compression"
        ]
    )

    params = {}

    if option == "Thresholding":
        params['th_low'], params['th_high'] = st.sidebar.slider("Threshold Range", 0, 255, (0, 255))
    elif option == "Brightness using Power Law Transformation":
        params['gamma'] = st.sidebar.slider("Gamma", 0.1, 5.0, 1.0)
    elif option == "Gaussian Blur":
        params['k'] = st.sidebar.slider("Kernel Size (odd)", 1, 15, 3, step=2)
    elif option == "Salt & Pepper Noise + Median Denoise":
        params['amount'] = st.sidebar.slider("Noise Amount", 0.0, 0.1, 0.02)
        params['apply_median'] = st.sidebar.checkbox("Apply Median Filter")
    elif option == "JPEG Compression":
        params['quality'] = st.sidebar.slider("JPEG Quality", 0, 100, 10)

    # Processing logic
    if option == "Thresholding":
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
        mask = cv2.inRange(gray, params['th_low'], params['th_high'])
        processed_np = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)

    elif option == "Brightness using Power Law Transformation":
        norm = img_np / 255.0
        transformed = np.power(norm, params['gamma'])
        processed_np = np.uint8(transformed * 255)

    elif option == "Contrast Enhancement (Histogram Equalization)":
        yuv = cv2.cvtColor(img_np, cv2.COLOR_RGB2YUV)
        yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
        processed_np = cv2.cvtColor(yuv, cv2.COLOR_YUV2RGB)

    elif option == "Gaussian Blur":
        processed_np = cv2.GaussianBlur(img_np, (params['k'], params['k']), 0)

    elif option == "Edge Detection (Canny)":
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        processed_np = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

    elif option == "Salt & Pepper Noise + Median Denoise":
        noisy = random_noise(img_np, mode='s&p', amount=params['amount'])
        noisy = np.array(255 * noisy, dtype='uint8')
        if params['apply_median']:
            processed_np = cv2.medianBlur(noisy, 3)
        else:
            processed_np = noisy

    elif option == "Complement Image":
        processed_np = cv2.bitwise_not(img_np)

    elif option == "JPEG Compression":
        def compress_jpeg(image, quality=10):
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
            _, encoded_img = cv2.imencode('.jpg', image, encode_param)
            decoded_img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
            return decoded_img, encoded_img, len(encoded_img)

        jpeg_np, jpeg_bytes, size = compress_jpeg(img_np, params['quality'])
        processed_np = jpeg_np

    processed_pil = Image.fromarray(processed_np)

    st.markdown("---")
    st.markdown("## 🔍 Image Comparison")
    image_comparison(
        img1=image,
        img2=processed_pil,
        label1="Original",
        label2="Processed",
        width=700
    )

    if option == "JPEG Compression":
        st.markdown(f"**📦 Compressed Size:** {size} bytes")
        st.download_button(
            label="📥 Download JPEG",
            data=jpeg_bytes.tobytes(),
            file_name="compressed.jpg",
            mime="image/jpeg"
        )

else:
    st.warning("Upload an image to get started.")