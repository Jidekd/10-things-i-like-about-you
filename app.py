from flask import Flask, render_template

app = Flask(__name__)

reasons = [
    "I love how you meet my overthinking with patience instead of frustration.",
    "I love how you remember even the smallest things about me. It makes me feel like you genuinely want to know me, not just the easy parts.",
    "I love the way you smile, and especially your eyes. There’s just something about them that gets me every time.",
    "I love how you somehow bring out a version of me that no one else has ever been able to get—not even me.",
    "I love how concerned you are about how I feel. You somehow know when something’s wrong even when I don't say anything.",
    "I love how you can read me like a book. Somehow, you just know when my mind isn't in the right place.",
    "I love how comfortable you make me feel. With you, I don't feel like I have to pretend to be someone else. I can just be myself.",
    "I love that you remind me of no one else. You're just completely you, and honestly, I wouldn't want you any other way.",
    "I love how you take care of me when you know I'm not in the right state of mind. You make me feel looked after without making me feel weak.",
    "And I love how much you get under my skin. You get into my head, you make me overthink, you make me smile, and somehow you became someone I can't help but care about so much."
]

@app.route("/")
def home(): 
    return render_template("index.html", reasons=reasons)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)