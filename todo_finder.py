#!/usr/bin/env python

class TodoFinder:
    def find_todos(self, text):
        if "draft = true" in text:
            return False
        elif "TODO:" in text or "(?)" in text:
            return True
        else:
            return False
