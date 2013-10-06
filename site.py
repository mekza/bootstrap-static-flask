#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
site.py

It's crappy but it works.
"""
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/favicon.ico')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/')
def home():
  """
  Render the home template
  """
  return render_template("home.html")

@app.route('/<name>')
def site(name):
  """
  Render any template from templates directory
  """
  template_name = "%s.html" % name

  return render_template(template_name)

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080,debug=True)