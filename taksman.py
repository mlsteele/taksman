#!/usr/bin/env python
""" Assignment management tool for school.
Usage:
  taksman.py (-h | --help)
  taksman.py add <entry>
  taksman.py done <entry>
  taksman.py course
  taksman.py date
  taksman.py debug

Examples:
  taksman.py add 033-reading   create a new task entry
  taksman.py done <entry>      mark an entry as done

Options:
  -h, --help
"""

import sys
import os
import errno
import subprocess
import re
from pprint import pprint
from docopt import docopt

def show_by_course(tasks):
    courses = set(tasks[name].get('course') for name in tasks)
    # Note: None can be in this set
    # courses -= set([None])
    courses = sorted(courses)

    for course in courses:
        print
        print "Course: %s" % course
        course_tasks = filter(
            lambda name: tasks[name].get('course') == course,
            tasks)
        for name in course_tasks:
            print "> %s" % name

def read_tasks(db_root):
    """ Load tasks from db. """
    entry_names = os.listdir(os.path.join(db_root, "entry"))
    entry_paths = {filename: os.path.join(db_root, "entry", filename) for filename in entry_names}
    tasks = {name: read_task(entry_paths[name]) for name in entry_names}
    return tasks

def read_task(filepath):
    """ Read a task from a file. """
    task = {}
    task['body'] = ""

    with open(filepath, 'r') as f:
        reading_headers = True
        for line in f.readlines():
            header_match = re.match(r"(?P<field>\w+): +(?P<value>.*)$", line)
            if reading_headers and header_match:
                field = header_match.group('field')
                value = header_match.group('value')
                assert field != 'body'
                assert field not in task
                task[field] = value.rstrip()
            else:
                reading_headers = False
                task['body'] += line.rstrip() + "\n"

    task['body'] = task['body'].rstrip()

    return task

def ensure_db(db_root):
    """ Make the storage directories exist. """
    mkdir_p(os.path.join(db_root, "entry"))
    mkdir_p(os.path.join(db_root, "done"))
    mkdir_p(os.path.join(db_root, "template"))

def mkdir_p(path):
    """ no error if existing, make parent directories as needed """
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def edit_file(filepath):
    editor = os.environ.get('EDITOR', 'nano')
    subprocess.call([editor, filepath])

if __name__ == "__main__":
    db_root = "tasks"
    ensure_db(db_root)
    tasks = read_tasks(db_root)

    arguments = docopt(__doc__)
    if arguments['debug']:
        pprint(tasks)
    elif arguments['add']:
        name = arguments['<entry>']
        if name in tasks:
            print "%s already in tasks" % name
            sys.exit(-1)
        filepath = os.path.join(db_root, 'entry', name)
        edit_file(filepath)
        print "%s saved to %s" % (name, filepath)
    elif arguments['done']:
        name = arguments['<entry>']
        if name not in tasks:
            print "%s not in tasks" % name
            sys.exit(-1)
        filepath = os.path.join(db_root, 'entry', name)
        newpath = os.path.join(db_root, 'done', name)
        os.rename(filepath, newpath)
        print "%s archived to %s" % (name, newpath)
    elif arguments['course']:
        show_by_course(tasks)
    elif arguments['date']:
        raise Exception("not implemented")
    else:
        print "Whoops, unhandled input."
