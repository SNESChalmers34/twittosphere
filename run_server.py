import os

from twittosphere.app import TwittosphereApp

import cherrypy

if __name__ == '__main__':
    repodir = os.path.realpath(os.path.dirname(__file__))
    staticpath = os.path.join(repodir, 'twittosphere/static')
    config = {
        '/': {
            'tools.sessions.on': True
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': staticpath
        }
    }
    # starting server
    cherrypy.quickstart(TwittosphereApp(), config=config)
