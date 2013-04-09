#!/usr/bin/env python


class HelloWorld(object):
    """ Hello World in Python using classes. """

    def __init__(self):
        self.message = 'Hello World!'

    def __str__(self):
        return self.message
