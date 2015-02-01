# url-shortener
Description: URL shortening service (django)

This project was coded using Python 3.4 and Django 1.7. To try the service on your own you need to install Python and Django and use the manage.py runserver command. After that you can use the service with your browser with the address and port 127.0.0.1:8000 (localhost:8000)... At your own risk, of course!

An sqlite database is used for the URLs. Each new URL given is added to the database. The model's primary key pk is used as the "shortened" ID for the URL. Starts with 1.

project/shortener/models.py has the URL model for the database
project/shortener/views.py defines shorten and getURL
project/project/urls.py has the regexp for the URLs that can be used
project/shortener/templates/shortener/index.html the only template file
