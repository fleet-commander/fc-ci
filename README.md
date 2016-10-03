This repository hosts CI code for fleet-commander.

### High level overview
Jenkins or its alternative is configured to run `run.py` upon some trigger (like new commits or pull requests for fc-admin).

`run.py` uses [duffy](https://wiki.centos.org/QaWiki/CI/Duffy) to request 2 nodes. The first node will run a libvirt server, which is required for testing fc-admin features like `live session`. The second node will run a docker server, which will be used to run the tests.

`run.py` executes `prepare-libvirt-node.sh` on the libvirt node, and `prepare-docker-node.sh` on the docker node. These two scripts prepare both nodes into a functional state. 

Then, `prepare-docker-node.sh` executes `docker-compose up`, which will run all the services specified in `docker-compose.yml`. Typically, there will be one service per distribution or some specific "testing environment". Every docker service is configured to run some script in `distro_tests`, and these scripts should handle the testing.

After the tests, every script can (and should) report their success/fail state to `paste.fedoraproject.org`. This can be done with `sticky_notes.py`.

### writing / modifying tests
`docker-compose.yml` contains configuration for the images that will be run. Edit the relevant scripts in `distro_tests` to change the tests. Don't forget to report your status to `paste.fedoraproject.org` (you can use `sticky_notes.py` for that, or just use the API manually).

