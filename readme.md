**Summary**:

It is written to retrieve navigation data for the last 48 hours for each vehicle using Django Framework and PostgreSQL.
For the cost problem that will arise due to frequent queries mentioned in the problem (`N+1 select problem`), The data 
requested from the table connected with the foreign key with `"select_related"` in Django ORM is retrieved with a single query.

**Steps**:

1- Run `sudo apt-get install docker` command

2- Run `sudo apt-get install docker-compose` command

3- Run `sudo docker-compose up -d --build` command when at LastPoints directory.

4- Run `curl http://0.0.0.0:8081/home/` command or get http://0.0.0.0:8081/home/ on your browser and see the result of 
last 48 hours navigaton data for each vehicle.

5- You can view tables with pgAdmin if you want. Get http://0.0.0.0:5050/ on your browser and login with credentialds 
from env/dev.env file. Then create server, you can find db's network ip `lastpoints_db_1` container's network settings 
and also credentials in env/dev.env file.
