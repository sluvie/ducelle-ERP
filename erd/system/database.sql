create user ducellesystem with password 'iamducellesystem';
alter role ducellesystem createdb;
create database ducellesystem_db with owner=ducellesystem;
grant all privileges on database ducellesystem_db to ducellesystem;
