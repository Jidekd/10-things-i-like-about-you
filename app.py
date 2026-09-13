from flask import Flask, render_template

app = Flask(__name__)

reasons = [
    "I like you.",
    "I like your smile.",
    "I like your eyes.",
    "I like how you can make me open up to you.",
    "I like how I can just be myself around you.",
    "I like how bossy you can be with me HAHAHA.",
    "I like how you worry about me.",
    "I like how you already reassure me before I even get the chance to overthink.",
    "I like that you're always there when I need someone to rant to.",
    "I like you. I meant it."
]

@app.route("/")
def home(): 
    return render_template("index.html", reasons=reasons)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)