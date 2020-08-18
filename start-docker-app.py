import re
import os
import fileinput
from subprocess import call

f = open("/etc/newrelic-infra.yml", "r")
for line in f: 
    if (re.search("display_name", line)): 
        line_list = line.split()
        hostname = line_list[-1]
        docker_command = "docker run --name zodiac-app --hostname %s -p  0.0.0.0:5000:5000 -d --rm flask-app" % hostname
        os.system(docker_command)
