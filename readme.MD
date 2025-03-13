# EDC Server

This is Jubaan's EDC server, connection params:
~~~
admin: jubaanedc
psw: **************
dns: edc.gixam.com
https: via NGIX, /etc/nginx/sites-available/openedc
postgres 16, admin: postgres
~~~

## following is a list of test applications

|application|testing what|
|-----------|------------|
|psql.py|testing basic sql execution to the internal postgres sql|
|mail.py|testing mail SMTP sending test anf HTML options|