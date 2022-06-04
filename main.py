from flask import Flask, redirect, render_template, request, url_for, flash, session, escape, request
import util

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def main_page():

    currencies = util.prices.keys()

    return render_template('main.html', currencies=currencies)



@app.route('/change', methods=['GET', 'POST'])
def change():

    if request.method == "POST":
        currency = request.form['to-what']
        after_change = util.changer(request.form['from-what'], request.form['to-what'], request.form['amount'])


    return render_template('change.html', after_change=after_change, currency=currency)



if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True
    )
