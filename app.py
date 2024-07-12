from flask import Flask, render_template, request
from database import add_contact, init_db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    add_contact(name, email, message)
    return 'Thank you for contacting us, {}!'.format(name)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)