import httpx
from Keys import *
import google.generativeai as genai
from anthropic import Anthropic, APIConnectionError
from google.api_core.exceptions import PermissionDenied, Unauthenticated

ANTHROPIC_MODEL = 'claude-3-5-sonnet-20241022'
GEMINI_MODEL = 'gemini-1.5-flash-002'
MAX_TOKENS = 1024
ROLE = 'user'

generic_error_response = 'Unable to perform this chat'
connection_error_response = 'ConnectionError'
timeout_error_response = 'TimeoutError'
connect_error_response = 'ConnectError'
api_connection_error_response = 'APIConnectionError'
permission_denied_error = 'PermissionDenied'
unauthenticated_error = 'UnAuthenticated'
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

def responseReturnChatHandlers(response):
    if(response['response'] is not None):
        return response['response']
    else:
        if(response['error']=='ConnectionError'):
            return 'Connection Error. Please check your wifi/ethernet connection.'
        elif(response['error']=='TimeoutError'):
            return 'Network Error. Please check your internet connectivity'
        elif(response['error']=='ConnectError'):
            return 'HTTP Connect Error'
        elif(response['error']=='APIConnectError'):
            return 'API Connection Error from Anthropic LLM'
        elif(response['error']=='PermissionDenied'):
            return 'You do not have the permissions required to perform this action. Please contact the server for more information.'
        elif(response['error']=='UnAuthenticated'):
            return 'Some error has occured within the system. Please contact the server for more information.'
        else:
            return generic_error_response

def getResponse(user_input: str):

    response = getAnthropicResponse(user_input=user_input)
    if(response['error'] is not None):
        response = getGoogleResponse(user_input=user_input)
    return response

def getAnthropicResponse(user_input: str):
    try:
        # Initialize Anthropic client
        anthropic = Anthropic(api_key=CLAUDE_SONET_API)

        # Get response from Claude
        message = anthropic.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=MAX_TOKENS,
            messages=[{
                "role": ROLE,
                "content": user_input
            }]
        )
        return {'response' : message.content[0].text, 'error': None, 'model': ANTHROPIC_MODEL}
    except ConnectionError as e:
        print(f'Connection Error : {e}')
        return {'response' : None, 'error': connection_error_response, 'model': ANTHROPIC_MODEL}
    except TimeoutError as e:
        print(f'Timeout Error : {e}')
        return {'response' : None, 'error': timeout_error_response, 'model': ANTHROPIC_MODEL}
    except httpx.ConnectError as e:
        print(f'Connect Error : {e}')
        return {'response' : None, 'error': connect_error_response, 'model': ANTHROPIC_MODEL}
    except APIConnectionError as e:
        print(f'API Connection Error : {e}\n  KEY : {CLAUDE_SONET_API}\n  MODEL: {ANTHROPIC_MODEL}\n  MAX-TOKENS: {MAX_TOKENS}\n  ROLE: {ROLE}')
        return {'response' : None, 'error': api_connection_error_response, 'model': ANTHROPIC_MODEL}
    except Exception as e:
        print(f'Unhandled Error : {e}')
        return {'response' : None, 'error': generic_error_response, 'model': ANTHROPIC_MODEL}

def getGoogleResponse(user_input: str):
    
    try:
        genai.configure(api_key=GEMINI_API)
        model = genai.GenerativeModel()
        response = model.generate_content(user_input, stream=False)
        print(f'Response Gemini : {response}')
        return {'response' : response.text, 'error': None, 'model': GEMINI_MODEL}
    except ConnectionError as e:
        print(f'Connection Error Gemini : {e}')
        return {'response' : None, 'error': connection_error_response, 'model': GEMINI_MODEL}
    except TimeoutError as e:
        print(f'Timeout Error Gemini : {e}')
        return {'response' : None, 'error': timeout_error_response, 'model': GEMINI_MODEL}
    except httpx.ConnectError as e:
        print(f'Connect Error Gemini : {e}')
        return {'response' : None, 'error': connect_error_response, 'model': GEMINI_MODEL}
    except PermissionDenied as e:
        print(f'Permission Denied Error Gemini : {e}\n  KEY: {GEMINI_API}\n  MODEL: {GEMINI_MODEL}')
        return {'response' : None, 'error': permission_denied_error, 'model': GEMINI_MODEL}
    except Unauthenticated as e:
        print(f'Authentication Error Gemini : {e}\n  KEY: {GEMINI_API}\n  MODEL: {GEMINI_MODEL}')
        return {'response' : None, 'error': unauthenticated_error, 'model': GEMINI_MODEL}
    except Exception as e:
        print(f'Unhandled Error Gemini : {e}')
        return {'response' : None, 'error': generic_error_response, 'model': GEMINI_MODEL}