from flask import Flask, render_template, jsonify

app = Flask(__name__)

TITLE = "Recruitin Careers"

JOBS = [{
  "id": 1,
  "title": "Data Analyst",
  "location": "Delhi",
  "salary": "Rs. 15,00,000"
}, {
  "id": 2,
  "title": "Java Developer",
  "location": "Pune",
  "salary": "Rs. 9,00,000"
}, {
  "id": 3,
  "title": "Python Developer",
  "location": "Noida",
  "salary": "Rs. 11,00,000"
}, {
  "id": 4,
  "title": "Android Developer",
  "location": "Chennai",
  "salary": "Rs. 7,00,000"
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, title=TITLE)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
