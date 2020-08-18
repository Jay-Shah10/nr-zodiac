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
   
