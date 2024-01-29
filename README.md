## Start Here

Current folder flask_demo/api_demo

Navigate a folder up to flask_demo

cd .. 

## Example 1

```flask_demo> python3 api_demo/flask_01_simple_app.py

flask_demo> curl http://127.0.0.1:5001/items

api_demo> python3 -m unittest tests/test_02.py
```

## Example 2

```
flask_demo> python3 api_demo/flask_02_curd_app.py

http://127.0.0.1:5002/

http://127.0.0.1:5002/items

http://127.0.0.1:5002/items/2

curl -X POST -H "Content-Type: application/json" -d '{"name":"Item 3"}' http://127.0.0.1:5002/items

curl -X PUT -H "Content-Type: application/json" -d '{"name":"New Updated Item 3"}' http://127.0.0.1:5002/items/3

curl -X DELETE  http://127.0.0.1:5002/items/3

flask_demo> python3 -m unittest tests/test_02.py

```


## Example 3

```
python3 -r requirements.txt

flask_demo>python3 api_demo/flask_03_basic_auth_app.py

flask_demo>curl -X GET http://127.0.0.1:5003

flask_demo>curl -u 'gc1:pass1' http://127.0.0.1:5003/items

```

## Example 4

```

flask_demo>python3 api_demo/flask_04_jwt_auth_app.py

curl -X POST -H "Content-Type: application/json" -d '{"username":"user1", "password":"password1"}' http://127.0.0.1:5004/login


Token expires in 30 seconds

curl -X GET -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjU1NzkwMywianRpIjoiOTA3ZjAxYjYtMjJjNy00NTE0LWJhMmItNWY2MWU2ZmEzN2QxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXIxIiwibmJmIjoxNzA2NTU3OTAzLCJjc3JmIjoiN2E3M2VmODUtOGQwOC00MjliLWIwYTgtMTRmMzc0Y2VhY2Y2IiwiZXhwIjoxNzA2NTU3OTMzfQ.ZOav8uBkvjsHLjU3VxPEA6z9uMOVjREsKkuI5gLGOno" http://127.0.0.1:5004/items

```

## Example 5

```
flask_demo>python3 api_demo/flask_05_jwt_auth_swagger_app.py
```

Visit http://127.0.0.1:5005 to see different in screen


