__author__ = 'rylan'

import importlib
import os
import rsa

# for file in current directory
for file in os.listdir(os.getcwd()):

    if file.endswith('Submission.py'):

        # import the student submission
        submission = importlib.import_module(file[:-3])

        # print results of executing student's main()
        if rsa.verify(*submission.main()):
            print file[:-16] + ': PASS'
        else:
            print file[:-16] + ': FAIL'

