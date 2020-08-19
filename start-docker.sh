#!/bin/bash

docker run --name zodiac-app --hostname pi-ub1804 -p 0.0.0.0:5000:5000 -d --rm flask-app
