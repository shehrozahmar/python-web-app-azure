from flask import Flask
import logging           


app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.INFO)


@app.route('/')
def hello():
    return 'Hello, World! This is my Azure VM.'

@app.route('/local-url')
def local_url():
    logging.info('Local URL accessed: /local-url')
    # Your route logic here
    return 'Hello from local URL!'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
