from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

def fizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBUzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "BUZZ";
    else:
        return str(num)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Python Backend Server is Running Successfully!</h1><p>Use index.html to interact with the API.</p>"

@app.route('/api/fizzbuzz', methods=['POST'])
def web_api():
    data = request.json
    user_num = int(data.get("num_input", 0))

    #Running the the Algorithm 
    result = fizzBuzz(user_num)

    return jsonify({"answer": result})

if __name__ == '__main__':
    app.run(port=5000, debug=True)