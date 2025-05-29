from flask import Flask, render_template, request, jsonify
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

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
        # Construct the full prompt with persona context
        full_prompt = f"{PERSONA_PROMPTS[persona]}\n\nUser: {user_message}\n\nAssistant:"
        
        # Get response from OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": PERSONA_PROMPTS[persona]},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        ai_response = response.choices[0].message.content
        
        return jsonify({'response': ai_response})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 