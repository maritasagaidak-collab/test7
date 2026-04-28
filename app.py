from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    stats = [
        {
            "title": "БАЛАНС",
            "value": "45,250 ₴",
            "desc": "Активний рахунок",
            "color": "text-success"
        },
        {
            "title": "КУРС USD",
            "value": "41.10 ₴",
            "desc": "+0.15% сьогодні",
            "color": "text-success"
        },
        {
            "title": "КУРС EUR",
            "value": "44.55 ₴",
            "desc": "-0.05% сьогодні",
            "color": "text-danger"
        }
    ]
    return render_template('index.html', stats=stats)


app.run(debug=True)