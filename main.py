from flask import Flask, app, render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/contact',methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('//about',methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)