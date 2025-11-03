# django_example
This is an example of a RESTful Django API with a simple front-end
If you follow the steps below, you should have a full-stack web application complete with a database, backend, frontend, and authentication system.

Part I: Creating & Activating Virtual Environment
1) On Github, I created a new repository called django_example and upon creation, I chose to open a github codespace to do the development.
2) Terminal --> 'python -m venv vevn'
    This creates a virtual evironment for the project
3) Terminal --> 'source venv/bin/activate'
    This activates that virtual environment and adds the (venv) tag to my terminal.

Part II: Install Django
1) Terminal --> 'pip install django'
2) Terminal --> 'django-admin --version'
    This prints 5.2.7 (or higher) and confirms the install

Part III: Start the Django project
*Note, I'm building a classroom message-board app and calling it 'forum'.
1) Terminal --> 'django-admin startproject messageboard_project .'
    This creates the folder structure in django
2) Test the app: Terminal --> 'python manage.py runserver 0.0.0.0:8000'
    Choose 'open in browser', this should show a blank app with a rocket-ship background.
    Terminal --> 'Ctrl + C' to shut the server down

-----------------------------------------------------------------------------------------------------------
Periodically throughout a project it is a good idea to save changes to github
To save to github, you need to:
    A) git add .
    B) git commit -m "Describe what you did"
    C) git push
As a rule of thumb, each time you make a change and your code 'works again', commit those changes.
Each commit should really only encompass one major change.

To check your commits, go back to github and note the contribution activity at the bottom of your profile page.
You should see your commits here.
-----------------------------------------------------------------------------------------------------------

Part IV: Create the Forum App
1) Terminal --> 'python manage.py startapp forum'
    This creates more file structures necessary for the app
2) Open the messageboard_project/settings.py file, scroll down and find the  INSTALLED_APPS list. At the end of the list, on a separate line, add 'forum'.
3) Restart the server - Terminal --> 'python manage.py runserver 0.0.0.0:8000'
    The rocket background should still be there
    Terminal --> 'Ctrl + C' to shut the server down

-----------------------------------------------------------------------------------------------------------
Commit to github:
    A) git add .
    B) git commit -m "Created Forum App inside of messageboard_project"
    C) git push
-----------------------------------------------------------------------------------------------------------

Part V: Set Up the Models
 - The structure of this project is that that sections will have posts which will in turn have replies
 - The hierarchy of classes within the app is hard to change later, so for your app, make a point to plan well here.

1) Open the forum/models.py file and add classes
2) The specific code is located there, feel free to copy that or adopt the general outline in your own app
3) Terminal --> 'python manage.py makemigrations'
    This stages changes to the database structure
4) Terminal --> 'python manage.py migrate'
    This pushes those models to the database
    You should see the migration with a green OK message next to each change 

-----------------------------------------------------------------------------------------------------------
Commit to github:
    A) git add .
    B) git commit -m "Add Section, Post, and Reply models with __str__ methods"
    C) git push
-----------------------------------------------------------------------------------------------------------

Part VI: Register Models in Admin
This entire process helps build out the admin page so that users can edit from a GUI.
1) Open the forum/admin.py file
2) Update your file to look like the one in this example

-----------------------------------------------------------------------------------------------------------
Commit to github:
    A) git add .
    B) git commit -m "Updated Admin Module"
    C) git push
-----------------------------------------------------------------------------------------------------------

Part VII: Create the first Forum Page
1) Create a folder in the main forum folder called 'templates'
2) Create a folder within that folder called 'forum'
3) Create a file within that folder called section_list.html
4) Copy the text of this html file for now
    Take a look at (https://www.w3schools.com/django/django_template_variables.php) for Django syntax
    It feels like python, but there are a few differences
5) Open the forum/views.py file
6) Copy the text of this file for now, but take a look at the documentation on that page.
7) Create a file called urls.py in the 
8) Update that file to look like the one in this example, but take a look at the documentation on that page.
9) Open the messageboard_project/urls.py file and add the line --> path('', include('forum.urls')), to the urlpatterns list.
    There is plenty of documentation on this file, please read that before moving on.

-----------------------------------------------------------------------------------------------------------
Commit to github:
    A) git add .
    B) git commit -m "Include forum app URLs in project URLs"
    C) git push
-----------------------------------------------------------------------------------------------------------

Step VIII: Add a form for creating new posts

1) Create a forms.py file in the parent forum/ folder
2) Use the file in this project as an example
3) In forum/views.py, create a view using this project as an example.
4) Create this file:
    In forum/templates/forum/create_post.html
5) Use this file as an example
6) Open the forum/urls.py file and add --> path('create/', views.create_post, name='create_post'), to the urlpatterns list.

    To test, we need to manually add a few things.  To do so, we need to access the /admin page:
    A) Terminal --> 'python manage.py createsuperuser'
    B) Fill this out and don't forget the creds, I chose admin as a user and my actual e-mail.
    C) Terminal --> 'python manage.py runserver 0.0.0.0:8000'
    D) Open in browser and add /admin to the url
    E) Log in
    F) Choose sections from the dashboard
    G) Create a few sections (I chose to add some courses that I teach)
    H) Navigate to ...8000.app.github.dev/create/
    I) Check the drop-down menu to make sure the sections are populated.

7) Submit some sample data in the form. The home page should show the new post.

-----------------------------------------------------------------------------------------------------------
Commit to github:
    A) git add .
    B) git commit -m "Fix imports and make create post form functional"
    C) git push
-----------------------------------------------------------------------------------------------------------