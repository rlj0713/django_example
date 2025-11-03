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