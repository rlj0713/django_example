# Import the render shortcut to render templates
from django.shortcuts import render

# Import the Section model from this app
from .models import Section

# Define a view function that will handle requests to the forum home page
def section_list(request):
    # Query the database to get all Section objects
    sections = Section.objects.all()
    
    # Render the 'section_list.html' template, passing in the sections
    # The dictionary {'sections': sections} makes the variable 'sections'
    # available inside the template for looping and displaying data
    return render(request, 'forum/section_list.html', {'sections': sections})
