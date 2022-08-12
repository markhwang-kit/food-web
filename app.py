import imp
from flask import Flask, render_template
import random
import movie

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
    # return 'Hello, World!'

@app.route('/naver')
def naver():
    return '네이버 사이트'

@app.route('/food')
def food():
    foodlist = ["짜장면", "짬뽕", "탕슉", "우동", "돈까스"]
    foodname = random.choice(foodlist)
    return render_template('food.html', data=foodname)

@app.route('/movie')
def movieurl():
    titles = movie.get_rank()
    return render_template('movie.html', data=titles)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)