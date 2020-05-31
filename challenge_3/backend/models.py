# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Sun May 31 11:06:02 2020
Name of file: models.py

@author: Andres Torres Garcia
@description: Rogo Technical Evaluation. Challenge number 3
"""

import sqlite3


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('tasks.db')
        self.create_to_do_table()

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Tasks" (
          id INTEGER PRIMARY KEY,
          Description TEXT,
          _is_done boolean DEFAULT 0
        );
        """

        self.conn.execute(query)

class TaskModel:
    TABLENAME = "Tasks"

    def __init__(self):
        self.conn = sqlite3.connect('tasks.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def get_by_id(self, _id):
        where_clause = f"WHERE id={_id}"
        return self.list_items(where_clause)

    def add(self, params):
        query =  f'insert into {self.TABLENAME} ' \
                 f'(Description) ' \
                 f'values ("{params.get("Description")}")'
        print(query)
        result = self.conn.execute(query)
        return self.get_by_id(result.lastrowid)

    def delete(self, item_id):
        query = f"DELETE FROM {self.TABLENAME} " \
                f"WHERE id = {item_id}"
        print (query)
        self.conn.execute(query)
        return self.list_items()

    def update(self, item_id, update_dict):
        """
        column: value
        Title: new title
        """
        set_query = " ".join([f'{column} = {value}'
                     for column, value in update_dict.items()])

        query = f"UPDATE {self.TABLENAME} " \
                f"SET {set_query} " \
                f"WHERE id = {item_id}"
        self.conn.execute(query)
        return self.get_by_id(item_id)

    def list_items(self, where_clause=""):
        query = f"SELECT id, Description, _is_done " \
                f"from {self.TABLENAME} " + where_clause
        print (query)
        result_set = self.conn.execute(query).fetchall()
        result = [{column: row[i]
                  for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result
