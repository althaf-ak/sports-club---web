from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    sport = request.form["sport"]
    phone = request.form["phone"]

    return f"""

    <html>

    <head>

    <title>Registration Successful</title>

    <style>

    body{{
        background:#111;
        color:white;
        font-family:Arial;
        text-align:center;
        padding-top:100px;
    }}

    h1{{
        color:lime;
    }}

    .box{{
        width:500px;
        margin:auto;
        background:#222;
        padding:30px;
        border-radius:15px;
        box-shadow:0px 0px 20px cyan;
    }}

    </style>

    </head>

    <body>

    <div class="box">

    <h1>Registration Successful</h1>

    <h2>Welcome {name}</h2>

    <p><b>Age :</b> {age}</p>

    <p><b>Gender :</b> {gender}</p>

    <p><b>Sport :</b> {sport}</p>

    <p><b>Phone :</b> {phone}</p>

    <br>

    <a href="/" style="color:cyan;">Go Back</a>

    </div>

    </body>

    </html>

    """


if __name__ == "__main__":
    app.run(debug=True)