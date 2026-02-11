from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    if "hello" in user_message or "hi" in user_message:
        reply = "Hello 👋 How can I help you with wildlife conservation?"
    elif "tiger" in user_message:
        reply = "Tigers are endangered due to habitat loss and illegal poaching."
    elif "elephant" in user_message:
        reply = "Elephants help maintain forest ecosystems and biodiversity."
    elif "rhino" in user_message:
        reply = "Rhinos are critically endangered mainly due to poaching."
    elif "forest" in user_message:
        reply = "Forests are essential for wildlife, climate balance, and human survival."
    elif "help" in user_message:
        reply = "You can ask me about animals, endangered species, and conservation."
    else:
        reply = "🌱 I'm still learning. Please ask about wildlife or conservation."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
