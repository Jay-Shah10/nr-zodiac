#!/bin/bash

docker run --name zodiac-app --hostname vargrant-u18-macbook15NRJ -p 0.0.0.0:5000:5000 -d --rm zodiac-app-image
