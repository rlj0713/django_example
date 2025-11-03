# Import the render shortcut to render templates
from django.shortcuts import render, redirect, get_object_or_404

# Import the Section model from this app
from .models import Section
from .models import Post

# Import the PostForm and ReplyForm model from this app
from .forms import PostForm
from .forms import ReplyForm

# Define a view function that will handle requests to the forum home page
# Note that this function was added in part 7 of the readMe
def section_list(request):
    # Query the database to get all Section objects
    sections = Section.objects.all()
    
    # Render the 'section_list.html' template, passing in the sections
    # The dictionary {'sections': sections} makes the variable 'sections'
    # available inside the template for looping and displaying data
    return render(request, 'forum/section_list.html', {'sections': sections})

# Note that this function was added in part 8 of the readMe
def create_post(request):
    if request.method == 'POST':
        # populate form with submitted data
        form = PostForm(request.POST)
        if form.is_valid():
            # save the new Post to the database
            form.save()
            # go back to home page
            return redirect('section_list')
    else:
        # empty form if GET request
        form = PostForm()

    # If the user submits the form (POST request), validate and save it
    # If the form is invalid or it’s the first visit (GET request), show an empty form
    # redirect('section_list') → sends the user back to the home page after submission
    return render(request, 'forum/create_post.html', {'form': form})

# Note that this function was added in part 9 of the readMe
def create_reply(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # find the post being replied to

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)  # don’t save to DB yet
            reply.post = post               # assign the Post
            reply.save()
            return redirect('section_list')  # back to home page
    else:
        form = ReplyForm()

    return render(request, 'forum/create_reply.html', {'form': form, 'post': post})