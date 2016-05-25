#!/usr/bin/env python

import unittest

from todo_finder import TodoFinder

class TodoFinderTest(unittest.TestCase):
    def setUp(self):
        self.tf = TodoFinder()

    def test_no_todos_found(self):
        self.assertEqual(self.tf.find_todos("""
lorem ipsum
foobar
lorem ipsum"""), False)

    def test_find_todo_block(self):
        self.assertEqual(self.tf.find_todos("""
lorem ipsum
TODO: foobar
lorem ipsum"""), True)

    def test_find_unsure_marker(self):
        self.assertEqual(self.tf.find_todos("""
lorem ipsum
foobar (?)
lorem ipsum"""), True)

    def test_ignore_draft_todos(self):
        self.assertEqual(self.tf.find_todos("""
+++
draft = true
+++
lorem ipsum
TODO: foobar
lorem ipsum"""), False)

if __name__ == '__main__':
    unittest.main()
