from os import path
from os import walk
import sys
from albert import *
import json

__title__ = "Show laravel projects on chrome"
__version__ = "0.4.0"
__triggers__ = "si "
__authors__ = "pkboom"

icon = "{}/icon.png".format(path.dirname(__file__))

code = '/home/y/code'

results = []
projects = []

for root, dirs, files in walk(code):
    results.extend(dirs)
    break

for project in results:
    projects.append(project + '.test')

dir = path.dirname(path.abspath(__file__))
sites = path.join(dir, 'sites.json')

file = open(sites)
projects.extend(json.load(file))
file.close()

def handleQuery(query):
    items = []

    if query.isTriggered:
        if not query.isValid:
            return

        for project in projects:
            if query.string.strip() in project: 
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
