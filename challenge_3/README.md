# Challenge 3

## Approach problem summary

My initial thoughts in solving this problem is to use a web app since a web app can run on any platform that has a browser. Then, I'll look for a web stack that meets the basic requirements. Since any stack will be able to meet those requirements, I decided to use the one that you listed as Bonus in the job listing for Software Engineer (Full Stack) - Full Time: Python/Flask + REST APIs + ReactJS Frontend.

## Installation

- The script can run on any OS(Windows, MacOS, Linux, etc.) with Python 3.* installed.

### Install dependencies backend

Recommended: Install these packages in a python3.6 virtual environment.

```bash
pip install flask
pip install sqlite3
pip install json
```

### Install dependencies frontend

Recommended: Install these packages in a python3.6 virtual environment.

Install dependencies. Make sure you already have [`nodejs`](https://nodejs.org/en/) & [`npm`](https://www.npmjs.com/) installed in your system.

```bash
$ sudo apt update
$ sudo apt install nodejs
$ sudo apt install npm
```

## Usage

In order to start the backend, run the following script assuming you are on a Unix platform:

```bash
cd ~/worktest/challenge_3/backend
python app.py
```

In order to start the frontend, run the following script assuming you are on a Unix platform:

```bash
cd ~/worktest/challenge_3/frontend/react-todo-app
python script.py
```

```bash
$ npm install # or yarn
```

Run it
```bash
$ npm start # or yarn start
```

## Details about the implementation

The backend is using the Python/Flask stack. I'm following the MVC -- Model View Controller Pattern by separating the app into three different files: 

- app.py -- Application layer - The entry and exit point to our application.
- service.py -- Logic layer - Converts the requests into a response.
- models.py -- Data layer - Handles everything that involves a Database.

For the frontend, I'm using a sample ToDo App from [https://github.com/kabirbaidhya/react-todo-app.git] and modified to fit the basic requeriments for challenge number 3.

## Short summary of the status of the app

The backend stack of the app is fully functional, i.e., you can add tasks, delete tasks, mark tasks as completed. I tested this functionality by using the python package 'requests' to consume APIs with Python.

For the frontend stack, I haven't tested it yet. I did the necessary changes in the `todo.js` file where you use the REST methods (GET, POST, PUT, DELETE) to make use of the API in the backend stack. Another thing that I'm missing is to deploy the backend and the frontend on a server. That way, one would be able to access the frontend on any device with a web browser.

## License
[MIT](https://choosealicense.com/licenses/mit/)