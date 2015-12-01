# container manager

Running multiple services and web applications in
[lxc-containers](https://linuxcontainers.org/lxc/introduction/) on linux for
development. These are scripts and tools to make running and
restarting many such environments slightly more convenient

the tool is a mixture of lxc api calls and wappers around the lxc-* shell commands

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
