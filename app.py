from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Process the data (e.g., save to database or send an email)
    return 'Thank you for contacting us, {}!'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
