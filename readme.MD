# EDC Server

## General Server connection params
This is Jubaan's EDC server, connection params:
~~~
admin: jubaanedc
psw: Tuduxy@2O25
dns: oedc.gixam.com
port for ssh: 2225
ssh command: ssh  -p 2225 jubaanedc@oedc.gixam.com

Server is backed-up in Azure under a backup service vault: "edc-backup"
1. every day at 4:00 UTC
2. retention for 30 days
~~~

## mail credentials
user: gixaminfo@jubaan.com
psw: ItsG00dT0BeH0me!23

## Postgres connection params
~~~
postgres 16 (running on docekr "supabase-db")
    dbname = "postgres"
    user = "postgres.your-tenant-id"
    password = "R3vyPCrVN0sMYdklJ2Rp13Y5"
    host = "localhost"
    port = "5461"
~~~
## NGINX configuration
~~~
location of config file:  /etc/nginx/sites-available/reverse-proxy
ssl for: oedc.gixam.com, oedc-db.gixam.com
certificates location:  /etc/letsencrypt/live/
~~~

## OEDC server environment configuration
~~~
cd OpenEDC-Server
sudo nano .env
~~~
### restarting the OEDC server
~~~
docker compose down && docker compose up --build --detach
~~~

## docker commands and info
|command|what it does|
|-------|------------|
|docker ps| shows all running docker images|
|docker exec -it supabase-db bash| to get into the database running image|
|/var/lib/postgresql/data/|location of data on the database in the docker|
|nano /var/lib/postgresql/data/postgresql.conf| configuring the postgres in the docker|
|nano /var/lib/postgresql/data/pg_hba.conf|configuring postgres network|
|exit|exit from the docker hosting|
|docker restart supabase-db|to restart the docker after changes|


## following is a list of test applications
~~~
location: /home/jubaanedc/projects/pconfig
python env: pconfig
~~~

|application|testing what|
|-----------|------------|
|welcome.py|check to see that the python virtual environment works|
|psql.py|testing basic sql execution to the internal postgres sql running in the supbase-db docker|
|mail.py|testing mail SMTP sending test anf HTML options|