# User Layer

In this layer, we'll do operations in the [features](#features) section.

## Features

- Listing All Users
- Get User Information
- Creating User
- Updating User
- Deleting User

## Info

All data operations work in controllers.py file. User requests are also coming here. 

Above features were completed. But this API still needs security. Because there is no control for requests. Which means, anyone who know this system, can send HTTP requests without any restricting. At this point, we can use JWT. I should open an issue for this. This needs attention.