from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import MealtimeForm
from app.meal import Meal
from app.main import FoodProcessor

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=["GET", "POST"])
def index():
    form = MealtimeForm()
    fp = FoodProcessor()
    fp.addInfo()
    if form.validate_on_submit():
        return render_template('index.html', title="Food Selector", form=form, fp=fp)
        
    return render_template('index.html', title="Food Selector", form=form, fp=fp)

if __name__ == '__main__':
    app.run()