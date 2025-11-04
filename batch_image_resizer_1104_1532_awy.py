# 代码生成时间: 2025-11-04 15:32:02
import os
from PIL import Image
import gr

"""
Batch Image Resizer
This script resizes multiple images to a specified size using the GRADIO framework.
"""

# Function to resize an image
def resize_image(image_path, output_path, size):
    try:
        with Image.open(image_path) as img:
            # Resize the image
            img = img.resize(size)
            # Save the resized image
            img.save(output_path)
            return f"{os.path.basename(output_path)} resized successfully."
    except Exception as e:
        return f"Error resizing {os.path.basename(image_path)}: {str(e)}"

# Function to process a batch of images
def process_images(image_folder, output_folder, size):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the folder
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_path = os.path.join(image_folder, filename)
            output_path = os.path.join(output_folder, filename)
            result = resize_image(image_path, output_path, size)
            print(result)

# Define the GrADIO interface
def gr_interface():
    # Create a GrADIO component for selecting the image folder
    image_input = gr.Folder(label="Select images folder")

    # Create a GrADIO component for selecting the output folder
    output_input = gr.Folder(label="Select output folder")

    # Create a GrADIO component for specifying the output size
    size_input = gr.Slider(minimum=100, maximum=1000, step=10, label="Resize to")

    # Function to handle GrADIO inputs
    def update_outputs(image_folder, output_folder, size):
        process_images(image_folder, output_folder, (size, size))
        return f"Resized images saved to {output_folder}"

    # Create a GrADIO output component
    output = gr.Textbox(label="Output")

    # Create the GrADIO interface
    demo = gr.Interface(
        fn=update_outputs,
        inputs=[image_input, output_input, size_input],
        outputs=output,
        live=True
    )

    # Run the GrADIO interface
    demo.launch()

# Run the GrADIO interface
if __name__ == '__main__':
    gr_interface()