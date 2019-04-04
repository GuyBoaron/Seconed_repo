from subprocess import Popen, PIPE

sudo_password = 'ncjwwr400'
command = 'sudo apt-get install python3-tk'.split()

p = Popen(['sudo', '-S'] + command, stdin=PIPE, stderr=PIPE, universal_newlines=True)
sudo_prompt = p.communicate(sudo_password + '\n')[1]
