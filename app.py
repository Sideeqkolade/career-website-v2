from flask import Flask, render_template, jsonify, request
from database import load_jobs_db, load_job_db, add_application_to_db

app = Flask(__name__)


@app.route('/')
def hello_sidnify():
  jobs = load_jobs_db()
  return render_template("home.html", jobs=jobs, company_name='Sidnify')


@app.route('/api/jobs')
def list_jobs_db():
  jobs = load_jobs_db()
  return jsonify(jobs)


@app.route('/job/<id>')
def show_job(id):
  job = load_job_db(id)

  if not job:
    return ("Not Found", 404)

  return render_template('jobpage.html', job=job)


@app.route('/api/job/<id>')
def show_job_json(id):
  job = load_job_db(id)
  return jsonify(job)


@app.route('/job/<id>/apply', methods=['post'])
def apply_job(id):
  data = request.form
  job = load_job_db(id)
  add_application_to_db(id, data)
  return render_template("application_submitted.html",
                         application=data,
                         job=job)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
