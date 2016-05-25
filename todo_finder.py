#!/usr/bin/env python

class TodoFinder:
    DRAFT_POST_CONFIG = "draft = true"
    TODO_BLOCK_MARKER = "TODO:"
    UNSURE_MARKER     = "(?)"

    def find_todos(self, text):
        if self.DRAFT_POST_CONFIG in text:
            return False
        elif self.TODO_BLOCK_MARKER in text or self.UNSURE_MARKER in text:
            return True
        else:
            return False
