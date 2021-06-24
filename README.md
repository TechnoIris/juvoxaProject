# juvoxaProject
A hospital portal

This app provides a online interaction and helps keep track and fetching of records for the hospital, doctor and patient end user.
Please follow the instructions as follows.,

1.create a database called hospital in psql.

2.create user if not setup as follows[in terminal].,
sudo -u postgres psql
create role <username> superuser;
grant psql to <username>;

3. cd <folder_name> where main.py exists

4. Code Pre-Setup details.
i. provide postgresql details for SQLALCHEMY_DATABASE_URI in main.py file in the format "postgresql://<db_username>:<password>@localhost:5432/hospital"

5.Finally run these cmds in terminal.,
export FLASK_APP=main
flask db init
flask db migrate
flask db upgrade
flask run
