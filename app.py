from Keys import *
from anthropic import Anthropic
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET','POST'])
def chat():
    user_input = request.form.get('user_input', '')

    # Initialize Anthropic client
    anthropic = Anthropic(api_key=CLAUDE_SONET_API)

    # Get response from Claude
    message = anthropic.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": user_input
        }]
    )

    return {'response' : message.content[0].text}

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        
        # Initialize Anthropic client
        anthropic = Anthropic(api_key=CLAUDE_SONET_API)
        
        # Get response from Claude
        message = anthropic.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": user_input
            }]
        )
        
        # Extract the response text
        user_response = message.content[0].text
        response = {
            'prompt' : user_input,
            'response' : user_response
        }
        print(f"User Input response : {response}")
        return render_template('response.html', result=user_response)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
