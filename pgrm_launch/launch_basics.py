from  shlex import split
from subprocess import Popen
from logging import debug, basicConfig, disable, DEBUG, CRITICAL
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(CRITICAL)

def open_calc():
    proc = Popen(split('/usr/bin/gnome-calculator'))
    debug(proc.poll() == None) # poll returns None if process is running
    # doesn't return till process is stopped, then returns 0
    debug(proc.wait()) 
    # returns 0 once process is stopped
    debug(proc.poll())

def run_py_script(script_loc):
    proc = Popen(['python3',*split(script_loc)])
    proc.wait()
    debug('run py script fn')

def open_with_def(file):
    proc = Popen(split('see %s' % file))
    proc.wait()
    debug(split('see %s' % file))

# open_with_def('sample.txt')
# run_py_script('sample.py')
# open_calc()