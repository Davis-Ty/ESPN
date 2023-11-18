from setDriver import *
from flask import Flask, request

app = Flask(__name__)

@app.route('/run_script', methods=['POST'])
def run_script():
    # Execute our Python script here
    setDriver()
    return 'Script executed successfully'

if __name__ == '__main__':
    app.run(debug=True)
