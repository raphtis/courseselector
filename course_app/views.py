from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import * 

# Create your views here.
def index(request):

    context = {
        "all_courses": Course.objects.all()
    }
    return render(request, 'index.html', context)


def create_course(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')
    else:
        new_course= Course.objects.create(course_name=request.POST['course_name'], 
        description=request.POST['description']), 
    return redirect('/')


def destroy(request, course_id):
    
    context = {
        'one_course': Course.objects.get(id=course_id)
    }
    return render(request, 'destroy.html', context)

def delete_course(request, course_id):
    # NOTE: Delete one show!
    to_delete = Course.objects.get(id=course_id)
    to_delete.delete()
    return redirect('/')