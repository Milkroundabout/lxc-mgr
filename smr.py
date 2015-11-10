import lxc
import re


smr_prefix = 'con-smr-'

machines = [ 'smr', 'shed', 'candidate-signups', 'smr-domain' ]

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

containers = lxc.list_containers("test")

smr_containers = [ SMRContainer(con) for con in containers if re.match(rxp, con) ]

for c in smr_containers:
    print(c)
    

