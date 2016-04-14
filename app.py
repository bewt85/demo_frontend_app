#!/usr/bin/env python

import os

from flask import Flask, request
from jinja2 import Template

app = Flask(__name__)

template = Template("""\
<h1>Hello {{ name }}</h1>
<p>Welcome to a basic demo</p>
""")

@app.route("/")
def hello():
    name = request.args.get("name", "World")
    return template.render(name=name)

if __name__ == "__main__":
    kwargs = {}
    if os.getenv("DEBUG"):
        kwargs["debug"] = True
    if os.getenv("PORT"):
        kwargs["port"] = int(os.getenv("PORT"))
    app.run(**kwargs)
