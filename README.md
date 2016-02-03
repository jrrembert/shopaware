1. Clone directory
2. Setup virtualenv
3. Install requirements

```
$ pip install -r requirements.txt
```

4. Setup Postgres and PostGIS

```
$ brew install postgresql
$ brew install postgis
# Note: In Django 1.8+, you no longer have to run `CREATE EXTENSION postgis;`
#       as `migrate` takes care of this. Can still run manually if you wish.
$ initdb /usr/local/var/postgres
$ pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start &
$ createdb shopaware_db
```

5. Sync Django models

```
$ python manage.py migrate --run-syncdb
```
