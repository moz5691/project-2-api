# Project 2 API

## Endpoints
![](img/api_screenshot.png)


## Instruction
### Using CLI (no docker)
* First, provision your own Postgres Database.

```sh

  $ python3 -m venv env
  $ source env/bin/activate
  $ pip install requirements.txt

  (env)$ export FLASK_APP=project/__init__.py
  (env)$ export FLASK_ENV=development
  (env)$ export DATABASE_URL=<postgres://username:password@host_uri:port/database_name>
  (env)$ python manage.py run
```


### Using Docker

```sh
  # build and run docker container
  $ docker-compose up -d --build
  # check if it runs with no errors
  $ docker-compose logs
  # recreate PostgreSQL db
  $ docker-compose exec apps python manage.py recreate_db
  # seed 1st dataset, geocode 
  $ docker-compose exec apps python manage.py seed_db1
  # seed 2nd dataset, athletes
  $ docker-compose exec apps python manage.py seed_db2
   # seed 3rd dataset, celebrities
  $ docker-compose exec apps python manage.py seed_db3
  # Pytest
  $ docker-compose exec apps python -m pytest 'project/tests'  
```

* PostgreSQL url path looks like this

  ```sh
  'postgres://username:password@<host_uri>:5432/dbname'
  ```

* Using Docker, <host_uri> is host name in docker-compose.yml.  In this code, 'dataset-db' is <host_uri>.

```sh
# Dockercompose.yml
...
...
    dataset-db:  
      build:
        context: ./project/db
        dockerfile: Dockerfile
      expose:
        - 5432
      environment:
        - POSTGRES_USER=postgres
        - POSTGRES_PASSWORD=postgres
```

### Heroku Deployment

* Create Heroku App
```sh
  $ heroku create  
  Creating app... done, ⬢ <app_name>
  https://<app_name>.herokuapp.com/ | https://git.heroku.com/<app_name>.git
```
* Login to Heroku container
```sh
  $ heroku container:login
```
* Provision a Postgres database, free tier.
```sh
  $ heroku addons:create heroku-postgresql:hobby-dev -a <app_name>
```
* Build a production image and tag it
```sh
  $ docker build -f Dockerfile.prod -t registry.heroku.com/<app_name>/web .
```

* Grab Postgres database URI & set it locally.  Heroku will take it locally set it to the application ENV.  

```sh
  $ heroku container:release web -a <app_name> 
  # returns 
  postgres://username:password@<db_host>:5432/<db_name>

  $ export DATABASE_URL=postgres://username:password@<db_host>:5432/<db_name>
```

* Set up container locally to test (optional)
```sh
  $ docker run --name <tag> -e "PORT=8765" -p 5002:8765 registry.heroku.com/<app_name>/web:latest

  [2020-06-27 15:11:23 +0000] [1] [INFO] Starting gunicorn 20.0.4
  [2020-06-27 15:11:23 +0000] [1] [INFO] Listening at: http://0.0.0.0:8765 (1)
  [2020-06-27 15:11:23 +0000] [1] [INFO] Using worker: sync
  [2020-06-27 15:11:23 +0000] [7] [INFO] Booting worker with pid: 7
```

* Check "http://localhost:5002/doc" and "http://localhost:5002/api/v1/ping".  Check both works.

* Remove local container if you don't use it.

```sh
  $ docker rm <tag>
```

* Push the docker image to Heroku Docker registry.

```sh
  $ docker push registry.heroku.com/<app_name>/web:latest
```

* Release the pushed image.  
```sh
  $ heroku container:release web -a <app_name>
```
* Check "https://<app_name>.herokuapp.com/doc" and "https://<app_name>.herokuapp.com/api/v1/ping"

* Create database and seeding data.
```sh
# drop all tables and recreate
$ heroku run python manage.py recreate_db -a <app_name>
# seed geocode table
$ heroku run python manage.py seed_db1 -a <app_name>
# seed athletes table
$ heroku run python manage.py seed_db1 -a <app_name>
# seed celebrities table
$ heroku run python manage.py seed_db2 -a <app_name>
```
* END


