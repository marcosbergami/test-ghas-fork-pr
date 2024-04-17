from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    user_name = request.args.get('user_name')
    return f'<h1>Welcome, {user_name}!</h1>'
