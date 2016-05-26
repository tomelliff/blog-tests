#!/usr/bin/env python

import argparse
import os

from todo_finder import TodoFinder

parser = argparse.ArgumentParser(description='Runs a series of tests on a Hugo blog')
parser.add_argument('blog_directory', help='Path to the root of a Hugo blog')

args = parser.parse_args()
blog_directory = args.blog_directory
post_directory = blog_directory + 'content/post/'

for file in os.listdir(post_directory):
    if file.split('.')[-1] == "md":
        foundTodos = TodoFinder().find_todos(post_directory + file)
        if foundTodos:
            print('Found todos in {0}'.format(file))
