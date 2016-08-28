import os

from twittosphere.app import TwittosphereApp

import cherrypy

if __name__ == '__main__':
    cfgdir = os.path.realpath(os.path.dirname(__file__))
    cfgpath = os.path.join(cfgdir, 'server.cfg')
    cherrypy.quickstart(TwittosphereApp(), '/', cfgpath)