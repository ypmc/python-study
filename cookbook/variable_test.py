class Article:
    def __init__(self, id, title, var='__private_in_class'):
        self._id = id
        self._title = title
        self.__private_in_class = var

    def __repr__(self):
        return repr(self.__dict__)

    def get(self):
        pass


_private_in_module = '_private_in_module'
COMMON_VAR = 'common_var'
