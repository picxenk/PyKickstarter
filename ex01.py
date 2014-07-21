#!/usr/bin/env python
#coding=utf-8

from PyKickstarter import PyKickstarter
kick = PyKickstarter()

projects = []
results = kick.search_projects('microview')
for p in results.next():
    projects.append(p)

first = projects[0].data
# print first
# check the project_block.txt in docs
print first.name
print first.location['displayable_name']
print first.backers_count
print first.goal
print first.pledged

