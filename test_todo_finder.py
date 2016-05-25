#!/usr/bin/env python

import os
import unittest

from todo_finder import TodoFinder

class TodoFinderTest(unittest.TestCase):
    def setUp(self):
        self.tf = TodoFinder()

    def tearDown(self):
        try:
            os.remove('test.md')
        except(OSError):
            pass

    def write_markdown_file(self, text):
        markdown_file_name = 'test.md'
        with open(markdown_file_name, 'w') as markdown_file:
            markdown_file.write(text)
        return markdown_file_name

    def test_no_todos_found(self):
        markdown_file = self.write_markdown_file("""
lorem ipsum
foobar
lorem ipsum""")
        self.assertEqual(self.tf.find_todos(markdown_file), False)

    def test_find_todo_block(self):
        markdown_file = self.write_markdown_file("""
lorem ipsum
TODO: foobar
lorem ipsum""")
        self.assertEqual(self.tf.find_todos(markdown_file), True)

    def test_find_unsure_marker(self):
        markdown_file = self.write_markdown_file("""
lorem ipsum
foobar (?)
lorem ipsum""")
        self.assertEqual(self.tf.find_todos(markdown_file), True)

    def test_ignore_draft_todos(self):
        markdown_file = self.write_markdown_file("""
+++
draft = true
+++
lorem ipsum
TODO: foobar
lorem ipsum""")
        self.assertEqual(self.tf.find_todos(markdown_file), False)

if __name__ == '__main__':
    unittest.main()
