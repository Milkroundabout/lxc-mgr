import lxc
import re
import sys

# this is a prefix on all the smr lxc container names
smr_prefix = 'con-smr-'

# this is the name of all the smr instances
machines = [ 'smr', 'shed', 'candidate-signups', 'smr-domain' ]

# make a regexp that matches the interesting smr lxc names
# using the prifix and the machine names
rxp = re.compile('^' + smr_prefix + "(:?" + "|".join(machines) + ')$' )


class SMRContainer:
    def __init__(self,namestr):
        self.con = lxc.Container(namestr)
        self.name = re.sub(smr_prefix,'',namestr)
        if self.con.state == 'RUNNING':
            self.running = True
            self.ips = self.con.get_ips()
        else:
            self.running = False
            self.ips = ['-']
            
        
    def __str__(self):
        return "{0.name:24} {0.con.state:16} {0.ips[0]}".format(self)

def init_containers ():
    containers = lxc.list_containers()

    smr_containers = [ SMRContainer(con)
                       for con in containers
                       if re.match(rxp, con) ]
    return smr_containers

containers = init_containers()

def parse_cmd (cmdlist):
    default_mode = 'list'
    default_target = 'all'
    if len(cmdlist) > 1 :
        mode = cmdlist[1]
    else :
        mode = default_mode
    if len(cmdlist) > 2 :
        target = cmdlist[2]
    else:
        target = default_target
    return [mode,target]
    


[mode,target] = parse_cmd(sys.argv)

def do_list_containers(containers,target):
    if target == 'ALL':
        lst = containers
    else:
        lst = [ c for c in containers if c.name == target ]
    for c in lst:
        print(c)


if mode == 'list' :
    do_list_containers(containers,target)

    

