#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
target = 'list.json'
os.chdir('languages')
entries = []
for files in os.listdir('./'):
    if files.endswith('.json') and not files == target:
        f = open(files, 'r')
        langFile = json.loads(f.read())
        languageCode = f.name[:len(f.name) - 5]
        f.close()
        entry = {'nativeName': langFile['nativeName'],
                 'name': langFile['name'], 'languageCode': languageCode}
        entries.append(entry)
f = open(target, 'w')
f.write(json.dumps(entries))
