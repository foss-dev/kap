# Applications Layer

In this layer, users will be able to create their applications to track their logs and custom logs like SQL queries.

## Features

- Create Application
- Edit Application
- Delete Application
- Application Details
- Application Logs
- Application Log Details (If possible elaborate explanation or StackOverflow URL etc.)
- Application Log Filtering

## Info

For the first, we will do the first four in the features list. I'll update this document when I completed the others.

Endpoints will be like this;

**Edit 10.03.2019:**: Logs will be managed in a different layer. This layer only should work for application info.

### CREATE

**Method:** POST

`api/applications`

### EDIT

**Method:** PUT

`api/applications/1`

And will have json body

### DELETE

**Method:** DELETE

`api/applications/1`

### DETAIL

**Method:** GET

`api/applications/1`

This request will return application details by id. Because of will not have applications the same ID, ID will be enough.