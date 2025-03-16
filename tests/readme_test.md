To run test of the project, first of all you need to run test_db_init.sql
to create a testing database.
and after that you need to run init.sql to create tables without data for tasting.
all data we will put automaticaly in the test and remove it after test ends.

To run test you need to run the following command:
 pytest tests

you  will see result of the test in terminal -  !pay attention!:
that you have a positive type of test and negative, that mean not every test will pass.
it's normal to have some test that will fail to check the negative scenario, like 
wrong data, wrong input, and other.
