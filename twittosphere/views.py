class GenericView(object):
    def __init__(self, appdir, configs, db, env):
        self._appdir = appdir
        self._configs = configs
        self._db = db
        self._env = env


class Tweet(GenericView):
    pass


class Project(GenericView):
    pass


class Setting(GenericView):
    pass