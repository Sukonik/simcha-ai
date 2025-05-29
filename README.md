# Simcha AI

A Jewish-themed AI chatbot with three selectable personas: Rabbi, Student, and Israeli. Built with Flask and OpenAI's GPT API.

## Features

- Three distinct AI personas with unique Jewish perspectives
- Modern, ChatGPT-like interface
- Real-time chat functionality
- Responsive design for mobile and desktop

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/simcha-ai.git
cd simcha-ai
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

5. Add your logo:
Place your Menorah logo image in the `static/img` directory as `logo.png`.

## Running the Application

1. Start the Flask server:
```bash
python3 app.py
```

2. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Usage

1. Select a persona from the dropdown menu:
   - Rabbi: Traditional Jewish law and Torah-based answers
   - Student: Casual, yeshiva-style responses
   - Israeli: Hebrew slang and modern Israeli perspective

2. Type your message in the input box and press Enter or click the send button.

3. The AI will respond in the style of the selected persona.

## Project Structure

```
simcha-ai/
├── static/
│   ├── css/
│   │   └── style.css
│   └── img/
│       └── logo.png
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 