from flask import Flask, request, render_template, jsonify
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

app = Flask(__name__)

# Load BlenderBot model
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    # Tokenisasi input
    inputs = tokenizer([user_input], return_tensors="pt")
    result = model.generate(**inputs)
    reply = tokenizer.decode(result[0], skip_special_tokens=True)

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)