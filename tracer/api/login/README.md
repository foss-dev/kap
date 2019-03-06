# Login Layer

In this layer, we'll do operations in the [features](#features) section.

## Features

- Login User
- Register User

## Info

All data operations work in controllers.py file. User requests are also coming here. 

~~Register user function not implemented yet.~~

When a user tries to attempt to log in firstly user an SQL query runs. These parameters applied to check unique user.

If the query created using columns named `email` and `active`, it returns an object, the password is checked.

Passwords control with Werkzeug `check_password_hash` function.

In this PR any user can register as admin.