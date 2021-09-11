from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from sqlalchemy import String
from wtforms import StringField, SubmitField

app = Flask(__name__)
# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'mysecretkey'


# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html


class SimpleForm(FlaskForm):
    breed = StringField("What breed are you?")
    # Just One Button
    submit = SubmitField('Click Me.')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"You just changed the breed to {session['breed']}!")

        return redirect(url_for('index'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
