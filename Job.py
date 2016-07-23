from elasticsearch import Elasticsearch
import json

class Job(object):
	"""docstring for Job"""
	def __init__(self, 
		company_name=None, 
		job_title=None, 
		wait_time=None,
		openings=None,
		budget=None,
		training=None,
		skills_needed=None,
		id=None):

		self.INDEX = "app"
		self.TYPE = "job_listing"

		self.company_name = company_name
		self.job_title = job_title
		self.wait_time = wait_time
		self.openings = openings
		self.budget = budget
		self.training = training
		self.skills_needed = skills_needed

		self.id = id

		self.elastic = Elasticsearch() 

	def save(self):
		try:
			job_listing_map={
				"company_name":self.company_name,
				"job_title":self.job_title,
				"wait_time":self.wait_time,
				"openings":self.openings,
				"budget":self.budget,
				"training":self.training,
				"skills_needed":self.skills_needed
			}

			resp = self.elastic.index(
					index=self.INDEX,
					doc_type=self.TYPE,
					body=job_listing_map
				)

			self.id = resp["_id"]

			return True
		except:
			return False

	def get_by_id(self, id):
		try:
			resp = self.elastic.get(
					index=self.INDEX,
					doc_type=self.TYPE,
					id=id
				)["_source"]
			
			self.company_name = resp["company_name"]
			self.job_title = resp["job_title"]
			self.wait_time = resp["wait_time"]
			self.openings = resp["openings"]
			self.budget = resp["budget"]
			self.training = resp["training"]
			self.skills_needed = resp["skills_needed"]
			self.id = id
			return True
		except:
			return False

	def get_as_json(self):
		self.get_by_id(self.id) # make sure to return the current version on the database
		return json.dumps({
			"company_name":self.company_name,
			"job_title":self.job_title,
			"wait_time":self.wait_time,
			"openings":self.openings,
			"budget":self.budget,
			"training":self.training,
			"skills_needed":self.skills_needed
		})

# Test #

if __name__ == "__main__":
	# Make sure job is created and saved 
	job1 = Job(
		company_name="testcasecentral", 
		job_title="developer", 
		wait_time=12,
		openings=1,
		budget=1000,
		training="/tmp/trainingsample.html",
		skills_needed="math 101")

	saved = job1.save()

	assert(saved)

	# Retrieve a job from db
	job2 = Job()
	gotit = job2.get_by_id(job1.id)

	assert(gotit)

	print str(job2.get_as_json())