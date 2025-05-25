from flask import Flask, render_template, request, jsonify
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Set OpenAI API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static',
    static_url_path='/static'
)

# Routes for static pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.get_json()
    try:
        submissions = []
        if os.path.exists('submissions.json'):
            with open('submissions.json', 'r') as f:
                try:
                    submissions = json.load(f)
                except json.JSONDecodeError:
                    submissions = []
        submissions.append(data)
        with open('submissions.json', 'w') as f:
            json.dump(submissions, f, indent=4)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return render_template('chat.html')
    
    user_msg = request.json.get('message', '')
    if not user_msg:
        return jsonify({'status': 'error', 'message': 'No message provided'}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": (
                        "You are a knowledgeable legal assistant specializing in the laws and legal systems "
                        "of Azerbaijan and other post-Soviet countries. Your responses should be clear, realistic, "
                        "and helpful, but note that this is a simulated assistant for a university project only. "
                        "The information you provide is not legally binding and should not be used for real legal decisions. "
                        "Always remind users to consult a qualified lawyer for real legal matters."
                    )
                },
                {"role": "user", "content": user_msg}
            ]
        )
        bot_msg = response.choices[0].message.content.strip()
        return jsonify({'response': bot_msg})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
