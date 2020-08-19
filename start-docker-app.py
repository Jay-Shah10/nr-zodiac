import re
import subprocess
import fileinput

f = open("/etc/newrelic-infra.yml", "r")
for line in f: 
    if (re.search("display_name", line)): 
        line_list = line.split()
        hostname = line_list[-1]
        subprocess.call([ "docker","run", "--name", "zodiac-app", "--hostname",hostname,"-p","0.0.0.0:5000:5000", "-d", "--rm", "flask-app"])
