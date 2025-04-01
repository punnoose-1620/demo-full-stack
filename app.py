from Keys import *
from controllers import getResponse, responseReturnChatHandlers, generic_error_response
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

    response = getResponse(user_input=user_input)
    return {'response': responseReturnChatHandlers(response=response)}
        

@app.route('/generate', methods=['GET', 'POST'])
def generate():

    if request.method == 'POST':
        user_input = request.form.get('user_input', '')

        response = getResponse(user_input=user_input)
        return render_template('response.html', result=responseReturnChatHandlers(response=response))

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
