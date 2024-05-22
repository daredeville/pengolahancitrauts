import streamlit as st
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt


# Fungsi untuk konversi gambar ke HSV
def rgb_to_hsv(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    return hsv_image

# Fungsi untuk menghitung histogram
def calculate_histogram(image):
    histogram = cv2.calcHist([image], [0], None, [256], [0,256])
    return histogram

# Fungsi untuk menyesuaikan brightness dan contrast
def adjust_brightness_contrast(image, brightness, contrast):
    adjusted = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
    return adjusted

# Fungsi untuk mendapatkan kontur gambar
def calculate_contours(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

# Fungsi untuk menggambar/mendapatkan kontur gambar
def draw_contours(image, contours):
    contoured_img = cv2.drawContours(np.copy(image), contours, -1, (0, 255, 0), 2)
    return contoured_img

# Streamlit App
def main():
    st.title("Tugas UTS Pengolahan Citra Memanipulasi Gambar")
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Konversi ke array numpy
        img_array = np.array(image)

        # Konversi RGB ke HSV
        hsv = rgb_to_hsv(img_array)
        st.image(hsv, caption="HSV Image", use_column_width=True)

        # Hitung histogram
        st.write("Histogram")
        histogram = calculate_histogram(img_array)
        st.bar_chart(histogram)
       
        # Menyesuaikan brightness dan contrast
        brightness = st.slider("Brightness", -100, 100, 0)
        contrast = st.slider("Contrast", 0.0, 3.0, 1.0)
        adjusted = adjust_brightness_contrast(img_array, brightness, contrast)
        st.image(adjusted, caption="Adjusted Image for Brightnes and Contrast", use_column_width=True)

        # Menghitung kontur
        contours = calculate_contours(img_array)
        
       
       #Menampilkan kontur gambar
        contoured_img = draw_contours(img_array, contours)
        st.image(contoured_img, caption="Image with Contours", use_column_width=True)

        st.write(f"Total Contours: {len(contours)}")
if __name__ == "__main__":
    main()
