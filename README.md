# nr-zodiac
Demo Flask app.

### Requirments: 
```
python3
venv
Flask
```

### How to
Create a virtual env. To do this let us create a folder that will house your env. 
```
~ mkdir python/flaskapp && cd python/flaskapp
python3 -m venv venv
```
The second command is going to create a python3 virtul env in your current dir. 


You will now activate this env. 
```
source /venv/bin/activate

verification is: (venv)python/flaskapp: 
you should see something like this.
```

Install Flask
```
pip install Flask
```

Now you have your env running and you are now ready to code. To deactivate the env. 
```
deactivate
```

## Run with Docker
After you have it developed using the above "How to", you can then write the Dockerfile.
Review the Dockerfile to see what is needed and you can use start-docker-app.py to run the image as a container.  
Using the steps found in hub.docker.com for python image - create your own Dockerfile and run it. 

Once the Dockerfile is created. 
```
docker build -t <name of image>
docker run -it --rm --name <name of container> <name of image>
```

You will need to follow steps for New Relic monitoring with python agent to generate the newrelic.ini file. 
```
newrelic-admin generate-config YOUR_LICENSE_KEY newrelic.ini
```

[New Relic Python Agent](https://docs.newrelic.com/docs/agents/python-agent/installation/standard-python-agent-install)   
[Docker hub python](https://hub.docker.com/_/python)
