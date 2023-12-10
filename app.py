from flask import Flask, request, send_from_directory
from calendar_main import add_event
from prompt_gpt import parse_input

openaiKey = 'your-openai-api-key'

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('.', 'index.html')

@app.route('/message', methods=['POST'])
def handle_message():
    print('message received')
    message = request.form['message']
    response = process_message(message)
    return response

def process_message(message):
    # Your code to process the message
    print('received:', message)

    parse_input(message, openaiKey)

    print('adding event...')
    add_event()
    print('finished!')

    return "Processed"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
