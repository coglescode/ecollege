# Final Project Capstone # 
<br>

# First steps #
  1. Read the **requirements.txt** file attached on the root of the project folder. 
  2. Download the project code [here](https://github.com/coglescode/capstone/archive/refs/heads/web50/projects/2020/x/capstone.zip) and unzip it.
  3. With your favorit terminal `cd` into the folder named `capstone` this is the project folder.
  4. Type and press Enter to run the following commands `python manage.py makemigrations ecollege`. This will migrate all the settings necesary of the project into the database to make it functional.
  5. Type and press Enter to run the following commands `python manage.py migrate` to validate step 3.   
<br>

# Understanding #
Inside the project folder `capstone` there are two apps, one called `ecollege` and the other `usertype`, this two apps are the main ones we are going to work with.

Head back to your terminal and run `python manage.py runserver` to start the web server. You will see a few lines similar like below.   

  `System check identified no issues (0 silenced). `  
  `October 30, 2021 - 12:03:37`  
  `Django version 3.1.2, using settings 'capstone.settings'`  
  `Starting development server at http://127.0.0.1:8000/`  
  `Quit the server with CTRL-BREAK.`     

In the second last line there is a link there you can open follow to open the web application on your browser. You can copy the url into your browser search bar or press `CTRL` key on your keyboard and click the url to open it automatically in your browser. You will see the index page of this web app Ecollege.

__Ecollege__ is an e-learning platform where users can be both teachers or students. As a teacher you can manage and publish your own courses, while being an student of somebody else courses. In order to become one of this two rolls you have to register first. If you are on a desktop computer, on top of the index page there is two links `Teacher Register` and `Student Register`, let's register as a teacher first to see its functionality. Click on `Teacher Register` and create your account, at the end of the form there is an input labeled `Group` where you are going to choose `Instructors` in order to create your Insctructor account. Click on `Create my account`.  

You has been redirected to a log-in page, go ahead an log in, you will be redirected to this page:

![create_courses](/readme_assets/create_courses.jpg)
<!-- img src="./readme_assets/create_courses.jpg" alt="create_courses" width="100%" height="0%" -->














