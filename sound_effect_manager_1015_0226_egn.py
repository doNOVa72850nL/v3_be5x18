# 代码生成时间: 2025-10-15 02:26:25
{
    "# Sound Effect Manager using Python and Gradio
",
    "# This program allows users to manage sound effects using a simple GUI.
",
    "# Import necessary libraries
",
    "import gradio as gr
import os
import sys
from gtts import gTTS
from playsound import playsound
",
    "# Define the SoundEffectManager class
",
    "class SoundEffectManager:
",
    "    def __init__(self):
",
    "        # Initialize an empty list to store sound effect files
",
    "        self.sound_effects = []
",
    "        # Create a Gradio interface
",
    "        self.interface = gr.Interface(
",
    "            fn=self.load_sound_effect,
",
    "            inputs=[gr.Textbox(label="Sound Effect File Path")],
",
    "            outputs=[gr.Audio(label="Sound Effect")],
",
    "            examples=[("sound1.wav",)],
",
    "            description="Load and play sound effects.",
",
    "        )
",
",
    "    def load_sound_effect(self, file_path):
",
    "        # Check if the file exists
",
    "        if not os.path.exists(file_path):
",
    "            return gr.update(value="", visible=False), "File not found."
",
",
    "        # Check if the file is a valid audio file
",
    "        if not file_path.endswith((".mp3", ".wav")):
",
    "            return gr.update(value="", visible=False), "Invalid file format."
",
",
    "        # Add the sound effect to the list
",
    "        self.sound_effects.append(file_path)
",
",
    "        # Play the sound effect
",
    "        playsound(file_path)
",
",
    "        # Return the sound effect as an audio output
",
    "        return file_path
",
",
    "# Create an instance of the SoundEffectManager class
",
"if __name__ == "__main__":
",
"    manager = SoundEffectManager()
",
"    # Run the Gradio interface
",
"    manager.interface.launch()
"
}