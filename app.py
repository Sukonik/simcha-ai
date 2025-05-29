from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import secrets
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Generate a random secret key if not provided
# In production, set a strong, unique key via environment variable
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', secrets.token_hex(16))

# Initialize Mistral AI client
client = MistralClient(api_key=os.getenv('MISTRAL_API_KEY'))

# Persona prompts
PERSONA_PROMPTS = {
    'rabbi': "You are a wise and knowledgeable Rabbi, well-versed in Jewish law, Torah, and tradition. Provide thoughtful, traditional Jewish perspectives while maintaining a warm and approachable tone. Base your answers on Jewish sources and teachings.",
    'student': "You are a yeshiva student with a good sense of humor and a casual, friendly approach to Jewish learning. Share insights with a mix of knowledge and lightheartedness, using yeshiva-style expressions and references.",
    'israeli': "You are a modern Israeli with deep knowledge of Jewish culture and Israeli society. Respond with a mix of Hebrew slang, cultural references, and contemporary Israeli perspectives while maintaining Jewish values."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    persona = data.get('persona', 'rabbi')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    try:
        # Get response from Mistral AI
        messages = [
            ChatMessage(role="system", content=PERSONA_PROMPTS[persona]),
            ChatMessage(role="user", content=user_message)
        ]

        # Using a basic Mistral model suitable for a free tier
        response = client.chat(
            model="mistral-tiny", 
            messages=messages
        )
        
        ai_response = response.choices[0].message.content
        
        return jsonify({'response': ai_response})
    
    except Exception as e:
        # Log the error for debugging
        print(f"Error calling Mistral AI API: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # In production, use a production-ready WSGI server like Gunicorn
    # app.run(debug=True)
    # For local testing, you can still use debug=True
    app.run(debug=True) 