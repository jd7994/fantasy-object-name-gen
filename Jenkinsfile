pipeline {
    agent any
    stages {
        stage('Setup & Install Ansible') {
            steps {
                sh '''#!/bin/bash
                    sudo apt update
                    sudo apt autoremove
                    sudo mkdir -p ~/.local/bin
                    sudo echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
                    source ~/.bashrc
                    sudo apt install python3
                    sudo apt install python3-pip -y
                    sudo apt install python3-venv -y
                    sudo pip3 install --user ansible
                    ansible --version'''
            }
        }        
        
        stage('Get Code for Testing') {
            steps {
                git branch: 'dev', changelog: false, poll: false, url: 'https://github.com/jd7994/fantasy-object-name-gen.git'
            }
        }
      
        stage('Testing Service 1') {
            steps {
                sh '''#!/bin/bash
                    sudo rm -rf venv
                    python3 -m venv venv
                    source venv/bin/activate
                    cd /home/jenkins/.jenkins/workspace/fan_gen/service_1
                    pip3 install -r requirements.txt
                    cd ..
                    python3 -m pytest service_1 --cov=application --cov-report=html
                    mv htmlcov/ serv_1_results/'''
                archiveArtifacts artifacts: 'serv_1_results/'
            }
        }

        stage('Testing Service 2') {
            steps {
                sh '''#!/bin/bash
                    sudo rm -rf venv
                    python3 -m venv venv
                    source venv/bin/activate
                    cd /home/jenkins/.jenkins/workspace/fan_gen/service_2
                    pip3 install -r requirements.txt
                    cd ..
                    python3 -m pytest service_2 --cov=application --cov-report=html
                    mv htmlcov/ serv_2_results/'''
                archiveArtifacts artifacts: 'serv_2_results/'
            }
        }

        stage('Testing Service 3') {
            steps {
                sh '''#!/bin/bash
                    sudo rm -rf venv
                    python3 -m venv venv
                    source venv/bin/activate
                    cd /home/jenkins/.jenkins/workspace/fan_gen/service_3
                    pip3 install -r requirements.txt
                    cd ..
                    python3 -m pytest service_3 --cov=application --cov-report=html
                    mv htmlcov/ serv_3_results/'''
                archiveArtifacts artifacts: 'serv_3_results/'
            }
        }

        stage('Testing Service 4') {
            steps {
                sh '''#!/bin/bash
                    sudo rm -rf venv
                    python3 -m venv venv
                    source venv/bin/activate
                    cd /home/jenkins/.jenkins/workspace/fan_gen/service_4
                    pip3 install -r requirements.txt
                    cd ..
                    python3 -m pytest service_4 --cov=application --cov-report=html
                    mv htmlcov/ serv_4_results/
                    sudo rm -rf venv'''
                archiveArtifacts artifacts: 'serv_4_results/'
            }
        }

        stage('Emptying Jenkins VM') {
            steps {
                sh '''#!/bin/bash
                    sudo rm -rf *'''
            }
        }

        stage('Instigate Docker') {
            steps {
                sh '''#!/bin/bash
                    cd ansible_playbooks
                    ansible-playbook -i inventory.yaml install_docker.yaml
                    cd . '''
            }
        }

        stage('Get Code from Repo') {
            steps {
                sh '''#!/bin/bash
                    cd ansible_playbooks
                    ansible-playbook -i inventory.yaml git_clone.yaml
                    cd .. '''
            }
        }

        stage('Create service containers using Docker-Compose, and clear unused images') {
            steps {
                sh '''#!/bin/bash
                    cd ansible_playbooks
                    ansible-playbook -i inventory.yaml run_docker_compose.yaml
                    cd .. 
                    echo "App running!"'''
            }
        }
       
    }
}