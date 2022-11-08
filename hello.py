from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route('/user/<username>')
def hello_user(username):
    # show the user profile for that user
    return f'<h1>Hello {username}</h1>'

if __name__ == "__main__":
    app.run(debug=True,
            host='0.0.0.0',
            port=9000,
            threaded=True)