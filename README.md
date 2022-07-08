# fantasy-object-name-gen
## Makes use of containerised microprograms to generate a random object name. Both the type and source of the object is random, but is based on classic fantasy tropes. 

> "Logic will get you from A to B. Imagination will take you everywhere."
>  _-Albert Einstein_


## Index:

-[User Stories](#user-stories)

-[Acceptance Criteria](#acceptance-criteria)

-[Initial Planning](#initial-planning)

-[Design](#design)

-[Definition of Done](#def-of-done)

-[Risk Assessment](#risk-assessment)

-[Implementation and Adaption](#implementation-and-adaptation)

-[Unit Testing](#unit-testing)

-[System Integration, Development, and Build](#system-integration-deployment-and-build)

-[Reflection](#reflection)

-[Final Thoughts](#final_thoughts)


Deployment:
Jenkins pulls code from github
Jenkins runs tests on code. 
Assuming good test results, Jenkins installs ansible.
If we want to get real fancy...
Ansible spins up docker swarm deployment VMs, installs docker and docker-compose, installs requirements for the app
Installs Nginx. Sets up nginx service file from repo, sets up systemd service file from repo. 
Commands app to run
Nginx displays app to user





-----
## User Story
<details>
<summary>Click to show user story</summary>
  
  
1. As someone who has an internet connection, \ I want a random fantasy style object,\ For inspiration, to add to a story, or just for fun.


</details>

## Acceptance Criteria
<details>
<summary>From these stories, we can construct acceptance criteria:</summary>
  
1. Given a user has access to the web app, when they go to the address, then they generate a random fantasy-style object  
   
</details>

## Initial Planning

We can now construct a plan for functionality of the project. It's clear that the emphasis of the project is on the deployment rather than the app itself, so we'll keep it as simple as possible and focus on deployment techniques. The various services of the app will be developed using python and the Flask micro-framework, then run within docker micro-containers. These containers will communicate with each other using HTML requests, and the final result will be displayed to the user via an nginx backwards proxy. My intention is the deploy the app via docker swarm, allowing multiple VMs to load balance, and allow for easy and seamless updates or changes to the app.   
Progress throughout the project will be tracked using the Jira Board, made for agile development. Different epics have been created based on different phases of the development, extrapolated from the above Use Cases and broken into tasks to facilitate the design of a project like this. The completed board is here: https://jderbyshire.atlassian.net/jira/software/projects/FNG/boards/3/roadmap?selectedIssue=FNG-11&shared=&atlOrigin=eyJpIjoiMjVhODFiOTg5OTg4NDdmNDk4N2UxMzA1M2NkMmIyNTUiLCJwIjoiaiJ9

![on_schedule](https://user-images.githubusercontent.com/100293943/177530442-2726d71c-8d3c-4b4b-b3a3-ca867c0748fd.jpg)

## Design
I created models for the various services of the project, and then a plan for the ultimate deployment of the app. I intend to put a webhook in place, allowing for automatic updates by jenkins, which will instigate ansible, allowing us to automate the installation of any requirements, as well as run the project automatically on the swarm-master VM.  

![Project service layout_1](https://user-images.githubusercontent.com/100293943/177530969-2873a3da-adc8-49d8-9cf0-05b674c403fd.jpg)

The brief called for a second iteration of the project, the concept for which is below:
![Second iteration concept_1](https://user-images.githubusercontent.com/100293943/177531007-ea14fa0b-85aa-4f9a-9e33-301d1169ada8.jpg)

And finally, a general overview of the project layout:
![Project layout_1](https://user-images.githubusercontent.com/100293943/177531259-cc8e8f5d-33b7-4d8d-b763-d58fbb5e2e7f.jpg)


_____YOU GOT TO HERE, JON _______<<<<<<<<<<<<<


## Definition of Done
- Testing must be written and passed with 100% coverage
- Features must meet or excell acceptance criteria

## Risk Assessment
With a small project like this handling non-sensitive data, the risks are not particularly severe, but a risk assessment has been carried out, the results of which are below.

![Risk assessment_1](https://user-images.githubusercontent.com/100293943/177957057-1e44ba0c-f33c-46a3-8eaa-92c1ff7376dd.jpg)


## Implementation and Adaption
![serv-1-examp](https://user-images.githubusercontent.com/100293943/177959078-e0cd7654-73e9-4a6f-89df-83f18851a09d.jpg)

The app makes a lot of use of the "random" module, particularly "choice", allowing me to use a hard coded list of options that the module would randomly select from. Service four makes use of a dictionary to add some further variety - each choice has a list of synonyms prepared so the user should get a different response each time they reload their web page. I initially programmed this as a long tower of if statements, but after discussing with my cohorts about ways to improve the readability and "cleanliness" of my code, I settled on this approach (thank you for the tip, Liam!). 

![serv-4-examp](https://user-images.githubusercontent.com/100293943/177959540-19917a08-73c0-4d96-ab81-b0ccde8e5f57.jpg)

Also visible here is the "second iteration" of the app requested, a small change that can demonstrate its capability to perform rolling updates. I've commented it out for now, but it could be committed to a new feature branch whenver convenient. 


## Unit Testing
As the app is relatively simple, it wasn't too difficult to achieve 100% - as the four services are separate entities, they must be tested serparately. Any time a service relies on input from another (for example, service 1) we can "mock" the response to check the app behaves as expected. 

The other three services take input, but then perform their function and return the result, so no mocking was necessary - we could test them normally with http requests. 

I had to think for a moment on how to test something that's designed to be random - eventually I realised that if I feed in a specific input, I could just check whether the response was in the list of repsonses expected. 

![tsting-s-4 jgp](https://user-images.githubusercontent.com/100293943/177961231-42186006-240b-42c8-b29e-7590ec5e0c2d.jpg)


## System Integration, Deployment, and Build
Particularly on a app like this with multiple stages and components, a pipeline build is really helpful to visualise the different stages of deployment. Jenkins allows us to do this nicely, and will act as the CI server for this project. From there, Jenkins will perform our tests, archiving the results for easy viewing, install and instigate Ansible. Ansible then kicks into action, installing everything our deployment environment needs to run our docker containers, then instigating them in unison using docker-compose. 

![an-installing-d](https://user-images.githubusercontent.com/100293943/177962362-758dbc71-3059-4527-93e8-eccf5f6d16ce.jpg)


![jenkins-calling-an](https://user-images.githubusercontent.com/100293943/177962582-ec5d92a3-8bcc-449d-9e15-e3048b7eccb6.jpg)

Above is the jenkinsfile calling on various ansible playbooks for the automation of various pieces of installation and preparation for the app's function. 
A webhook ensures rolling updates are easily achieved, meaning jenkins will start a new build each time the main codebase is updated. 
NGINX acts as a reverse proxy, displaying only service 1 to the user (our frontend) no matter what they put into the address bar. Nginx is also installed and managed by docker and dockercompose.

## Reflection
In comparison with my first project, this has run an enourmous amount more smoothly. With more idea of what to expect, I was able to plan my time effectively, and I have no doubt that had I not had a positive covid result on the second day of the project and been bedbound for several days, I'd have been able to achieve my ambitious goals of using ansible to instigate GCP instances, meaning the app can start up with even less user input. Sadly, both this and use of an Orchestration Manager was not possible in the time frame. Despite this, I'm proud of the app, simple as it is, and I think it seems durible. 

## Final Thoughts
Through this project I built an upp using Python, making use of Flask and a html template. I used the random module in seperate containerised services to select from a list of objects and descriptives, then combined those two items in a third containerised service, before displaying it on a final service. The containers are managed using docker-compose, and the final result is displayed to the user using nginx, in a backwards proxy setup. 
