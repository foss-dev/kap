# Keys Layer

In this layer, users will be able to create API keys for their applications. Every application should have only one API key.

If the user removes an API key, applications shouldn't work with the deleted API key.

## Features

- Create API Key
- List Application API Keys (Active / Inactive)
- Update API Key Status

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

To get all application keys endpoint should be like this `http://yourdomain.tld/api/keys/USER_ID/APPLICATION_ID`

If keys exists, you will see an output like below:

```js
[
  {
    "active": false,
    "application_id": 1,
    "created_at": "09.03.2019 12:47:26",
    "id": 1,
    "key": "717aa13d-c017-372b-ae0a-d72b3861bb4e",
    "updated_at": null,
    "user_id": 1
  },
  {
    "active": true,
    "application_id": 1,
    "created_at": "09.03.2019 15:59:41",
    "id": 2,
    "key": "86cfdcdd-2875-3310-a4ee-d9541dad5b43",
    "updated_at": null,
    "user_id": 1
  }
]
```

To update key status you need to use this endpoint

`api/keys/update/KEY_ID`

You will send PUT request.

And JSON body will be like this:

```json
{
	"active": false
}
```