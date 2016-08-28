try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser
import os

from twittosphere.db import SimpleDatabaseConnection
from twittosphere.views import Tweet

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
        self.tweets = Tweet(self._appdir, self._configs,
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
        return "Hello World"

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
