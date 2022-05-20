# Overview

This is my attempt at making a simple Heating, Ventilation, and Air Conditioning (or HVAC) ToDo list using Python and Django. I wanted to be able to have a front end
that handles user input and then outputs that input into a table on another page with the status of each task the user inputs. I have only been able to get as far as 
passing data in from the user and being able to output it in the python terminal. This web app is run locally on my computer and you have to run a command to start the server.

Steps to begin program:
The command you need to run in your editor is python manage.py runserver **** (4 numbers for the port, if you leave blank it will default to use 8000).

After you open the link after starting the server, you need to enter /HVACtodo to get to the application.


I wanted to right this software because I was interested in learning how to create a website that isn't purely HTML, CSS, or Javascript and wanted to learn how to make 
the data communicate with each other.

[Software Demo Video](https://www.youtube.com/watch?v=SNpUZO0ArOc)

# Web Pages

My first page is the one with the most happening of the three pages. It has the form where the user is prompted to input data and press submit. This sends the data 
from the form back to the backend where it is queried and shown in the terminal. After clicking submit it links to the next page with so far just has three buttons 
with status updates and when one of those is pressed it links to the third page which just says Task Updated.

# Development Environment

I used Visual Studio Code as my editor and Python, HTML, and CSS as the primary languages. I also used Zoom to record my tutorial and Youtube to upload my video.

# Useful Websites


* [Django Tutorial from Django's website](https://docs.djangoproject.com/en/3.0/contents/)
* [Stack Overflow - Template not found error](https://stackoverflow.com/questions/27973522/django-template-not-found)
* [HTML and Django Help](https://www.geeksforgeeks.org/render-html-forms-get-post-in-django/)

# Future Work

* I need to be able to bring the data that the user inputs back into my html pages to display.
* I need to get my objects working correctly because I think that is what is my next main obstacle in sending data back to the frontend
* I also really need to make the display a bit better, pretty bare bones right now.
