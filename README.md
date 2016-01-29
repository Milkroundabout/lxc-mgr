# container manager

Running multiple services and web applications in
[lxc-containers](https://linuxcontainers.org/lxc/introduction/) on linux for
development. These are scripts and tools to make running and
restarting many such environments slightly more convenient

the tool is a mixture of lxc api calls and wappers around the lxc-* shell commands

it has a simple verb noun syntax

    smr <verb> <noun>

where verb is one of a set of known commands list, start, stop, shell
and noun corresponds to a container short name

if no verb is supplied, the default is assumed (list)
if no noun is supplied, the verb is applied to all of the known nouns

e.g.
- `smr` -> list all containers
- `smr start` -> ask all containers to start
- `smr stop foo` -> ask container foo to stop


## example usage

listing all known smr containers

    # smr
    candidate-signups        RUNNING          172.20.0.189
    dev                      RUNNING          172.20.0.83
    shed                     RUNNING          172.20.0.169
    smr                      RUNNING          172.20.0.198
    smr-domain               RUNNING          172.20.0.131
    website                  RUNNING          172.20.0.170

stop the 'dev' container

    # smr stop dev

listing the containers shows dev as stopped
    
    # smr
    candidate-signups        RUNNING          172.20.0.189
    dev                      STOPPED          -
    shed                     RUNNING          172.20.0.169
    smr                      RUNNING          172.20.0.198
    smr-domain               RUNNING          172.20.0.131
    website                  RUNNING          172.20.0.170

start the dev container

    # smr start dev

listing the containers shows dev as started again

    # smr
    candidate-signups        RUNNING          172.20.0.189
    dev                      RUNNING          172.20.0.83
    shed                     RUNNING          172.20.0.169
    smr                      RUNNING          172.20.0.198
    smr-domain               RUNNING          172.20.0.131
    website                  RUNNING          172.20.0.170

bring up a shell on the dev container
    
    # smr shell dev
    user@dev $>

start all containers

    # smr start

stop all containers

    # smr stop


there is a provisional ansible playbook for cloning a new machine

use it like this

ansible-playbook -K -i ansible/hosts ansible/playbooks/lxc-clone.yml -e 'con_name=newname'
