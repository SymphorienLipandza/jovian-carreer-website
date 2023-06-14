#Importing library 

from flask import Flask, render_template, jsonify, request
from flask_restful import Api, Resource
import yaml
from flask import Flask, render_template, jsonify,request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
from email_sender import send_email

#Main app and api
app = Flask(__name__)
api = Api(app)

#The index page
@app.route('/')
def index():
  jobs=load_jobs_from_db()
  return render_template('home.html', jobs=jobs)

#Jobs listing 
@app.route('/api/jobs')
def list_jobs():
  jobs=load_jobs_from_db()
  return jsonify(jobs)

#api specification
class JobSpec(Resource):
    def get(self):
        with open('jobs_api_spec.yaml', 'r') as file:
            spec = yaml.safe_load(file)
        return spec

api.add_resource(JobSpec, '/api/jobies.yaml')

#job api 
@app.route('/api/job/<id>')
def show_job_json(id):
  job= load_job_from_db(id)
  return jsonify(job)

#Job's page 
@app.route("/job/<id>")
def show_job(id):
  job= load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', job=job)
  

@app.route('/job/<id>/applay', methods=['post'])
def applay_to_job(id):
  data = request.form
  job=load_job_from_db(id)
  add_application_to_db(id, data)
  # Send email to the applicant
  if job:
    to_email = data['email']
    subject = 'Application Submitted for Job: {}'.format(job['title'])
    message = 'Dear {},\n\nThank you for applying for the job: {}\n\nWe have received your application and will review it shortly.\n\nBest regards,\nEcoLink Ltd'.format(data['full_name'], job['title'])
    send_email(to_email, subject, message)
  
  return render_template('applicationsubmitted.html',application=data, job=job)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)





            