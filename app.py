from flask import Flask, render_template, request
from config import getkey
from google import genai

# Create Flask application
app = Flask(__name__)

# Gemini Client
client = genai.Client(api_key=getkey())


@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""
    question = ""

    if request.method == "POST":

        question = request.form.get("question", "").strip()

        if question:
            try:
                response = client.models.generate_content(
                    model="gemini-flash-lite-latest",
                    contents=question
                )

                answer = response.text

            except Exception as e:
                answer = f"Error: {str(e)}"

    return render_template(
        "index.html",
        answer=answer,
        question=question
    )


if __name__ == "__main__":
    app.run(debug=True)