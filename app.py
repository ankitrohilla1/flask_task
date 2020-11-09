from flask import Flask, render_template, request, redirect,jsonify
import os
#from flask_mysqldb import MySQL
import yaml
import json

app = Flask(__name__)

# Configure db
tasks = []
task1 = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        storage_path = 'filtered_data_file.json'
        data = None
        if os.path.exists(storage_path):
            with open(storage_path, 'r') as f:
                try:
                    data = json.load(f)
                    print('loaded that: ', data)
                except Exception as e:
                    print("got %s on json.load()" % e)

        if data is None:
            data_base = []
            with open(storage_path, 'w') as f:
                json.dump(data_base, f)
        # Fetch form data
        userdetails = request.form
        name = userdetails['name']
        email = userdetails['email']
        new_task = create_user_id(name, email, data)
        if data is None:
            data = []
        data.append(new_task)
        with open("filtered_data_file.json", "w") as data_file:
            json.dump(data, data_file, indent=2)
        #return redirect('/users')
        #return "success"
    return render_template('index.html')

def create_user_id(name, email,data):
    if data is None:
        user = {
            'id': 1,
            'name': name,
            'email': email
        }
    else:
        user = {
            'id': data[-1]['id'] + 1,
            'name': name,
            'email': email
        }

    return user

@app.route('/users')
def users():
    #return jsonify({'tasks': tasks})
    userDetails = ["My_computer", "lol"]
    return render_template('users.html', userDetails=userDetails)

if __name__ == '__main__':
    app.run()
