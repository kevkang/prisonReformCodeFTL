from bottle import route, run, template, post, get, request
import json
from Job import Job

@route('/index')
def index():
    return template('home.tpl', benefit = None)

@post('/index')
def submit_job_posting():
	email = request.forms.get('email')
	print("email:" + email)
	compName = request.forms.get('compName')
	print("compName:" + compName)
	jobTitle = request.forms.get('jobTitle')
	print("jobTitle:" + jobTitle)
	skillReq = request.forms.get('skillReq')
	openings = request.forms.get('openings')
	trainMat = request.forms.get('trainingMaterial')
	budget = request.forms.get('budget')

	waitTime = request.forms.get('waitTime')


	#DB handling
	newJob = Job(compName, jobTitle, waitTime, openings, budget, trainMat, skillReq)
	if(newJob.save()):
		#yay
		print("success")
	else:
		print("error!")
	return template('home.tpl',benefit = 2)

run(host='localhost', port=8080)