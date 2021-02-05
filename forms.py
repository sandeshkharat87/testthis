from flask_wtf import FlaskForm
import wtforms as wt

class Reg(FlaskForm):

    sl = wt.FloatField("sl")
    sw = wt.FloatField("sw")
    pl = wt.FloatField("pl")
    pw = wt.FloatField("pw")
    submit = wt.SubmitField("Predict")
