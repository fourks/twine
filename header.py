#!/usr/bin/python

import os, imp
from collections import OrderedDict

class Header (object):

    def __init__(self, id, path):
        self.id = id.lower()
        self.path = path
        self.label = id.capitalize()

    def files_to_embed(self):
        """Returns an Ordered Dictionary of file names to embed into the output.
        
        The item key is the label to look for within the output. 
        The item value is the name of the file who's contents will be embedded into the output.
        
        NOTE: Currently assumes the files are within self.path
        """
        return OrderedDict()

    def is_endtag(self, name, tag):
        """Return true if the name is equal to an endtag."""
        return (name == ('end' + tag))

    def nested_macros(self):
        """Returns a list of macro names that support nesting."""
        return ['if', 'silently', 'nobr']
    
    @staticmethod
    def factory(type, path):
        header_def = path + type + '.py'
        if os.access(header_def, os.R_OK):
            py_mod = imp.load_source(type, header_def)
            obj = py_mod.Header(type, path)
        else:
            obj = Header(type, path)
        return obj
