# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Sun May 31 11:08:17 2020
Name of file: service.py

@author: Andres Torres Garcia
@description: Rogo Technical Evaluation. Challenge number 3
"""

from models import TaskModel


class TaskService:
    def __init__(self):
        self.model = TaskModel()

    def add(self, params):
        return self.model.add(params)

    def update(self, item_id, params):
        return self.model.update(item_id, params)

    def delete(self, item_id):
        return self.model.delete(item_id)

    def list(self):
        response = self.model.list_items()
        return response
