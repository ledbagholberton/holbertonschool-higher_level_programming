-- creates a mysql user with conditions
-- CREATE user IF NOT EXISTS
CREATE USER IF NOT EXISTS user_0d_1@localhost;
-- SET password
SET PASSWORD FOR user_0d_1@localhost = "user_0d_1_pwd";
-- GRANT all privileges
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
-- Apply privileges
FLUSH PRIVILEGES;
