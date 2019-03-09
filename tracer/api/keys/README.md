# Keys Layer

In this layer, users will be able to create API keys for their applications. Every application should have only one API key.

If the user removes an API key, applications shouldn't work with the deleted API key.

## Features

- Create API Key
- List Application API Keys (Active / Inactive)
- Remove API Key

## Info

All data operations work in controllers.py file. User requests are also coming here. 

**Currently:** Remove API key and List Application API Keys not implemented yet. Also, this layer has to check whether the API key has already been created or not.

API Keys generates by `uuid.uuid3` method with `uuid.NAMESPACE_DNS` and custom domain. Domain will be like this;

**INT(CURRENT TIMESTAMP) + APPLICATION ID + USER ID + SECRET KEY**

The output should be like this;

`717aa13d-c017-372b-ae0a-d72b3861bb4e`

This is an API to a specific application.

Developer have to pass these params to the `generate_key` method

```py
from tracer.utils.key_generator import generate_key

key_obj = {
    "user_id": user_id,
    "application_id": application_id
}

generated_key = generate_key(key_obj)
```