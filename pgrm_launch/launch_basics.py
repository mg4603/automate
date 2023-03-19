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

open_calc()