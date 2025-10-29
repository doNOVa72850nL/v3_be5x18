# 代码生成时间: 2025-10-29 08:19:31
import gradio as gr
def generate_learning_path(user_input):
    """
    Generate a personalized learning path based on user input.
    Args:
    user_input (dict): A dictionary containing user's information and preferences.
    Returns:
    str: A personalized learning path.
    """
    try:
        # Extract user information from the input dictionary
        user_age = user_input.get('age', 0)
        user_interests = user_input.get('interests', [])
        user_experience = user_input.get('experience', '')
        
        # Define the learning path based on user's age, interests, and experience
        learning_path = ""
        if user_age < 18:
            learning_path += "Beginner courses
"
        elif 18 <= user_age < 30:
            learning_path += "Intermediate courses
"
        else:
            learning_path += "Advanced courses
"
        
        for interest in user_interests:
            learning_path += f"Course on {interest}
"
        
        if user_experience == 'none':
            learning_path += "Start with basic courses
"
        elif user_experience == 'some':
            learning_path += "Start with intermediate courses
"
        else:
            learning_path += "Start with advanced courses
"
        
        return learning_path
    except Exception as e:
        return f"Error generating learning path: {str(e)}"

# Define the Gradio interface
iface = gr.Interface(
    fn=generate_learning_path,
    inputs=[
        gr.Textbox(label="Age"),
        gr.CheckboxGroup(label="Interests", choices=["Math", "Science", "History", "Art"]),
        gr.Radio(label="Experience", choices=["none", "some", "a lot"])
    ],
    outputs="text"
)

# Run the Gradio interface
iface.launch()