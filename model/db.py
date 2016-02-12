from flask_sqlalchemy import SQLAlchemy


class Db(object):

    def __init__(self, app):
        self.initialize(app)

    def initialize(self, app):
        self.db = SQLAlchemy(app)
        return self.get_db()

    def get_db(self):
        return self.db
