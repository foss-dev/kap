# Changelog


## [unreleased]

### Other

* I updated requirements file and updated CHANGELOG.md file. [aligoren]

* I added documentation for applications layer. [aligoren]

* I added auto CHANGELOG generator. Repo uses [https://github.com/vaab/gitchangelog](https://github.com/vaab/gitchangelog) now. [aligoren]

* Added __repr__ for keys. [aligoren]

* Now, after new key, other keys will be inactive. And also user can set key status as active/inactive. [aligoren]

* Added new resources for this project. I added resources for UUID and secret keys. [aligoren]

* Salt added to BaseConfig class. [aligoren]

* Keys endpoint added. [aligoren]

* I added API Key generator method. You can check /tracer/api/keys/README.md file. [aligoren]

* Keys model generated. User and Keys models have fields named 'created_at' and 'updated_at' now. [aligoren]

* Api KEY Generator layer created. It only generates API for now. The other features not implemented yet. [aligoren]

* I added register endpoint. User can register without other logged user's action. [aligoren]

* Documentation updated for register api endpoint in login layer. [aligoren]

* I added documentation for login API. [aligoren]

* I added login API. [aligoren]

* I added test section. [aligoren]

* I disabled sqlalchemy's track modification setting. [aligoren]

* I added user test for create and select queries. [aligoren]

* User API documentation was updated. [aligoren]

* Base endpoints were changed. And I added DELETE request to remove resource. For User API, I completed all HTTP requests. [aligoren]

* Url map strict slashes rule changed to False. Because HTTP requests were not working. [aligoren]

* Added UPDATE user endpoint. It only works with PUT request. [aligoren]

* All users listing now with base endpoint. [aligoren]

* I added key to origins array for CORS config. [aligoren]

* Added new features. [aligoren]

* I moved changelog section from README.md to CHANGELOG.md file and README.md file is completely English now. [aligoren]

* Updating README.md for Application resources and changelod. [aligoren]

* The user endpoint was changed as 'users' [aligoren]

* Mixins are removed from models. [aligoren]

* User info returns from database and also users can create now. [aligoren]

* Documentation added for user api. [aligoren]

* Users will have their name. So, for first db innstallation, admin user will create with 'John doe' name. [aligoren]

* I added user' name to models.py. Now, user will have their name. [aligoren]

* Using Werkzeug generate_password_hash, I changed the salt password. It will store an encrypted password to the first DB setup. Also, all passwords are will be stored as encrypted. #8 close. [aligoren]

* Requiresments updated. [aligoren]

* Readme changed. [aligoren]

* Models have User and Role classes now. They are connected with each other. Mixins are may not necessary here. [aligoren]

* Configure_app added for database operations. Db also initalize here. [aligoren]

* *.db files won't push to git now. [aligoren]

* I added ENV config and Database file variable into the Development class. #5 Fixed. [aligoren]

* Database Setup file created #4 fixed. [aligoren]

* Decoratorler eklendi. Ilk decorator deprecated icin. [aligoren]

* Fix typo. [aligoren]

* Unutulan init ve repr fonksiyonları eklendi. [aligoren]

* Kullanıcı model'ini oluşturdum. Henüz migration gerçekleştirmedim. #1 fixes olur. [aligoren]

* Admin endpoint'ini user olarak değiştirdim. Kullanıcı işlemlerinin döneceği kısım burası olacak. Şu an boş çöp data dönüyor böylelikle Insomnia ile test edebiliyorum. [aligoren]

* Readme.md Cors bilgisini ekledim. [aligoren]


