#!/usr/bin/env python3
import lxc
import re
import sys
import json
import os

# this is a prefix on all the smr lxc container names
smr_prefix = 'con-smr-'

# this is the name of all the smr instances
machines = [ 'smr', 'shed', 'candidate-signups', 'smr-domain', 'dev',
             'website', 'floorplan', 'companies', 'companies-old' ]

# make a regexp that matches the interesting smr lxc names
# using the prifix and the machine names
rxp = re.compile('^' + smr_prefix + "(:?" + "|".join(machines) + ')$' )


class SMRContainer:
    def __init__(self,namestr):
        self.con = lxc.Container(namestr)
        self.name = re.sub(smr_prefix,'',namestr)

    @property
    def ips(self):
        lst = ['-']
        if self.con.running and self.con.get_ips():
            lst = self.con.get_ips()
        return lst

    def __str__(self):
        return "{0.name:24} {0.con.state:16} {0.ips[0]}".format(self)

def init_containers ():
    containers = lxc.list_containers()

    smr_containers = [ SMRContainer(con)
                       for con in containers
                       if re.match(rxp, con) ]
    return smr_containers



def parse_cmd (cmdlist):
    default_mode = 'list'
    default_target = 'all'
    if len(cmdlist) > 1 :
        mode = cmdlist[1]
    else :
        mode = default_mode
    if len(cmdlist) > 2 :
        target = cmdlist[2:]
    else:
        target = default_target
    return [mode,target]

def filter_containers(containers,target):
    lst = containers
    if target !=  'all':
        lst = [ c for c in containers if c.name in target ]
    return lst



def do_print_cons(containers):
    for c in containers:
        print(c)

def do_start_cons(cons):
    for c in cons:
        if not c.con.running:
            c.con.start()
            c.con.attach_wait(lxc.attach_run_command,["hostname", c.name])

def do_stop_cons(cons):
    for c in cons:
        if c.con.running:
            c.con.stop()

def do_shell_cons(cons):
    for c in cons:
        c.con.attach_wait(lxc.attach_run_command, ["bash", "-l"])

# program starts

[mode,target] = parse_cmd(sys.argv)
containers = filter_containers(init_containers(),target)

if mode == 'list' :
    do_print_cons(containers)

if mode == 'start' :
    do_start_cons(containers)

if mode == 'stop' :
    do_stop_cons(containers)


if mode == 'shell' :
    do_shell_cons(containers)
