# fantasy-object-name-gen
Makes use of containerised microprograms to generate a random object name. Both the type and source of the object is random, but is based on classic fantasy tropes. 




Deployment:
Jenkins pulls code from github
Jenkins runs tests on code. 
Assuming good test results, Jenkins installs ansible.
If we want to get real fancy...
Ansible spins up docker swarm deployment VMs, installs docker and docker-compose, installs requirements for the app
Installs Nginx. Sets up nginx service file from repo, sets up systemd service file from repo. 
Commands app to run
Nginx displays app to user
