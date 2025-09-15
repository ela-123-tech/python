from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Simple Web App!</h1><p>Go to /hello to say hi.</p>"

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        name = request.form.get("name", "Guest")
        return f"<h2>Hello, {name}! 👋</h2>"
    return '''
        <form method="POST">
            <input type="text" name="name" placeholder="Enter your name">
            <button type="submit">Say Hello</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
