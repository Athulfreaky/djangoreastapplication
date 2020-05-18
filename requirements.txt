
Requirements

Python 3.7
Django (3.0.6)
Django REST Framework


Installation

	pip install django
	pip install djangorestframework
    pip install psycopg2
	
Structure

In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our 
application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around
collections and elements, both of which are resources.

In our case, we have two  resource, usersmodel and activitymodel, so we will 
use the following URLS - /users/ , /activity/ ,/combined_view/ for all users , activity of users sort by username
and combined view of both models respectively:

Endpoint	HTTP Method	CRUD Method	Result

users	GET	READ	Get all users
activity GETREAD	Get the activity sort by username
combined_view GETREAD Get the combined view of both models

Use
There are no authentication

python manage.py runserver

Commands

http://3.22.21.146/users/
http://3.22.21.146/activity/
http://3.22.21.146/combined_view/

Pagination

The API supports pagination, by default responses have a page_size=10 but if you want 
change that you can pass through params page=size=X

