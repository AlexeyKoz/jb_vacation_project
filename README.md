# jb_vacation_project
This is john bryce backend project on python and postgres database. Vacation management system with admin/regular user and likes and unlikes for vacations

project prerequisites:
1) create virtual environments by running command python -m venv venv 
2) activate virtual environments by running command venv\Scripts\activate in terminal.
3) install requirements by running command pip install -r requirements.txt in terminal.
4) Connect to database 
  * recommended use extension like postgres for vscode to make direct connection within the IDE.
5) run project_db_init.sql under src folder to create database
6) run init.sql under src folder and choose project_db for database to create tables and necessary data in database
recommended: run main_project_exe.py if you wish to try project features

testing prerequisites:
1) run test_db_init.sql under tests folder to create database
2) run init.sql and choose test_db for database to create tables and necessary roles data for database
3) run main.py file under jb_project_vacation main folder to run pytest testing


expected result:
7 pass
7 fails
total: 14 tests
(like and unlike tests have been merged to one hence the reduced amount of tests)