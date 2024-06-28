from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {
        'title': 'Python Developer',
        'location': 'Remote',
        'salary': '100k'
    },
    {
        'title': 'Data Analyst',
        'location': 'Remote',
        'salary': '120k'
    },
    {
        'title': 'Data Scientist',
        'location': 'Remote',
        'salary': '150k'
    },
    {
        'title': 'Frontend Developer',
        'location': 'Remote',
        'salary': '80k'
    },
    {
        'title': 'Backend Developer',
        'location': 'Remote',
        'salary': '90k'
    },
]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=jobs)


@app.route('/api/jobs')
def list_jobs():
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
