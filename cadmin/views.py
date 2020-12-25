from django.shortcuts import render, redirect
from blog.forms import  PostForm
from django.contrib import messages

# Create your views here.


def post_add(request):

    # If request is POST, create a bound form (form with data)
    if request.method == "POST":
        f = PostForm(request.POST)

        # check whether form is valid or not
        # if the form is valid, save the data to the database
        # and redirect the user back to the add post form

        # If form is invalid show form with errors again
        if f.is_valid():
            #  save data
            f.save()
            messages.add_message(request,messages.INFO,'Post Added.')
            return redirect('post_add')

    # if request is GET the show unbound form to the user
    else:
        f = PostForm()
    return render(request, 'post_add.html', {'form': f})