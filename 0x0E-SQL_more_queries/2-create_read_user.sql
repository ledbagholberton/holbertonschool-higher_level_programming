-- createss database and user
-- creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates user
CREATE USER IF NOT EXISTS user_0d_2@localhost;
-- create pswd
SET PASSWORD FOR user_0d_2@localhost = "user_0d_2_pwd";
-- grant privileges select
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
-- flush privileges
FLUSH PRIVILEGES;
