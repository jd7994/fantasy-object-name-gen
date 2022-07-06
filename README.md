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
While designing the model, I realised quickly that implementing both a foods liked and foods disliked field would be complicated, both in terms of back-end and front facing UI - already we're looking at a many to many relationship, so doubling up that relationship seemed like something that could potentially be added to the app later if there was time. Using MoSCoW principles, I decided specifying what the cats liked was a Must and what the cats did not like was a Could. I also realised that I'd be looking at another many to many relationship including the medical care information for the cats, so decided to simplify. Instead of a full care app, the cat-carer-5000 will aim specifically at feeding the cats food that they like the most. Given the time constraints of the project, that seemed like a more reasonable aim. Other aspects of care could be added later. Obviously this change would reflect a change in the DoD (definition of done). 

## Definition of Done
With these adjustments made to the project, I've focused and redefined and am ready to consider the DoD(definition of done) for each main task on the project. 
- Testing must be written and passed with 100% coverage
- Features must meet or excell acceptance criteria

## Risk Assessment
With a small project like this handling non-sensitive data, the risks are not particularly severe, but a risk assessment has been carried out, the results of which are below.

![Risk Assessment - Sheet1_1](https://user-images.githubusercontent.com/100293943/173845149-5f125b6e-e14a-43db-aa75-c55f54f34703.jpg)

Another way the project could be extended in the future would be add the funcionality to login as a particular user and access only your own files. As the app stands at the moment, it's only suitable for one user, as all information will be available to anyone who uses it. 

## Implementation and Adaption
![routes models](https://user-images.githubusercontent.com/100293943/173849618-379e6533-a879-46e4-89bc-db18ec6ed669.jpg)
(Above is the implementation in progress, below is the first version of the home page, displayed for the first time)
![First sign of life](https://user-images.githubusercontent.com/100293943/173846006-6bf44dc8-4263-4e11-8d0d-c918bd81fb90.jpg)

Creating the code and building functionality was fairly trouble free, apart from one feature - I was keen to implement a page that allowed the user to pick form the list of foods which foods their cat liked. This required me to create a form with a field for each item on the food table in the database. 

This proved quite tricky, shifting several 'for loops' around, and experimenting with feeding various types of data into jinja2 to get the desired response. Eventually it worked as intended, but I still had a problem. The form is instantiated when the app is launched, and if you then add a food item to it, because the route to the page expects a field for each food item in the database, the table is a field short because it doesn't update each time an item is added, only each time the app restarts. 

Here's the error I keep running into:
![error2](https://user-images.githubusercontent.com/100293943/171618127-a9f79a35-1b9f-4212-b2ca-36ab5f8f1bf8.jpg)
![error3](https://user-images.githubusercontent.com/100293943/171618132-ab510139-4c62-46f6-89e1-c22767d91a41.jpg)
![error1](https://user-images.githubusercontent.com/100293943/171618135-cc8fcb75-590e-4502-bf80-dc004196dc86.jpg)


At first I thought I'd have to completely remove the many to many fuctionality, which was frustrating - the relationships and tables actually worked fine, the issue was really related to the way I wanted to display that information to the user. This was when I created the devlight branch, and began simplifying substantially. 

Thanks to the extension granted to our group, I was able to keep my many to many functionality and shift around how I use and display the information. I decided that to prove the concept of the app, I'd hard code a good number of food objects, still allowing the user to enter the main focus of the app, their cats. This allows us to keep the complex relationships and good functionality of the app as a whole, but removes the functionality of intelligently adaptive form fields for the food objects. I feel that at this stage of my training it's reasonable to demonstrate the potential for the app without implementing this complicated functionality. This change also reflects a change in the DoD(definition of done). 

## Unit Testing
Once I'm confident the webapp is stable and functional, I begin work on unit testing. This ensures the app performs as expected and responds in a predictable way to data entry, as well as get requests to all routes associated with the app and post requests to any routes that allow them. Testing was achieved by considering all functionality of each page, and then implementing code to test all aspects of that functionality. After thorough testing, I'm able to achieve 99% coverage. 
![Test Coverage](https://user-images.githubusercontent.com/100293943/173849662-1fba4c38-60cf-4b3b-86b3-e58c5a2cbaf9.jpg)

The final 1% is a single line of code that functions only to populate a list to feed information into a html template. This last 1% took me a while!
![1% not covered by testing](https://user-images.githubusercontent.com/100293943/173853954-20ab26f3-da02-42f0-9a91-405bb8ecec14.jpg)

I adapt and implement code adding a test food_like relationship, and then check the liked food is present in the final template displayed. This allows me to achieve 100% test coverage. ![final_touch](https://user-images.githubusercontent.com/100293943/173854913-914c2e17-5e3d-4e29-978b-c248184294ec.jpg)

![SUCCESS](https://user-images.githubusercontent.com/100293943/173854293-7ed1ebe4-9405-4262-9718-544806e421df.jpg)
It is at this point that I begin pushing to main. 

## System Integration, Deployment, and Build
I'll be integrating Jenkins to produce builds of this project, as well as automating testing on new commits. I planned in integrate the app through a pipeline project to accurately view the separate stages of the build. Because of the way Jenkins runs projects, to allow a build to "complete" while still running the app, I chose to use a linux systemd service file to create a service to handle the running of the app - this allows Jenkins to start (or restart) that process, as well as producing and running tests, performing maintenence and keeping a clean deployment space. That way, our Jenkins build will complete properly, but our app will run perpetually. 
![systemd-service-file-on-deploy](https://user-images.githubusercontent.com/100293943/174312116-f9787ddf-f363-4f01-937f-babbe9139dc4.jpg)

Above you can see the .service file has been fed everything it needs to work properly, our environment variables and the sources for the commands that are used to start it up.

I also applied a webhook from our github repository, meaning that any time a new push is made to the repo, Jenkins will spin up a new build, performing tests (and returning those test results as a downloadable artifact), launching the systemd process on the deployment VM. It will do all of this automatically, following a jenkinsfile:  
![jenkinsfilefinal](https://user-images.githubusercontent.com/100293943/174305500-7fc17fb8-7644-498d-93ab-a23ee7aba27a.jpg)

![the successful build](https://user-images.githubusercontent.com/100293943/174305564-715927ac-7dc6-4a42-8f5d-115187b33545.jpg)

## Reflection
This app has been an excellent lesson in project planning and management - because I was overambitous in the scope of the project, I had to adapt my plans throughout to meet realistic and achievable goals. This is an excellent lesson to take forwards - keep plans grounded, and based in code currently achievable by your skill level. More careful planning would have made this project easier. 

Another issue I ran into was I lapsed in keeping my Jira board updated after the first week of the project - our timescale shifted dramtically, meaning my plan for the project and timescale changed dramatically as well. In hindsight, my first job when learning this should have been updating my Jira to keep my day to day achievements managable and reasonable. 

Finally, I followed what I now know is incorrect professional protocol in pushing my project to main - my logic at the time of this project was I carefully kept the project on a dev (or devlight) branch, but once the app was stable and functional I pushed to main. I now know that I should have then created a new dev or deployment branch, worked on that branch until my deployment was functional and complete, then merged with main again. Because I considered the project itself (that is, the code itself) complete, I thought it was fine to keep pushing to main. I now understand this is unacceptable. 

## Final Thoughts
Through this project I built an upp using Python, making use of Flask to create intelligent, recreatable templates. I stored information for the app across several tables on an SQL database, using a one to many table and a many to many table. I've implemented the app through a Jenkins pipeline system, allowing for automation of thorough testing (using pytest) and automatic deployment on a dedicated deployment Virtual Machine. I feel my project made a few basic mistakes that are understandable for a new developer, but overall I'm pleased with the function of the project and I feel I implemented the requirements well. 
