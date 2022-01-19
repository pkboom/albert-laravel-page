from albert import *
import json
import re
from os import path
from os import walk
import sys

__title__ = "Show laravel projects on chrome"
__version__ = "0.4.0"
__triggers__ = "si "
__authors__ = "pkboom"

icon = "{}/icon.png".format(path.dirname(__file__))

code = '/home/y/code'

dir = path.dirname(path.abspath(__file__))

sites = path.join(dir, 'sites.json')

file = open(sites)

projects = json.load(file)

file.close()

print(projects)

def handleQuery(query):

    if not query.isTriggered or not query.isValid:
        return

    for root, dirs, files in walk(code):
        for project in dirs:
            projects.append(project + '.test')
        break

    items = []

        
    regexp = query.string.strip().replace(" ", ".*")

    for project in projects:
        if re.search(regexp, project): 
            items.append(Item(
                id=project,
                icon=icon,
                text=project,
                actions=[ProcAction(
                    text="This action runs vscode.", 
                    commandline=['google-chrome-stable', project]
                )],
            ))

    return items
