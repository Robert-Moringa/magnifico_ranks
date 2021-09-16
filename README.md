# Magnifico Ranks

This python/django web-app was developed during Moringa Core. This is Week Django week 3 Independent Project.
Date: 16th September 2021
By: Robert Maina

## Description
This web-app will allow a user to post a project he/she has created and get it reviewed by other users. Each user will have a profile. Th e projects will be ranked with respect to; design, usability and content.

## Setup/Installation Requirements
* Live site can be accessed from the following link https://magnifico.herokuapp.com/
* Pre-configured Admin details are:
Password: 12345
Username: Robert

### Known Bugs
* 
* 
* 

### Behaviour Driven Development
* The program should return all added projects on the home page<br>
Given:All projects<br>
When: Url is changed to home page<br>
Then: All projects are displayed<br>

* The project with the highest average should be displayed the first on the home page<br>
Given:A Project with the highest average<br>
When: Home page is accessed <br>
Then: Project with highest average is displayed.<br>

* Admin site should be displayed when "admin/" url is chosen<br>
Given: An admin url<br>
When: The user enters admin url in browser<br>
Then: Admin Login is displayed<br>

* User authentication occurs when Admin tries to Login<br>
Given:Admin page is accessed<br>
When: User tries to login<br>
Then: User details are authenticated to confirm if user is an admin<br>

* User session should end when logout url is chosen<br>
Given:Logout choice is provided<br>
When: User opts to logout<br>
Then: User session is ended<br>


### Technologies Used
* Visual Studiuo was the source code editor.
* Git and Github were my respective used local and online repositories.
* Django was used as the framework.
* Heroku was used in deploying the live site
* Postman for testing the API created.


### Support and contact details
* Contact me through my email: mainarobert16@gmail.com
* The source code is also contained within the folder containing this ReadMe with comments on the code thus third-party support can be offered.

### License
Moringa School
Copyright (c)2021 **Magnifico Ranks presented by Robert Maina**