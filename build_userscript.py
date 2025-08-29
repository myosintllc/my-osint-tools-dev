#!/usr/bin/env python
# coding: utf-8

# In[115]:


import requests
from bs4 import BeautifulSoup
import json

VERSION = "1.3"

HEADER = f"""
// ==UserScript==
// @name         My OSINT Training
// @namespace    http://tampermonkey.net/
// @version      {VERSION}
// @description  Tamper before bookmarklets
// @match        *://*/*
// @grant        GM_registerMenuCommand
// @grant        GM_openInTab
// ==/UserScript==
"""

FOOTER = """
const currentDomain = window.location.hostname.replace(/^www\./, '');

if (window.top === window.self) {
    bookmarkletsJSON.forEach(item => {
        if (currentDomain.includes(item.domain) || item.domain === '*') {
            console.log(`Initializing worker: ${item.title}`);
            GM_registerMenuCommand(item.title, item.js);
        }
    })
}
"""

def generate_js_bookmarklets(data):
    lines = ["const bookmarkletsJSON = ["]
    for entry in data:
        title = entry["title"]
        js_func = entry["name"]
        domain = entry["domain"]

        lines.append("  {")
        lines.append(f'    title: "{title}",')
        lines.append(f'    js: {js_func},')  # uden citationstegn
        lines.append(f'    domain: "{domain}",')
        lines.append("  },")
    lines.append("];")
    return "\n".join(lines)

def get_bookmarklets_from_github():
    url = "https://raw.githubusercontent.com/janhalendk/my-osint-tools-dev/refs/heads/main/index.html"
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html)
    bookmarklets = soup.select("tr a[data-name]")
    print(f"{len(bookmarklets)} bookmarklets retrieved from Github")
    keys = {
        "domain": "data-domain",
        "name": "data-name",
        "replace": "data-replace-open"
    }
    bookmarklet_definitions = []
    for bml_tag in bookmarklets:
        bml = {}
        for k,v in keys.items():
            try:
                tag_value = bml_tag.get(v)
                tag_value = json.loads(tag_value)
            except:
                pass
            bml[k] = tag_value
        bml["js"] = bml_tag.get("href")
        bml["title"] = bml_tag.get_text().strip()
        bookmarklet_definitions.append(bml)
    return bookmarklet_definitions

def build_js_definitions(bookmarklet_definitions):
    js_definitions = []
    for bml in bookmarklet_definitions:
        js = bml["js"].replace("javascript:","")
        js_definition = f"const {bml['name']} = {js}"
        if js_definition.endswith(";"):
            js_definition = js_definition[:-1]
        if js_definition.endswith("()"):
            js_definition = js_definition[:-2]
        js_definition += ";"

        if bml.get("replace"):
            js_definition = js_definition.replace("window.open", "GM_openInTab")
        js_definitions.append(js_definition)
    js_def_str = "\n\n".join(js_definitions)
    return js_def_str

def build_userscript():
    bookmarklet_definitions_str = get_bookmarklets_from_github()
    bookmark_list_str = generate_js_bookmarklets(bookmarklet_definitions)
    javascript_definitions_str = build_js_definitions(bookmarklet_definitions)
    user_script_elements = [HEADER.strip(), javascript_definitions_str.strip(), bookmark_list_str.strip(), FOOTER.strip()]
    user_script = "\n\n".join(user_script_elements)
    return user_script

user_script = build_userscript()
print(user_script)


# In[ ]:





# In[ ]:




