"""
Sample Python Flask web  application
"""
import forms
from flask import Flask, request, render_template, flash

# Create flask application
application = Flask(__name__)

# Load configuration data
application.config.from_pyfile('config.py')

@application.route('/')
@application.route('/index', methods=['GET', 'POST'])
def index():
    form = forms.MyForm()
    if form.validate_on_submit():
        username = request.form.get('user_name')
        flash(f'Thanks, {username}, for trying the examples!!')
    return render_template('index.html', form=form)

@application.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

if __name__ == '__main__':
    application.run(port=5000, debug=True)
