#Importing library 
from flask import Flask, render_template, jsonify
app = Flask(__name__)
JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Tunis,Tunisa',
    'salary':'Dt. 1000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Tunis,Tunisa',
    'salary':'Dt. 1100'
  },
  {
    'id':3,
    'title':'Cloud Architect',
    'location':'Remote',
  },
  {
    'id':4,
    'title':'IoT Engineer',
    'location':'Nashville, Tennesses, USA',
    'salary':'$ 3000'
  }
]
@app.route('/')
def hello_word():
  return render_template('home.html', jobs=JOBS, company_name="EcoLink")

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

