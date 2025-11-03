# django_example
This is an example of a RESTful Django API with a simple front-end

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


