## Startup
#### Start local test server for API
~~~
$env:FLASK_APP="app"
flask run
~~~
## Virtual Environment
#### Startup virtual environment 
``` .\.venv\Scripts\activate.ps1```

#### Install Requirements
```pip install -r requirements.txt```

#### End Session
```deactivate```

## Pytest
#### Run Pytest (as a script)
This command runs pytest as a script, which treats this python project as a package and allows it to use absolute imports (*from <span>app.services.xxx</span> import xxx*)
```python -m pytest```