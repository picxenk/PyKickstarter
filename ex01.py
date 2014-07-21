#!/usr/bin/env python
#coding=utf-8

from PyKickstarter import PyKickstarter
kick = PyKickstarter()

# search project by keyword
projects = []
results = kick.search_projects('microview')
for p in results.next():
    projects.append(p)

# get the first project data from results
first = projects[0].data

# print attributes in project
# check the project_block.txt in docs
# print first
print first.name
print first.location['displayable_name']
print first.backers_count
print first.goal
print first.pledged

