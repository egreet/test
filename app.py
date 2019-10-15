from flask import Flask,render_template
from app-Copy import demo
app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/sec')
def second():
	return demo()

if __name__=="__main__":
	app.run()