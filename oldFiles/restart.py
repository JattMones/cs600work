import os, sys, re
import subprocess32 as subprocess
import time

time.sleep(5)
fileRef = sys.argv[0]
path = os.path.abspath(os.path.dirname(fileRef))
subprocess.call(['python3', 'assistiveDraft.py'])
