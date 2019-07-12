from flask import Flask,render_template,request
from weatherreport import weather_info

app=Flask(__name__)

@app.route('/',methods = {'GET','POST'})
def home():
	if request.method =='POST':
		city=request.form['city']
		units=request.form['units']
		info=weather_info(city,units)
		return render_template('home.html',title='home page',info=info)
	return render_template('home.html',title='home page')

''''@app.route('/about')
def about():

		return render_template('about.html',title='prasanth')

@app.route('/contact')
def contact():

		return render_template('contact.html',title='contact')
'''
app.run(debug=True)