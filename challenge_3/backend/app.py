# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Sun May 31 11:09:53 2020
Name of file: app.py

@author: Andres Torres Garcia
@description: Rogo Technical Evaluation. Challenge number 3
"""

from flask import Flask, request, jsonify
from service import TaskService
from models import Schema

import json

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name):
    return "Hello " + name


@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(TaskService().list())


@app.route("/tasks", methods=["POST"])
def add_tasks():
    return jsonify(TaskService().add(request.get_json()))


@app.route("/tasks/<item_id>", methods=["PUT"])
def update_item(item_id):
    return jsonify(TaskService().update(item_id, request.get_json()))


@app.route("/tasks/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    return jsonify(TaskService().delete(item_id))


if __name__ == "__main__":
    Schema()
    app.run(debug=True)
