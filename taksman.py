#!/usr/bin/env python
import os
import errno
import re
from pprint import pprint

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

if __name__ == "__main__":
    db_root = "tasks"
    ensure_db(db_root)
    tasks = read_tasks(db_root)
    pprint(tasks)
