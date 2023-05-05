# YaMDb (api v1)
## _The application collects and stores user reviews for works of various categories, be it books or music, movies or paintings by artists._

The YaMDb project collects user reviews for works. The works themselves are not stored in YaMDb, so you cannot watch a movie or listen to music here.
Works are divided into categories, such as "Books", "Movies", "Music". For example, the "Winnie-the-Pooh and All-All-All" and "The Martian Chronicles" works can be in the "Books" category, and the song "Davicha" by the "Beetles" group and Bach's second suite can be in the "Music" category. The list of categories can be expanded (for example, you can add the category "Fine Arts" or "Jewelry"). 
A work can be assigned a genre from a list of presets (such as "Fairy Tale", "Rock" or "Art House"). 
Only an administrator can add works, categories, and genres.
Grateful or outraged users leave text reviews for works and rate the work on a scale of one to ten (integer); the user ratings form an average rating of the work - a rating (integer). A user can only leave one review for a work.
Users can leave comments on reviews.
Only authenticated users can add reviews, comments and ratings.

## Features

- Independent registration of new users via POST request, after which the YaMDB service sends a confirmation code to the specified e-mail address.
- To update the access token, there is no need to use a refresh token and an additional endpoint. The token is updated by re-submitting the username and confirmation code.

## Technologies

- [Python 3.9](https://www.python.org/)  - a programming language that allows you to work quickly and more efficiently implement systems!
- [Django 3.2](https://www.djangoproject.com/)- simplifies the creation of better web applications faster and with less code.
- [Django Rest Framework 3.12.4](https://www.django-rest-framework.org/) - a powerful and flexible toolkit for creating web APIs.
- [PyJWT 2.1.0](https://pyjwt.readthedocs.io/en/stable/) a Python library that allows you to encode and decode JSON web tokens (JWT).

## Installation

Clone the repository and navigate to it in the command line.

> Windows commands are given.

Create and activate a virtual environment:
```
python -m venv venv
```

```
source venv/scripts/activate
```

Update the package management system:

```
python -m pip install --upgrade pip
```

Install dependencies from the requirements.txt file:

```
pip install -r requirements.txt
```

Perform migrations:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Run the project:

```
python manage.py runserver
```

## Examples of work
Detailed documentation is available at the /redoc/ endpoint.
For unauthorized users, API work is available in read mode.

## User roles
Anonymous - can view descriptions of works, read reviews and comments.
Authenticated user (user) - can read everything, in addition he can publish reviews and rate works (movies/books/songs), can comment on other people's reviews; can edit and delete his own reviews and comments. This role is assigned by default to every new user.
Moderator (moderator) - the same rights as an Authenticated user plus the right to delete any reviews and comments.
Administrator (admin) - full rights to manage all project content. Can create and delete works, categories, and genres. Can assign roles to users.
Django superuser - has administrator rights (admin)

###### Access rights: Available without a token.
- GET /api/v1/categories/ - get a list of all categories
- GET /api/v1/genres/ - get a list of all genres
- GET /api/v1/titles/ - get a list of all works
- GET /api/v1/titles/{title_id}/reviews/ - get a list of all reviews
- GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/ - get a list of all comments on a review
###### Access rights: Administrator
- GET /api/v1/users/ - get a list of all users

#### Registering a new user

```
POST /api/v1/auth/signup/
```

Getting a JWT token:

```
POST /api/v1/auth/token/
```

### Examples of working with the API for authenticated users

Adding a category:

```
Access rights: administrator.
POST /api/v1/categories/
```

Deleting a category:

```
Access rights: administrator.
DELETE /api/v1/categories/{slug}/
```

Adding a genre:

```
Access rights: administrator.
POST /api/v1/genres/
```

Deleting a genre:
```

Access rights: administrator.
DELETE /api/v1/genres/{slug}/
```

Updating a publication:

```
PUT /api/v1/posts/{id}/
```

Adding a work:

```
Access rights: Administrator. 
POST /api/v1/titles/
```
Adding a work:

```
Access rights: Available without a token
GET /api/v1/titles/{titles_id}/
```

Partial update of work information:

```
PATCH /api/v1/titles/{titles_id}/
```

Deleting work information:
```
Access rights: Administrator
DEL /api/v1/titles/{titles_id}/
```

### Working with users:

Getting a list of all users.

```
Access rights: Administrator
GET /api/v1/users/ - Get a list of all users
```

Adding a user:

```
Access rights: Administrator
The email and username fields must be unique.
POST /api/v1/users/ - Adding a user
```

Getting a user by username:

```
Access rights: Administrator
GET /api/v1/users/{username}/ - Get a user by username
```

Changing user data by username:

```
Access rights: Administrator
PATCH /api/v1/users/{username}/ - Changing user data by username
```

Deleting a user by username:

```
Access rights: Administrator
DELETE /api/v1/users/{username}/ - Deleting a user by username
```

Getting data from your own account:

```
Access rights: Any authenticated user
GET /api/v1/users/me/ - Get data from your own account
```

Changing data from your own account:

```
Access rights: Any authenticated user
PATCH /api/v1/users/me/ # Changing data from your own account.
```

Deleting a category:

```
Access rights: administrator.
DELETE /api/v1/categories/{slug}/
```

Adding a genre:

```
Access rights: administrator.
POST /api/v1/genres/
```

Deleting a genre:

```
Access rights: administrator.
DELETE /api/v1/genres/{slug}/
```

Updating a publication:

```
PUT /api/v1/posts/{id}/
```

Adding a work:

```
Access rights: Administrator. 
POST /api/v1/titles/
```
Adding a work:

```
Access rights: Available without a token
GET /api/v1/titles/{titles_id}/
```

Partial update of work information:

```
PATCH /api/v1/titles/{titles_id}/
```

Deleting work information:
```
Access rights: Administrator
DEL /api/v1/titles/{titles_id}/
```

### Working with users:

Getting a list of all users.

```
Access rights: Administrator
GET /api/v1/users/ - Get a list of all users
```

Adding a user:

```
Access rights: Administrator
The email and username fields must be unique.
POST /api/v1/users/ - Adding a user
```

Getting a user by username:

```
Access rights: Administrator
GET /api/v1/users/{username}/ - Get a user by username
```

Changing user data by username:

```
Access rights: Administrator
PATCH /api/v1/users/{username}/ - Changing user data by username
```

Deleting a user by username:

```
Access rights: Administrator
DELETE /api/v1/users/{username}/ - Deleting a user by username
```

Getting data from your own account:

```
Access rights: Any authenticated user
GET /api/v1/users/me/ - Get data from your own account
```

Changing data from your own account:

```
Access rights: Any authenticated user
PATCH /api/v1/users/me/ # Changing data from your own account.
```
