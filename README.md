## Start Here

- If you have not installed **git**, 
  
    Windows https://gitforwindows.org/

    MAC users ```brew install git```

- Create a new folder (Example: demo) in your machine

```
git clone https://github.com/gchandra10/flask_demo.git

cd flask_demo
```

- python3 -r requirements.txt
- Rename the config_template.yaml to config.yaml
- Substitute it with your MySQL details. (needed for Example 6 only)
- Open VSCode and open flask_demo folder.


## Example 1

```
flask_demo> python3 api_demo/flask_01_simple_app.py
```

### Browser

Open browser and navigate to http://127.0.0.1:5001/items

### CLI

```
flask_demo> curl http://127.0.0.1:5001/items
```

### Unit Test

```
flask_demo> python3 -m unittest tests/test_01.py
```

## Example 2

```
flask_demo> python3 api_demo/flask_02_crud_app.py
```

### Browser

http://127.0.0.1:5002/

http://127.0.0.1:5002/items

http://127.0.0.1:5002/items/2

### CLI

```
flask_demo> curl -X POST -H "Content-Type: application/json" -d '{"name":"Item 3"}' http://127.0.0.1:5002/items

flask_demo> curl -X PUT -H "Content-Type: application/json" -d '{"name":"New Updated Item 3"}' http://127.0.0.1:5002/items/3

flask_demo> curl -X DELETE  http://127.0.0.1:5002/items/3
```

### Unit Test

```
flask_demo> python3 -m unittest tests/test_02.py
```


## Example 3

```
python3 -r requirements.txt

flask_demo>python3 api_demo/flask_03_basic_auth_app.py
```

### CLI

```
flask_demo>curl -X GET http://127.0.0.1:5003

flask_demo>curl -u 'gc1:pass1' http://127.0.0.1:5003/items
```

### Unit Test

```
flask_demo> python3 -m unittest tests/test_03.py
```

## Example 4

```
flask_demo>python3 api_demo/flask_04_jwt_auth_app.py
```

### CLI

```
curl -X POST -H "Content-Type: application/json" -d '{"username":"user1", "password":"password1"}' http://127.0.0.1:5004/login
```

**Copy the token after access_token and use it as given below.**

*This token expires in 30 seconds*

```
curl -X GET -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjU1NzkwMywianRpIjoiOTA3ZjAxYjYtMjJjNy00NTE0LWJhMmItNWY2MWU2ZmEzN2QxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXIxIiwibmJmIjoxNzA2NTU3OTAzLCJjc3JmIjoiN2E3M2VmODUtOGQwOC00MjliLWIwYTgtMTRmMzc0Y2VhY2Y2IiwiZXhwIjoxNzA2NTU3OTMzfQ.ZOav8uBkvjsHLjU3VxPEA6z9uMOVjREsKkuI5gLGOno" http://127.0.0.1:5004/items

```

## Example 5

```
flask_demo>python3 api_demo/flask_05_jwt_auth_swagger_app.py
```
### Browser

Visit http://127.0.0.1:5005 to see different in screen

## Example 6

Remember to update config.yaml with your credentials

Get sakila-data-02.sql and sakila-schema-01.sql from this.

https://github.com/gchandra10/sakila_schema_data_mysql

```
flask_demo> python3 api_demo/flask_06_mysql_app.py
```