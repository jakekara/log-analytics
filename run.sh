#!/bin/bash

# remove old file
rm -f merged.csv

# create csv from all logs in accesslogs directory
python analyzeall.py accesslogs/*

# create sqlitedb and run a simple query
sqlite3 < todb.sql
