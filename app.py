from flask import Flask, render_template
import random
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

if __name__ == '__main__':
    app.run()