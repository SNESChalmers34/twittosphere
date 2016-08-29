try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser
import os
import uuid

from twittosphere.db import SimpleDatabaseConnection
from twittosphere.views import TweetView, ProjectView
from twittosphere.models import Project

import cherrypy
from jinja2 import Environment, PackageLoader


class TwittosphereApp(object):
    def __init__(self):
        # Base Configs
        self._appdir = os.path.realpath(os.path.dirname(__file__))
        self._configs = self._get_configs()
        self._db = self._get_db_conn()
        self._env = Environment(
            loader=PackageLoader(
            'twittosphere', 'templates')
        )
        # Add class-based views here!!!
        self.tweets = TweetView(self._appdir, self._configs,
                                self._db, self._env)
        self.projects = ProjectView(self._appdir, self._configs,
                                    self._db, self._env)

    # ---------------------------------------------
    # Put your root views here.
    # ---------------------------------------------
    @cherrypy.expose
    def index(self):
        """
        Index Page displaying a summary description and
        table of all projects.

        :return: html rendering of view.
        :rtype: String
        """
        # Set a csrf token for the user
        csrf_token = cherrypy.session.get('csrf_token')
        if not csrf_token:
            csrf_token = str(uuid.uuid4())
            cherrypy.session['csrf_token'] = csrf_token
        # Get db session
        session = self._db.get_session()
        projects = session.query(Project).all()
        session.close()
        # Render template
        template = self._env.get_template('index.html')
        return template.render(projects=projects,
                               csrf_token=csrf_token)

    #----------------------------------------------
    # Private functions
    # ---------------------------------------------
    def _get_db_conn(self):
        """
        Get a database session.
        :return: Database Session.
        """
        user = self._configs.get('database', 'user')
        password = self._configs.get('database', 'password')
        host = self._configs.get('database', 'host')
        dbname = self._configs.get('database', 'database')
        conn = SimpleDatabaseConnection(user=user, password=password,
                                        host=host, dbname=dbname)
        return conn


    def _get_configs(self):
        """
        Get configuration values from config file.

        :returns: Parsed Config Values.
        :rtype: ConfigParser
        """
        parser = ConfigParser()
        cfg_file = os.path.join(self._appdir, 'config.cfg')
        parser.read(cfg_file)
        return parser
