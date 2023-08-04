# Portfolio project for ALX SE

This is the last segment of the ALX SE foundations where peers are required to partner to make a comprehensive project that combines the concepts that were taught during the foundations period.
We decided to make a website which allows people who have apartments or a spacious place to reside to have "roommates" based on location to help solve housing issues experienced in our countries.

## Table of contents

* [Environment](#environment)
* [FrontEnd](#frontend)
* [BackEnd](#backend)
* [Database](#database)
* [Testing](#testing)
* [Integration](#integration)
* [Deployment](#deployment)
* [Maintenance](#maintenance)
* [Development](#development)
* [Authors](#authors)
* [Bugs](#bugs)
* [Landing](#landing)

## Environment

This will be built and tested using the following technologies:
Ubuntu 20.04 LTS.
Python3 venv(virtual environment).
Python console.

## FrontEnd

HTML5: Will be used to create the structure of the website.

CSS3: Will be used to style the website.

Javascript: Will be used to add functionality to the website.

## BackEnd

Python: Will be used to create the back-end of the website on the server side.

Flask: Will be used to create the web application framework.

SQLAlchemy: Will be used to create the database and manage it.

The relevant modules are found within the models folder.

## Database

SQLite: Will be used to create the database and manage it in its initial stages.

For connecting the database to the web application, SQLAlchemy will be used.

Migrations will be done using the Flask-Migrate module to maintain the database in case of any changes to the application.

## Testing

Unit testing will be done using the python unittest module.

Integration testing will be done using the python unittest module.

Manual testing will be done by the developers.

Unit tests will be found within the tests folder.

## Integration

The front-end and back-end will be integrated using the Flask framework.

Third party APIs  like payment processing, map integration, messaging and any other functionality will be integrated using the respective APIs.

## Deployment

The website will be deployed on Heroku when complete.

## Maintenance

The website will be maintained by the developers.

## Development

The initial development files were stored within the models folder for class definitions and web_static folder for frontend development.

An example of a tested user class from the roommate_app is shown below:

    ```sasaka-jr@ubuntu:~/Roommate-to-Survive$ python3
    ```Python 3.10.6 (main, May 29 2023, 11:10:38) [GCC 11.3.0] on linux
    ```Type "help", "copyright", "credits" or "license" for more information.
    ```>>> from roommate_app.models import User
    ```>>> u = User(username="Inco", email="inco@gmail.com", age=34, phone="678909345", country="Kenya", gender="F", ```budget=234567)
    ```>>> u
    ```<User Inco : Country Kenya>
    ```>>> print(u.email)
    ```inco@gmail.com
    ```>>> print(u.age)
    ```34
    ```>>> exit()

## Bugs

No bugs at the moment.

## Landing

The landing page link of this project can be found in <https://csasaka19.github.io/>

## Authors

Clive Sasaka - [Github](https://github.com/Csasaka19) / [Twitter](https://twitter.com/Sasaka_JR)

Helen Zeleke - [Github](https://github.com/93Helu)

&copy; 2023 Roommate To Survive - All Rights Reserved
