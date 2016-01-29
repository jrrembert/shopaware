1. Clone directory
2. Setup virtualenv
3. Install requirements

```
$ pip install -r requirements.txt
```

4. Setup Postgres

```
$ brew install postgresql
$ initdb /usr/local/var/postgres
$ pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start &
$ createdb shopaware_db
```

5. Sync Django models

```
$ python manage.py migrate --run-syncdb
```
