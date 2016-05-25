#!/usr/bin/env python

class TodoFinder:
    DRAFT_POST_CONFIG = "draft = true"
    TODO_BLOCK_MARKER = "TODO:"
    UNSURE_MARKER     = "(?)"

    def _find_todos_in_text(self, text):
        if self.DRAFT_POST_CONFIG in text:
            return False
        elif self.TODO_BLOCK_MARKER in text or self.UNSURE_MARKER in text:
            return True
        else:
            return False

    def find_todos(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            return self._find_todos_in_text(text)
