from __future__ import print_function
import sys
import os
import re
import subprocess
from collections import defaultdict

from flask import Flask, render_template, redirect, abort, Response
app = Flask(__name__)

import github.web
import text


basic_page_names = [
        'index',
    ]
    
# Custom Jinja globals
app.jinja_env.globals['url'] = lambda x: x
app.jinja_env.globals['datetime_generated'] = subprocess.check_output(['date', '+%Y-%m-%d %H:%M:%S %z']).strip()
app.jinja_env.globals['page_titles'] = text.page_titles
app.jinja_env.globals['top_titles'] = text.top_titles 
app.jinja_env.globals['page_titles'] = text.page_titles 
app.jinja_env.globals['short_page_titles'] = text.short_page_titles 
app.jinja_env.globals['page_leads'] = text.page_leads
app.jinja_env.globals['page_sub_leads'] = text.page_sub_leads
app.jinja_env.globals['top_navigation'] = text.top_navigation
app.jinja_env.globals['navigation'] = text.navigation
app.jinja_env.globals['navigation_reverse'] = { page:k for k,pages in text.navigation.items() for page in pages }
app.jinja_env.globals['navigation_reverse'].update({ k:k for k in text.navigation})


app.add_url_rule('/github.html', 'github_main', github.web.main)
app.add_url_rule('/milestones.html', 'github_milestones', github.web.milestones)
app.add_url_rule('/milestones-completed.html', 'github_milestones_closed', github.web.milestones_closed)

app.add_url_rule('/', 'index_redirect', lambda: redirect('index.html'))

@app.route('/<page_name>.html')
def basic_page(page_name):
    if page_name in basic_page_names:
        kwargs = {}
        parent_page_name = page_name
        return render_template(page_name+'.html', page=parent_page_name, **kwargs)
    else:
        abort(404)

# Server an image through the development server (--live)
@app.route('/<image>.png')
def image_development(image):
    return Response(open(os.path.join('out', image+'.png')).read(), mimetype='image/png')

@app.route('/<name>.csv')
def csv_development(name):
    return Response(open(os.path.join('out', name+'.csv')).read(), mimetype='text/csv')



if __name__ == '__main__':
    if '--live' in sys.argv:
        app.debug = True
        app.run()
    else:
        from flask_frozen import Freezer
        app.testing = True
        app.config['FREEZER_DESTINATION'] = 'out'
        app.config['FREEZER_REMOVE_EXTRA_FILES'] = False
        freezer = Freezer(app)
        
        @freezer.register_generator
        def url_generator():
            for page_name in basic_page_names:
                yield 'basic_page', {'page_name': page_name}
            
            

        freezer.freeze()
        
        freezer.freeze()
