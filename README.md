# MoodTrackingAPI

## Dependencies:
- Python 3.7 or above <br />
- Django 3 or above <br />
- (Optional) Docker Desktop (PROJECT IS NOT CURRENTLY CONFIGURED)
## Additional Tools:
- django-cripsy-forms
- Bootstrap 5
- Django REST Framework

## Running:

1. To run exclusively on your computer, navigate to the MoodTracking API directory and run ``` python3 manage.py runserver ```
    - Note: One may need to run  ``` python3 manage.py makemigrations``` and ``` python3 manage.py migrate ``` before being able to run the server correctly
    - Docker is available however, this project has not yet been configured to work with Docker
2. Navigate to the development server specified after running ```python3 manage.py runserver ``` in a browser of your choice
   - This is generally at ``` http://127.0.0.1:8000/ ```

## Different URLS and Functionality:

This project has 3 different parts to its functionality

1. REST API through http commands
   - Supports logging in
   - User can GET and POST
2. Web Browserable REST API
   - Supports logging in and signing out through provided login and signup html pages
   - User can GET and POST
3. Full-Stack User Friendly Mood Tracker Application
   - Supports logging in and logging out
   - Provides visual representation of a User's Mood Log
   - Users can append to their Mood Log through a Form
   - Users can visually track streaks

### REST API through http commands

  To access the REST API through commandline or code utilize 

  ``` http -a [username]:[password] [GET|POST] http://127.0.0.1:8000/mood/ ```

  An account can be created through Django commands or through ``` http://127.0.0.1:8000/register ```

### Web Browserable REST API

1. Register through ``` http://127.0.0.1:8000/register ``` if you do not have an account
2. Login to your account through ```http://127.0.0.1:8000/login ```
3. Navigate to ```http://127.0.0.1:8000/mood```


### Full-Stack Mood Tracker

1. Register through ``` http://127.0.0.1:8000/register ``` if you do not have an account
2. Login to your account through ```http://127.0.0.1:8000/login ```
3. Navigate to ```http://127.0.0.1:8000/moodUserFriendly ```
4. Logout by navigating to ```http://127.0.0.1:8000/logout ```

## What if this was a production application?

- Currently this project does not have a custom User Model and instead utilizes the built in Django User model. If this was a production application with more users and data, it would be more effective to create a User Model that holds a list of Mood Inputs, instead of Mood Inputs holding a user id.
- For a better REST API experience, I would add user Authentication tokens. This would allow API requests to use tokens instead of logging in each time and could allow for more effective GET and POST automation.  
- I would configure the app for Docker so one could test the project on a small network
- Create a better dynamic User Interface for Full-Stack experience
- For better performance on a larger scale streak calculations should be performed in the models instead of views
- Track User Consistent Use, Provide Badges/Achievements
