from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def chart():
    goalAmount = 450000
    collectedAmount = 32000
    amountRemaining = goalAmount - collectedAmount
    labels = ["Collected", "Goal"]
    values = [collectedAmount, amountRemaining]
    colors = ["#88FF88", "#FF9494"]
    return render_template('chart.html', set=zip(values, labels, colors))

if __name__ == "__main__":
    app.run(debug=True)
