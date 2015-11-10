import lxc
import re

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


smr_containers = [ SMRContainer(con) for con in containers if re.match(rxp, con) ]

for c in smr_containers:
    print(c)
    

