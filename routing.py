from flask import Flask
app = Flask(__name__)
@app.route('/home')
def home():
    return "hello, welcome to our website";
@app.route('/about')
def about():
    return "hello, welcome to our 2nd website";
@app.route('/gallery')
def gallery():
    return "hello, welcome to my profile";
if __name__ =="__main__":
    app.run(debug = True)
