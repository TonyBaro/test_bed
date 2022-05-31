from flask import Flask, render_template, request, redirect, session
from friend import Friend
app = Flask(__name__)
app.secret_key = 'nobody_knows_the_trouble_ive_seen'

@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends[0].first_name)
    return render_template('index.html', all_friends = friends)

if __name__=='__main__':
    app.run(debug=True)