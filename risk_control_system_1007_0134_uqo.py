# 代码生成时间: 2025-10-07 01:34:19
import gradio as gr
def check_risk(data):
    """
    Function to check the risk level based on provided data.
    :param data: dict containing 'age' and 'income'
    :return: str with risk level
    """
    try:
        age = data['age']
        income = data['income']
        
        # Basic risk assessment logic
        if age < 18 or income < 20000:
            return "High Risk"
        elif age < 30 or income < 50000:
            return "Medium Risk"
        else:
            return "Low Risk"
    except KeyError:
        return "Error: Missing data"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# Create Gradio interface
iface = gr.Interface(
    fn=check_risk,
    inputs=gr.Dropdown(label="Select Data", choices=["Input Data Manually", "Example 1", "Example 2"]),
    outputs="text",
    title="Risk Control System",
    description="Use this system to evaluate risk based on different scenarios."
)

# Define example data for dropdown options
examples = [
    {'age': 25, 'income': 30000},
    {'age': 45, 'income': 120000}
]

# Update interface with examples
iface.input.choices = examples
iface.input.select_multiple = False
iface.input.option_rename = {"Example 1": examples[0], "Example 2": examples[1]}

# Launch the application
iface.launch()