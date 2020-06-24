# create_flask

This is a Python script that creates a Flask boilerplate directory and file structure in the user's current working directory. Since it uses bash commands to carry out certain steps, it's only designed for a UNIX-based OS.

Execute the following script the same as any standard Python script with the desired file name as the required first argument. Include 'bootstrap' as the second argument if you want that CDN for Bootstrap 4 included in the 'layout.html' file.

`python3 create_flask.py project_name bootstrap`

The following directory/file structure is then created in your current working directory:

```
project_name
    |--app.py
    |--templates
    |    |--layout.html
    |    |--main.html
    |--static
    |    |--styles.css
    |    |--main.js
    |--env/ (standard Python virtual environment directory)
    |--requirements.txt
```

The 'layout.html' and 'main.html' documents both contain boilerplate code including jinja blocks for 'content' and 'scripts'.
