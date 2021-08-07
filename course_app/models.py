from django.db import models

# Create your models here.
class New_CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['course_name']) < 6:
            errors["course_name"] = "Course name should be more than 5 characters."
        if len(postData['description']) < 16:
            errors["description"] = "Descriptionshould be more than 15 characters."
        return errors

class Course(models.Model):
    course_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = New_CourseManager()











# Make a new Django project and app

# Have the root route render the main wireframe above

# Create the POST method to add new courses to the database

# Ensure that the name entered is more than 5 characters, and the description is more than 15 characters

# Display all the courses in a table beneath the form

# For each course, have a link to remove that renders a page as shown in the second wireframe

# If the user selects "No," redirect to the root route. If the user selects "Yes," delete the course and redirect to the root route