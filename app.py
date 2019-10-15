from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
	return "HI"


if __name__=="__main__":
	app.run()