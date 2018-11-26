import subprocess as subprocess
launch = subprocess.call('cd ~', shell = True)
launch2 = subprocess.call('~/.local/bin/autokey-gtk', shell = True)
launch2.wait()
