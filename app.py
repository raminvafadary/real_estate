from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        # Here, you could send an email or store to a DB
        return redirect(url_for("thank_you"))
    return render_template("contact.html")

@app.route('/thank-you')
def thank_you():
    return render_template("thank_you.html")

if __name__ == '__main__':
    app.run(debug=True)
