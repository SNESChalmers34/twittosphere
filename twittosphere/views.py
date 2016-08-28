import cherrypy


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

    def create(self, csrf_token, **kwargs):
        """
        Generic view to create an object.
        """
        return NotImplementedError()

    @cherrypy.popargs('obj_id')
    def modify(self, obj_id, csrf_token, **kwargs):
        """
        Generic view to modify an object.
        """
        return NotImplementedError()

    @cherrypy.popargs('obj_id')
    def delete(self, obj_id, csrf_token):
        """
        Generic view to delete an object.
        """
        return NotImplementedError()

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
    pass


class SettingView(GenericView):
    pass