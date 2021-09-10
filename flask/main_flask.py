from flask import Flask, request
from flask import render_template
from ufw.util import debug

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Sample endpoint
    :return: str html rendered
    """
    # return '<h1>Hello World</h1>'
    # puppy_name = 'Rufas'
    #
    # puppy_description = ['The name is Rufas', 'I am 1 year old']
    # dict_puppy_detailed = {'Age': 1, 'Colour': 'Golden', "Breed": "Golden Retriever"}

    # render the template
    # here we are using jinja template to send a variable to html
    # here we are going to use home.html and that html is going to extend base.html
    # this is inheritance in html
    # return render_template('basic.html')
    return render_template('home.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signup_form')
def signup_form():
    return render_template('signup_form.html')


@app.route('/thankyou')
def thank_you():
    # grab parameters from request
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thankyou.html', first=first, last=last)


@app.route('/information')
def info() -> str:
    """
    Added another info page
    :return: a page for puppy information
    """
    return '<h3> Puppies are cute !</h3>'


@app.route('/puppy/<name>')
def puppy(name: str) -> str:
    # return f'This is a puppy page {name}'

    puppy_description = ['The name is ' + name, 'I am 1 year old']
    dict_puppy_detailed = {'Age': 1, 'Colour': 'Golden', "Breed": "Golden Retriever"}
    return render_template('puppy.html', name=name,
                           puppy_description=puppy_description,
                           dict_puppy_detailed=dict_puppy_detailed)


@app.route('/puppy/<name>/internalerror')
def puppy_error(name: str) -> str:
    return f'This is a puppy page with error{name[100]}'


@app.route('/puppy/<name>/latin')
def puppy_name_to_latin(name: str) -> str:
    if name[::-1][0].lower() != 'y':
        latin_name = name + 'y'
        return latin_name
    else:
        latin_name = name[:len(name) - 1:] + 'iful'
        return latin_name


@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404
    :return:
    """
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
