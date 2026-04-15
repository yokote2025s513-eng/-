from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        year = int(request.form["year"])
        a = float(request.form["a"])
        d = float(request.form["d"])
        rate = float(request.form["rate"])

        months = year * 12
        r = rate / 12

        total = 0
        for i in range(months):
            total = total * (1 + r) + (a + d * i)

        result = total

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

