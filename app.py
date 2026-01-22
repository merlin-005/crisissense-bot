from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"].lower()

    if "earthquake" in msg:
        reply = "Drop, Cover and Hold On"
    elif "fire" in msg:
        reply = "Leave immediately and call fire service"
    elif "flood" in msg:
        reply = "Go to higher ground"
    else:
        reply = "I answer only emergency related questions"

    return jsonify({"reply": reply})

app.run()
