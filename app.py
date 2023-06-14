from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'New York, USA',
  'salary': '$100,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Ontario, Canada',
  'salary': '120,000 CAD'
}, {
  'id': 3,
  'title': 'DevOps Engineer',
  'location': 'California, USA',
  'salary': '$90,000'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Remote',
  'salary': '$80,000'
}]


@app.route('/')
def hello_sidnify():
  return render_template("home.html", jobs=JOBS, company_name='Sidnify')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
