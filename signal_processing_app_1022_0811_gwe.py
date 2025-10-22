# 代码生成时间: 2025-10-22 08:11:25
import numpy as np
import gradio as gr
from scipy.signal import butter, lfilter, freqz
# 改进用户体验

# Define a function to create a Butterworth filter
def butterworth_filter(lowcut, highcut, fs, order):
    nyq = 0.5 * fs  # Nyquist Frequency
# TODO: 优化性能
    low = lowcut / nyq  # Low cut-off normalized
# 添加错误处理
    high = highcut / nyq  # High cut-off normalized
# 添加错误处理

    # Design filter
    b, a = butter(order, [low, high], btype='band')
    return b, a

# Function to apply the Butterworth filter to a signal
def apply_filter(signal, fs, order=5, lowcut=0.1, highcut=0.6):
    try:
        b, a = butterworth_filter(lowcut, highcut, fs, order)
        y = lfilter(b, a, signal)
        return y
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to generate a sample signal
def generate_sample_signal():
    duration = 2  # seconds
    fs = 1000  # sample rate, Hz
    t = np.linspace(0, duration, int(duration * fs), endpoint=False)
    freq = 5  # Hz
    return np.sin(2 * np.pi * freq * t)

# Define the interface for the signal processing app
def signal_processing_interface():
    # Sample signal
    sample_signal = generate_sample_signal()
# NOTE: 重要实现细节

    # Create a Gradio interface
    demo = gr.Interface(
        fn=apply_filter,
        inputs=["array",
                 gr.CheckboxGroup(choices=["Low-pass", "High-pass", "Band-pass"], label="Filter Type"),
                 gr.Slider(minimum=1, maximum=10, default=5, label="Order"),
                 gr.Slider(minimum=0.1, maximum=0.9, step=0.1, default=0.1, label="Low Cut-off"),
                 gr.Slider(minimum=0.1, maximum=0.9, step=0.1, default=0.6, label="High Cut-off")],
        outputs="array",
        examples=[[sample_signal, ["Low-pass"], 5, 0.1, 0.6]],
        live=True
    )
    return demo.launch()

# Uncomment the line below to launch the interface
# signal_processing_interface()