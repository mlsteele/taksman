# Taksman

Assignment management tool for school.

## Setup

Install the requirements with

    $ pip install -r requirements.txt

Enable autocompletion by copying completion.bash or completion.zsh into your bashrc or zshrc.

This requires that you add taksman to your PATH (so you call `taksman` and not `./taksman`)

# Notes
```
directories:
entry - store entry files
done - archive done tasks
template - store task templates

script options:
all - list all entries
date - list by day
course - list by course
priority - list by priority
info - show details for task

supported fields in task files:
due - the due date
course - the course/project to which the task belongs
priority - will color the task name red/blue/cyan/white for values 0/1/2/3
```
