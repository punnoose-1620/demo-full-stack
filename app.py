import os
from Keys import *
from anthropic import Anthropic
from flask import Flask, render_template, request, redirect, url_for, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/favicon.ico")
def get_icon():
    return send_file("static/images/favicon.ico", mimetype="image/vnd.microsoft.icon")

@app.route('/chat', methods=['GET','POST'])
def chat():
    user_input = request.form.get('user_input', '')

    error_response = 'Unable to perform this chat'

    dummy_response = '''
    Sure! Here's a simple dummy HTML page with basic structure and styling, that you can use as a starting point:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Dummy Page</title>
    <style>
        body {
        background-color: #f5f5f5;
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 20px;
        }
        .container {
        background-color: white;
        max-width: 600px;
        margin: 50px auto;
        padding: 30px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border-radius: 12px;
        }
        .container h1 {
        color: #333;
        }
        .container p {
        color: #666;
        }
        .container button {
        padding: 10px 20px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        }
        .container button:hover {
        background-color: #45a049;
        }
    </style>
    </head>
    <body>

    <div class="container">
        <h1>Welcome to Dummy Page</h1>
        <p>This is a sample dummy page created for testing and development purposes.</p>
        <button onclick="alert('Button clicked!')">Click Me</button>
    </div>

    </body>
    </html>
    ```
    If you want, I can also:

    Add a simple form

    Add a chat-style UI

    Make it look like ChatGPT message area

    Add API call example

    Shall I?
    '''

    try:

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
    except Exception:
        return {'response' : dummy_response}

@app.route('/generate', methods=['GET', 'POST'])
def generate():

    error_response = 'Unable to perform this chat'

    dummy_response = '''
    Sure! Here's a simple dummy HTML page with basic structure and styling, that you can use as a starting point:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Dummy Page</title>
    <style>
        body {
        background-color: #f5f5f5;
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 20px;
        }
        .container {
        background-color: white;
        max-width: 600px;
        margin: 50px auto;
        padding: 30px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border-radius: 12px;
        }
        .container h1 {
        color: #333;
        }
        .container p {
        color: #666;
        }
        .container button {
        padding: 10px 20px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        }
        .container button:hover {
        background-color: #45a049;
        }
    </style>
    </head>
    <body>

    <div class="container">
        <h1>Welcome to Dummy Page</h1>
        <p>This is a sample dummy page created for testing and development purposes.</p>
        <button onclick="alert('Button clicked!')">Click Me</button>
    </div>

    </body>
    </html>
    ```
    If you want, I can also:

    Add a simple form

    Add a chat-style UI

    Make it look like ChatGPT message area

    Add API call example

    Shall I?
    '''

    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        try:
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
            # print(f"User Input response : {response}")
            return render_template('response.html', result=user_response)
        except Exception:
            return render_template('response.html', result=dummy_response)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
