# Kap Error Logging ve Monitoring System

Kap is a simplistic API based error logging system. You can create applications and track their errors. 

*This is an experimental repo. You shouldn't use it in production if you're not sure if it works as you expected.*

## Planned Features

Planned features are like below. They can change according to requirements.

 - Web UI to users
 - User applications
 - Special API keys for each application
 - Filtering by date range
 - If it possible, links for errors' explanation by the vendor.
 - Filtering by logging types.
 - Log status (Active / Inactive)
 - General log types
 - Adding new log categories
 - Changing the logged data' category


## Running Tests

To run unit tests you need to use this command

```bash
python -m unittest test.YOUR_TEST_FILE_NAME
```

or you can use discover to run all tests.

```bash
python -m unittest discover
```

## Development Resources

This project follows below resources for the project structure.

[https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications)

[https://damyanon.net/post/flask-series-environment/](https://damyanon.net/post/flask-series-environment/)

[https://www.restapitutorial.com/lessons/httpmethods.html](https://www.restapitutorial.com/lessons/httpmethods.html)

[https://danidee10.github.io/2016/12/12/flask-by-example-10.html](https://danidee10.github.io/2016/12/12/flask-by-example-10.html)

[https://realpython.com/python-testing/](https://realpython.com/python-testing/)

[https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure](https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure)