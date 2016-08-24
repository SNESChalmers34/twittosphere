from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SimpleDatabaseConnection(object):
    def __init__(self, user, password, host, dbname):
        uri_template = 'mysql://{user}:{password}@{host}/{dbname}'
        uri = uri_template.format(user=user, password=password,
                                  host=host, dbname=dbname)
        self.engine = create_engine(uri, echo=False)
        self._create_db()
        self.Session = sessionmaker(bind=self.engine)

    def _create_db(self):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()
