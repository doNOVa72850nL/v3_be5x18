# 代码生成时间: 2025-10-02 02:51:22
import cv2
import numpy as np
from PIL import Image
import gr
from gr import *

# Digital Watermarking using Python and Gradio
# This script demonstrates how to embed and extract a watermark from an image.

# Function to embed a watermark into an image
def embed_watermark(image_path, watermark_text, output_path):
    try:
        # Load the original image
        image = cv2.imread(image_path)
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Create a binary representation of the watermark text
        watermark = np.array([[0, 255] for _ in range(len(watermark_text))])
        # Embed the watermark into the image
        watermarked_image = np.copy(gray_image)
        for i in range(len(watermark_text)):
            watermarked_image[i:i+2, i:i+2] = watermark[0, :]
        # Save the watermarked image
        cv2.imwrite(output_path, watermarked_image)
        return True
    except Exception as e:
        print(f"Error embedding watermark: {e}")
        return False

# Function to extract a watermark from an image
def extract_watermark(image_path):
    try:
        # Load the watermarked image
        image = cv2.imread(image_path)
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Extract the watermark from the image
        watermark = ''
        for i in range(len(gray_image[0, :2])):
            if gray_image[i:i+2, i:i+2] == np.array([[0, 255]]):
                watermark += '1'
            else:
                watermark += '0'
        # Convert the binary watermark to text
        watermark_text = ''.join([chr(int(watermark[i:i+8], 2)) for i in range(0, len(watermark), 8)])
        return watermark_text
    except Exception as e:
        print(f"Error extracting watermark: {e}")
        return None

# Create a Gradio interface for the digital watermarking functions
iface = gr.Interface(
    fn=embed_watermark,
    inputs=[gr.Textbox(label="Image Path"), gr.Textbox(label="Watermark Text"), gr.Textbox(label="Output Path")],
    outputs="file",
    title="Digital Watermarking",\    description="Embed and extract watermarks from images using Python and Gradio.")

iface.launch()