# AWWWARDS 2021

#### Created on 19 July 2021
#### By Samuel Maingi Mutunga

---
# Description  
This is a WebApp that Allows a Any use to login, Post project they have created and Receive a reviews and Rating from their Peers, Work Mates and Friends. Also Has Various API's available to implement to your Website

---
## User Stories  
User Can :-

* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects
* View projects overall score
* View my profile page

---
## Access the website
Need the latest browser to be able to View

Follow this link https://awwwards254.herokuapp.com/

It is hosted by heroku

---

## Setup and Installation  
To get the project .......  
  
##### Clone Repository:  
 ```bash 
https://github.com/layersony/awwwards.git
```
##### Install and activate Virtual Enviroment envgallery  
 ```bash 
cd awwwards  && python3 -m venv envawwards && source envawwards/bin/activate 
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
##### Setup Database  
  SetUp Database User,Password, Host then following Command  

  Create .env file
```bash
  SECRET_KEY='<SECRET_KEY>'
  DEBUG=True 
  DB_NAME='database name'
  DB_USER='database user'
  DB_PASSWORD='password'
  DB_HOST='127.0.0.1'
  MODE='dev'
  ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
  DISABLE_COLLECTSTATIC=1

  EMAIL_USE_TLS=True
  EMAIL_HOST='smtp.gmail.com'
  EMAIL_PORT=587
  EMAIL_HOST_USER='email'
  EMAIL_HOST_PASSWORD='email-password'
```

 ```bash 
python manage.py makemigrations portfolios 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run Application  
 ```bash 
 python3 manage.py server 
```
##### Test Application  
 ```bash 
 python manage.py test awwwards
```
Open the application on your browser `127.0.0.1:8000`.  

### API's
##### local-Machine
```bash
http://localhost:8000/api/users/
http://localhost:8000/api/projects/
http://localhost:8000/api/profile/
```
##### Live Link
```bash
https://awwwards254.herokuapp.com/api/users/
https://awwwards254.herokuapp.com/api/projects/
https://awwwards254.herokuapp.com/api/profile/
```
  
### Access Django Admin
```bash
>>> Username: layersony
>>> Password: < Buy me Coffee >
```
## Technology used  
  
* HTML, CSS, Bootstrap

* Git

* Pythonp, Django Framework, Rest_framework

* Heroku 
  
  
## Bugs  
* Refresh Page for Review Rating to Appear
  
## Contact Details
sammaingi5@gmail.com

@code_with_maingi (Twitter)

@Maingi `Slack Moringa`

---

### License
This Project is under the [MIT](LICENSE) license

Copyright (c) 2021 MaingiSamuel