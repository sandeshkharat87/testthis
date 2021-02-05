from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from forms import Reg
import joblib

model = joblib.load("iris.pkl")


app = Flask(__name__)

bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


@app.route('/', methods=('GET', 'POST'))
def submit():
    data = None
    # form = MyForm()

    form = Reg()
    if form.validate_on_submit():
        print(dict(request.form).values)
        data = request.form.to_dict().values()
        data = list(data)[1:-1]
        data = [float(i) for i in data]
        data = model.predict([data])[0]

    return render_template('home.html', form=form, data=data)


if __name__ == '__main__':
    app.run(debug=True)
