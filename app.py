from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/init-call', methods=['POST'])
def init_call():
    data = request.get_json()
    print("Received call data:", data)

    return jsonify({
        "first_message": "Здравствуйте, чем могу помочь?",
        "variables": {
            "phone": data.get("from")
        }
    })

if __name__ == '__main__':
    app.run()
