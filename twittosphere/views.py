import cherrypy

from twittosphere.models import Project


class GenericView(object):
    """
    Generic class representing a View with methods to be
    overridden.
    """
    def __init__(self, appdir, configs, db, env):
        self._appdir = appdir
        self._configs = configs
        self._db = db
        self._env = env


    def _list_view(self):
        """
        View to represent all instances of an object type.
        """
        return NotImplementedError()

    def _detail_view(self, obj_id):
        """
        Detail view of a single object.
        """
        return NotImplementedError()

    def _check_csrf(self, csrf_token):
        if str(cherrypy.session.get('csrf_token')) != csrf_token:
            msg = 'CSRF Token Invalid'
            raise cherrypy.HTTPError(status=400, message=msg)



@cherrypy.popargs('tweet_id')
class TweetView(GenericView):
    """
    Views for Tweets.

    Use as a pattern for other view types. Basic idea is that the
    web request for /tweets returns a list view.

    If the request matches /tweets/<tweet_id>,
    a view for a detailed description of that tweet
    is returned.
    """
    @cherrypy.expose
    def index(self, tweet_id=None):
        if tweet_id:
            self._detail_view(tweet_id)
        self._list_view()

    def _list_view(self):
        pass

    def _detail_view(self, tweet_id):
        pass


@cherrypy.popargs('project_id')
class ProjectView(GenericView):

    @cherrypy.expose
    def create(self, csrf_token, name, description):
        self._check_csrf(csrf_token)
        session = self._db.get_session()
        project = Project(name=name, description=description)
        session.add(project)
        session.commit()
        return "Success"


class SettingView(GenericView):
    pass