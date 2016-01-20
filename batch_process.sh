#!/bin/bash

python ${CHILI_HOME}/chili_time.py

cd ${GITHUB_IO_HOME}
git add projects/chilitime/*
git commit -m 'Auto-committing chilitime.ics file'
git push https://github.com/bdetweiler/bdetweiler.github.io.git
