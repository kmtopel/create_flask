import argparse
import subprocess
import venv

parser = argparse.ArgumentParser()
parser.add_argument('project', help='Name of Project', type=str)
parser.add_argument('--bootstrap', help='Add bootstrap lib', action='store_true')
args = parser.parse_args()
project_name = args.project

project_path = './'+project_name

print('Creating project folder...')
subprocess.run(['mkdir',project_name])
print('Creating Templates folder...')
subprocess.run(['mkdir',project_path+'/templates'])
print('Creating Static folder...')
subprocess.run(['mkdir',project_path+'/static'])

print('Creating main application .py file...')
with open(project_path+'/app.py','w+') as app:
    app_code = "from flask import Flask, render_template, url_for \napp = Flask(__name__) \n\n@app.route('/')\ndef main():\n    return render_template('main.html')"
    app.write(app_code)

print('Creating layout file for templates...')
with open(project_path+'/templates/layout.html','w+') as layout:
    html_boilerplate = '''<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta charset="UTF-8">
    <title></title>
  </head>
  <body>
    {% block content %}
    {% endblock content %}
    {% block scripts %}
    {% endblock scripts %}
  </body>
</html>'''
    html_boilerplate_w_bootstrap = '''<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" src= "{{ url_for('static', filename='style.css')}}"
    <title></title>
  </head>
  <body>
    {% block content %}
    {% endblock content %}
    {% block scripts %}
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script src="{{ url_for('static', filename='scripts.js') }}"
    {% endblock scripts %}
  </body>
</html>'''
    print('Writing boilerplate code for layout file...')
    if args.bootstrap==True:
        layout.write(html_boilerplate_w_bootstrap)
    else:
        layout.write(html_boilerplate)

print('Creating main HTML page for app...')
with open(project_path+'/templates/main.html','w+') as main:
    main_html_boilerplate = "{% extends 'layout.html' %}\n{% block content %}\n\n<h1>If you're seeing this, the setup worked!</h1>\n\n{% endblock content%}"
    main.write(main_html_boilerplate)

print('Creating empty CSS file...')
with open(project_path+'/static/style.css','w+'):
    pass

print('Creating empty JavaScript file...')
with open(project_path+'/static/scripts.js','w+'):
    pass

print('Creating virtual environment...')
subprocess.run(['python3','-m','venv',project_path+'/env'])
print('Creating Requirements.txt file...')
subprocess.run([project_path+'/env/bin/pip3','install','pipreqs'])
subprocess.run([project_path+'/env/bin/pipreqs',project_path])
print('Installing package dependencies...')
subprocess.run([project_path+'/env/bin/pip3','install','-r',project_path+'/requirements.txt'])
print('Complete!')
