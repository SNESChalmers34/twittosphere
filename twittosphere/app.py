try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser
import os

from twittosphere.db import SimpleDatabaseConnection

import cherrypy


class TwittosphereApp(object):
    def __init__(self):
        self.appdir = os.path.realpath(os.path.dirname(__file__))
        self.configs = self._get_configs()
        self.db = self._get_db_conn()

    # ---------------------------------------------
    # Put your views here.
    # i.e. Everything exposed to the outside world.
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
        user = self.configs.get('database', 'user')
        password = self.configs.get('database', 'password')
        host = self.configs.get('database', 'host')
        dbname = self.configs.get('database', 'database')
        conn = SimpleDatabaseConnection(user=user, password=password,
                                        host=host, dbname=dbname)
        return conn.get_session()


    def _get_configs(self):
        """
        Get configuration values from config file.

        :returns: Parsed Config Values.
        :rtype: ConfigParser
        """
        parser = ConfigParser()
        cfg_file = os.path.join(self.appdir, 'config.cfg')
        parser.read(cfg_file)
        return parser