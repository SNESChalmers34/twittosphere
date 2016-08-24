from twittosphere.app import TwittosphereApp

import cherrypy

if __name__ == '__main__':
   cherrypy.quickstart(TwittosphereApp(), '/')