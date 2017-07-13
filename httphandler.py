import cgi
import os
class Request(object):
    """
    HTTP class
    """
    def __int__(self, environ=os.environ):
        """

        :param environ:
        :return:
        """
        self.__form=cgi.FieldStorage()
        self.environ=environ