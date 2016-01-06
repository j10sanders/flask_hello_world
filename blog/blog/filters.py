from blog import app
from flask import Markup
import mistune as md
from urllib.parse import urljoin

@app.template_filter()
def markdown(text):
    return Markup(md.markdown(text,escape=True))

@app.template_filter()
def dateformat(date, format):
    if not date:
        return None
    return date.strftime(format)
    
@app.template_filter()
def pagesize(url, limit):
    return urljoin(url, '?limit=' + str(limit))