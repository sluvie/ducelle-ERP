create user ducellehr with password 'iamducellehr';
alter role ducellehr createdb;
create database ducellehr_db with owner=ducellehr;
grant all privileges on database ducellehr_db to ducellehr;
