# 代码生成时间: 2025-10-14 17:17:49
import gradio as gr
import numpy as np
from PIL import Image
from pythreejs import *

"""
A simple 3D rendering engine using Gradio and PyThreeJS.
This program creates a basic 3D scene with a cube and allows users to interact with it.
"""

def update_scene(rotation_speed, scale, color):
    """
    Update the 3D scene based on user input.
    
    Args:
        rotation_speed (float): The speed at which the cube rotates.
        scale (float): The size of the cube.
        color (str): The color of the cube.
    
    Returns:
        Scene: The updated 3D scene.
    """
    scene = Scene()
    camera = PerspectiveCamera(position=[1,1,2])
    scene.add(camera)
    
    cube = Mesh(geometry=BoxGeometry(width=1, height=1, depth=1),
                material=MeshBasicMaterial(color=color),
                position=[0, 0, 0],
                rotation=[0, 0, 0])
    scene.add(cube)
    
    # Create an animation loop to rotate the cube
    def animate():
        cube.rotation.x += rotation_speed
        cube.rotation.y += rotation_speed
        return cube
    
    # Scale the cube based on user input
    cube.scale = [scale, scale, scale]
    
    return scene

# Create a Gradio interface
iface = gr.Interface(
    update_scene,
    inputs=["slider:0.0:0.1:0.01", "slider:0.1:2.0:0.1", "color"], 
    outputs="image",
    examples=[[0.05, 1.0, "#ff0000"], [0.01, 1.5, "#00ff00"], [0.02, 1.0, "#0000ff"]],
    title="3D Rendering Engine",
    description="Render a 3D cube with customizable rotation speed, scale, and color."
)

# Run the Gradio interface
iface.launch()