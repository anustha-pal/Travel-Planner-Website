from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory store (you can replace this with a database)
plans = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_plan', methods=['POST'])
def add_plan():
    destination = request.form['destination']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    activities = request.form['activities']

    plan = {
        'destination': destination,
        'start_date': start_date,
        'end_date': end_date,
        'activities': activities
    }

    plans.append(plan)
    return redirect(url_for('view_plans'))

@app.route('/plans')
def view_plans():
    return render_template('plans.html', plans=plans)

if __name__ == '__main__':
    app.run(debug=True)
