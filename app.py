from flask import Flask, render_template, url_for, json
import os,pdb
from testing import testingresult

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sitelogic')
def sitelogic():
    return render_template('sitelogic.html')

@app.route('/<category>')
def infopage(category):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "res.json")
    data = json.load(open(json_url))
    env = data[category.title()]
    companies = list(env.keys())
    return render_template('infopage.html',env=env,companies=companies,category=category.title())

@app.route('/<category>/<articleid>')
def infopagearticle(category,articleid):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "res.json")
    data = json.load(open(json_url))
    env = data[category.title()]
    companies = list(env.keys())
    terms = testingresult['Terms']
    term_set_split = [i.split('::') for i in terms.split('|:|')]
    unpack_terms = {s[0]:s[1] for s in term_set_split}
    return render_template('infopagearticle.html',env=env,companies=companies,category=category.title(),articleresults=testingresult,terms=unpack_terms)

    
if __name__ == '__main__':
  app.run(debug=True)
