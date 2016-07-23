from bottle import route, run, template, post, get
import json

@route('/index')
def index():
	benefit = 3
    return template('home.tpl', benefit = 3)

@post('/index')
def submit_job_posting():
	email = request.forms.get('email')
	compName = request.forms.get('compName')
	jobTitle = request.forms.get('jobTitle')
	skillReq = request.forms.get('skillReq')
	trainMat = request.forms.get('trainingMaterial')
	hourlyWage = request.forms.get('hourlyWage')
	budget = request.forms.get('budget')
	numPos = request.forms.get('numPos')
	waitTime = request.forms.get('waitTime')
	#DB handling
	calculatedBenefit = 2;	
	return template('home.tpl',benefit = 2)

run(host='localhost', port=8080)