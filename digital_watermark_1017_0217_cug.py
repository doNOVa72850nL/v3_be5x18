# 代码生成时间: 2025-10-17 02:17:38
import numpy as np
import cv2
from PIL import Image
import gr
import io
from gr import Interface

def embed_watermark(image_path, watermark_text, output_path):
    """
    Embeds a watermark into an image.

    Args:
    - image_path (str): Path to the input image.
    - watermark_text (str): Text to be embedded as a watermark.
    - output_path (str): Path to save the watermarked image.
    """
    try:
        # Load the original image
        image = np.array(Image.open(image_path))
        
        # Convert the watermark text to binary
        watermark_binary = ''.join(format(ord(c), '08b') for c in watermark_text)
        
        # Create a watermark image (height 1 pixel, width equal to the binary string length)
        watermark = Image.new('RGB', (len(watermark_binary), 1))
        pixels = watermark.load()
        for i in range(len(watermark_binary)):
            pixels[i, 0] = (255 if watermark_binary[i] == '1' else 0,) * 3
        watermark_array = np.array(watermark)
        
        # Insert the watermark into the least significant bit of the image
        watermarked_image = np.bitwise_or(image, watermark_array)
        
        # Save the watermarked image
        Image.fromarray(watermarked_image).save(output_path)
        
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def extract_watermark(watermarked_image_path):
    """
    Extracts the watermark from a watermarked image.

    Args:
    - watermarked_image_path (str): Path to the watermarked image.

    Returns:
    - watermark_text (str): The extracted watermark text.
    """
    try:
        # Load the watermarked image
        watermarked_image = np.array(Image.open(watermarked_image_path))
        
        # Extract the watermark from the least significant bit of the image
        watermark_binary = ''.join('1' if watermarked_image[:, -1, 0] == 255 else '0' for _ in range(watermarked_image.shape[0]))
        
        # Convert the binary watermark back to text
        watermark_bytes = bytes(int(watermark_binary[i:i+8], 2) for i in range(0, len(watermark_binary), 8))
        watermark_text = watermark_bytes.decode('utf-8')
        
        return watermark_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Create a Gradio interface
    with Interface("Digital Watermark", "Embed and extract watermarks in images") as demo:
        with demo:
            # Input image file and watermark text
            input_image = gr.inputs.Image(type="file")
            watermark_text = gr.inputs.Textbox(label="Watermark Text")
            output_image = gr.outputs.Image(type="file")
            
            # Embed watermark button
            def embed_watermark_func(input_img, watermark_text):
                # Convert input image to a path-like object
                image_io = io.BytesIO()
                input_img.save(image_io, format='PNG')
                image_io.seek(0)
                
                # Embed the watermark and return the output image
                if embed_watermark(image_io, watermark_text, 'watermarked_image.png'):
                    image = Image.open('watermarked_image.png')
                    output_image.set_image(image)
                else:
                    output_image.set_image(None)
                    
            # Extract watermark button
            def extract_watermark_func(watermarked_img):
                # Convert input image to a path-like object
                image_io = io.BytesIO()
                watermarked_img.save(image_io, format='PNG')
                image_io.seek(0)
                
                # Extract the watermark and return the output text
                watermark_text = extract_watermark(image_io)
                if watermark_text:
                    return watermark_text
                else:
                    return "Failed to extract watermark"
            
            gr.Button("Embed Watermark").click(embed_watermark_func, inputs=[input_image, watermark_text], outputs=[output_image])
            gr.Button("Extract Watermark").click(extract_watermark_func, inputs=[output_image], outputs=[watermark_text])
            
if __name__ == "__main__":
    main()