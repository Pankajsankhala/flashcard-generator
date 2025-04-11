import gradio as gr
import google.generativeai as genai

# Replace with your Gemini API key
genai.configure(api_key="AIzaSyBjoKFZ92lqV23wevSosBYlqyUGquoDqMU")

# Gemini model setup
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# Function to generate flashcards
def generate_flashcards(input_text):
    prompt = f"""
You are an assistant that creates flashcards for learning engineering concepts.
Generate 5 flashcards from the following text. Each flashcard should be in the format:
Q: <question>
A: <answer>

Text: {input_text}
"""
    response = model.generate_content(prompt)
    return response.text.strip()

# Gradio UI
iface = gr.Interface(
    fn=generate_flashcards,
    inputs=gr.Textbox(lines=10, label="Enter Engineering Concept Text"),
    outputs=gr.Textbox(lines=15, label="Generated Flashcards"),
    title="Engineering Flashcard Generator",
    description="Enter engineering notes or a concept description. This app uses Gemini to generate study flashcards."
)

# Launch the app
iface.launch()
