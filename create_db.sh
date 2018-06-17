#!/bin/bash

dropdb --if-exists northwind
dropuser --if-exists northwind_user
createuser northwind_user

createdb northwind --owner=northwind_user
psql northwind --user=northwind_user < northwind.sql

psql template1 -c "alter user northwind_user password 'thewindisblowing';"
psql template1 -c "grant all on DATABASE northwind to northwind_user;"
psql northwind -c "GRANT ALL on ALL tables IN SCHEMA public to northwind_user"
