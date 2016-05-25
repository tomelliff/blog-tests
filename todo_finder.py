#!/usr/bin/env python

class TodoFinder:
    def find_todos(self, text):
        if "TODO:" in text:
            return True
        else:
            return False
