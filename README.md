# Taksman

Assignment management tool for school.

## Setup

    $ git clone git://github.com/mlsteele/taksman.git ~/.taksman

Add taksman to your `PATH`

    $ echo "export PATH=\$HOME/.taksman:\$PATH"

Install the requirements with

    $ pip install -r requirements.txt

Enable autocompletion by sourcing completion.bash or completion.zsh into your bashrc or zshrc.

    $ echo "source ~/.taksman/completion.bash" >> ~/.bashrc

    $ echo "source ~/.taksman/completion.zsh" >> ~/.zshrc

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
