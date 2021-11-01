# Final Project Capstone # 


# Distinctiveness #
This  project is based on existing e-learning platforms on the internet with the distinctiveness of __is free of charge for all users__ that seek free education no matter social status or economic situation. Instead of having a price range, limited discounts an so on. I decided to make it free for all students and you won't find a payment system, cart or promotions of any kind. 

From an Instructor perpective this can be controversial due to give free knowledge to people with the only reward of an happy student that later spread same knowledge to others in classrooms or work places.
Thas why we only accept Instructors that are passionated to give knowledge.
This project is built for you to teach or learn, that's why there is not any kind of social system, we want you to fully commit to the given rolls to be in this platform.

# Complexity #
This project contains two apps `ecollege` and `usertype`.
The app `ecollege` take care of the content to be created by Instructors and consumed by students, this two rolls are handled by the `usertype` app, that also handled the registration and log in for both rolls.
As an Instructor you can create and manage your courses content you can also check is every content is showing correctly this mean you can check your courses content as an student without the need of register as one. This is handled in the back-end, to fully understand the complexity of this project you might want to read the Back-end session in this documentation.


# Understanding #

# Back-end #
Inside the project folder `capstone` there are a few files and folder that compose the entire project
We are going to take a look into the subfolder `ecollege` which is the main app of this project.

## Inside ecollege folder ##
`static` folder holds the `*.css` and `*.js` files necesary to style the project.

`templates` folder holds subfolder with `*.html` files that compose the body for the courses content of the project.

`templatetags` folder holds `course.py` file. This file has a function that acts as a template filter when accessing the item model name, this also build the link to edit the object.

`admin.py` . In this file are registered some models to be manageable from the administration site. 

`fields.py` file handles the ordering of each course modules content.

`forms.py` file holds two forms. The first form is a formset based on Course and Module models, that takes care of the module content for each course. 

`models.py` file holds the information that we are going to ask for in the project to later be saved into the database, like the course content, the differents type of content for each course module and the ariety of subject. There are a total of 9 models.

`urls.py` file holds the urls routes that you are going to click in this project, every url point out to a function into views.py that recieve the data you are going to ask and recieve.

`views.py` file holds python functions that takes care the web request and returns a web response when a user register, log in, log out, enroll in a courses, also the ability for instructors to create, edit and delete courses and its respective modules and contents. There are a total of 15 view functions.

## Inside usertype folder ##
`templates` folder holds subfolder with `*.html` files that compose the body for the courses content of students as well as the registration templates for both studenst and instructors.

`forms.py` file holds two forms. The first form is for enroll courses based on the Course model in `ecollege` app `models.py` file. The second one is the choice input field that you'll see when registering to get access into the site by choosing __student__ or __instructor__ roll.

`urls.py` file holds the urls routes that you are going to click for registering as student or instructor, as well for accessing your course content, every url point out to a function into views.py that recieve the data you are going to ask and recieve.

`views.py` file holds python functions that takes care the web request and returns a web response when a user want to have access to its enrolled courses content. There is as well functions that takes care of the registration process based of the roll choosen by the user (student or instructor)

# Inside media folder #
`media` folder holds two subfolder `file` and `images`. This folder are going to be used for isntructors when they upload their courses materials for the courses content, instead of saving it into the database we are going to use this subfolder to store everything and use a url path that tells the database where to look for the courses materials.

# Additional Information #
## Inside readme_assets ##
This folder holds the images used for this readme

## Requirements.txt ##
In the requirements.txt file you will find the two python packages needed to run this project.
<br>
<br>

# Front-end #
## How to run and use the project ##
# First steps #
  1. Read the **requirements.txt** file attached on the root of the project folder. 
  2. Download the project code [here](https://github.com/coglescode/capstone/archive/refs/heads/web50/projects/2020/x/capstone.zip) and unzip it.
  3. With your favorit terminal `cd` into the folder named `capstone` this is the project folder.
  4. Type and press Enter to run the following commands `python manage.py makemigrations ecollege`. This will migrate all the settings necesary of the project into the database to make it functional.
  5. Type and press Enter to run the following commands `python manage.py migrate` to validate step 3.   
<br>

Inside the project folder `capstone` there are two apps, one called `ecollege` and the other `usertype`, this two apps are the main ones we are going to work with.

Head back to your terminal and run `python manage.py runserver` to start the web server. You will see a few lines similar like below.   

  ```
  System check identified no issues (0 silenced).   
  October 30, 2021 - 12:03:37  
  Django version 3.1.2, using settings 'capstone.settings' 
  Starting development server at http://127.0.0.1:8000/  
  Quit the server with CTRL-BREAK.     
  ```
In the second last line there is a link there you can open follow to open the web application on your browser. You can copy the url into your browser search bar or press `CTRL` key on your keyboard and click the url to open it automatically in your browser. You will see the index page of this web app Ecollege.

__Ecollege__ is an e-learning platform where users can be both teachers or students. As a teacher you can manage and publish your own courses, while being an student of somebody else courses. In order to become one of this two rolls you have to register first. If you are on a desktop computer, on top of the index page there is two links `Teacher Register` and `Student Register`, let's register as a teacher first to see its functionality. Click on `Teacher Register` and create your account, at the end of the form there is an input labeled `Group` where you are going to choose `Instructors` in order to create your Insctructor account. Click on `Create my account`.\
\
![index](/readme_assets/index.jpg)      


# Be an Instructor #
You has been redirected to a log-in page, make sure to choose __Instructors__, go ahead an log in. Once you have logged in successfully you will be redirected to your profile page where you can create new courses and manage them. Now create a course.\
\
![create_courses](/readme_assets/create_courses.jpg)   

\
On the next page there is a form that you are going to fill with the information of your course. All fields are required.  Once done save it.\
\
![edit_modules_form](/readme_assets/edit_modules_form.jpg)

You will be redirected back to your  `My courses` page where now you can see your first course created, but this course is still empty. Click `Edit modules`, and create at least one module and save it.\
\
![edit_modules_form](/readme_assets/edit_modules_form.jpg) 

No you will see a `Manage content` link has been added to your course box, click it to finally add some content to module you just created. You will see a page like below.\
\
![add_content_module_form](/readme_assets/add_content_module_form.jpg) 

You might want to start by adding some text to your course followed by a video or an image or both. `Text`, `Image`, `Video` and `File` are links that leads to its own form to load the course module content. With `Image` and `File` you can upload content from your device. `Text` is just a textarea there you eihter type or copy the text you are going to present for the course. In `Video` you are going to paste an url from another source like Youtube. Once your are done you will see that the page of the course has changed.\
\
![content_module](/readme_assets/content_module.jpg)  

Now your are able to edit or delete each content of the module.
On the left side of the page there is a sidebar there you can navigate between modules, right now we just created one module, go ahead and click on `Edit modules` and create as many modules you like to see the sidebar functionality.

\
You can see the course content as teacher but we are not going to do that. On the top navbar log out and click on `Register`, this will take you to a form to register as an student, make sure you choose __Student__ from the dropdown input.

# Be an student #
Once logged in you will be redirect to your personal page `My courses` where all courses you are enrolled to
will be displayed but right now you are not enrolled in any course, click on `Browse courses` link to see all courses available.\
\
![student_courses](/readme_assets/student_courses.jpg)  

Now you are able to choose any course if available on the right side, on the left side there is a sidebar with all existing subjects in the Ecollege platform, choose any subject to see all existing courses for that
subject, choose a course and click on the name.\
\
![all_courses](/readme_assets/all_courses.jpg)

Click on `Enroll now` button.\
\
![enroll_course](/readme_assets/enroll_course.jpg)

Now is time to sit and learn from your chosen course.\
\
![course_content](/readme_assets/course_content.jpg)

One thing good to know, if you logged out and log in back again, you will be redirected to your personal `My courses` page but this time you will see the courses you are enrolled to. By clicking to `Acces contents` link will take you to the courses content. \
\
![courses_enrolled](/readme_assets/courses_enrolled.jpg) 

# Happy learning\! #
  




























