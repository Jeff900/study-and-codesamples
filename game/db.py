import sqlite3
from os.path import getsize

class Database():

    def __init__(self, db_name='stranded.db'):
        self.db_name = db_name
        self.db = sqlite3.connect(db_name)
        self.cursor = self.db.cursor()
        self.create_database()

    def create_database(self):
        """create sqlite database if no database is already created"""
        print(f'Checking database {self.db_name}')

        if getsize(self.db_name) <= 0:
            print('Database seems to be empty. Configuring database...')
            with open('db/create_database.sql', 'r') as f:
                queries = f.read()
            cur = self.db.cursor()
            for query in queries.split(';'):
                cur.execute(query)

    def get_query(self, file):
        with open(file, 'r') as f:
            query = f.read()
        return query

    def get_prompt(self, cols, prompt_id):
        query = self.get_query('db/get_prompt.sql')
        query = query.format(cols=', '.join(cols), id=prompt_id)
        result = self.cursor.execute(query)
        return result.fetchone()

    def get_answers(self, cols, prompt_id):
        query = self.get_query('db/get_answers.sql')
        query = query.format(cols=', '.join(cols), prompt_id=prompt_id)
        result = self.cursor.execute(query)
        return result.fetchall()
