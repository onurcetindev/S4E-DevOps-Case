from flask import Flask, render_template, request
from AI_assistant import generate_code_and_title

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    title = ""
    code = ""
    is_loading = False
    if request.method == "POST":
        user_prompt = request.form.get("prompt")
        if user_prompt:
            is_loading = True
            title, code = generate_code_and_title(user_prompt)
            is_loading = False
    return render_template("index.html", title=title, code=code, is_loading=is_loading)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)