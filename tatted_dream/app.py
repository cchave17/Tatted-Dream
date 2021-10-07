from flask import Flask, render_template, url_for, request

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/bookAppointment", methods=["POST"])
def book_appointment():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
    return "FORM SUBMITTED"
