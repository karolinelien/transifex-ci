
from translayer import tx3
import os

#create an instance of a transifex organisation (pass organisation slug and transifex API token)
org = "hisp-uio"
tx_token = os.getenv("TX_TOKEN")

tx = tx3.tx(org,tx_token)

project_langs = {}

# get a list of the projects
projects = tx.projects()

for p in projects:
    if p.name[0:4] in ("ANDR", "APP-", "APP:"):
        project_langs[p.name] = set()
        # print(p.name)
        # get project languages
        langs = p.languages()
        for l in langs:
            #print(l.code)
            project_langs[p.name].add(l.id)

print(all_langs)

for p in projects:
    if p.name[0:4] in ("ANDR", "APP-", "APP:"):
        print(p.name)
        # get project languages
        if 'l:en_US' in project_langs[p.name]:
            print("language en_US exists")
            p.delete_language("l:en_US")
            

