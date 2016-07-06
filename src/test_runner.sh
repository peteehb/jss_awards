#!/bin/bash

coverage run --source='.' test_suite.py
coverage report
coverage html
x-www-browser "file://$(pwd)/htmlcov/index.html" &
