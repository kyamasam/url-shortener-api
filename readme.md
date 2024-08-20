A url shortener in django and django rest

## How to use 
1. Create a virtual env 
2. Install deps using
    ```shell
   pip install -r reqirements.txt
   ```
3. Migrate db
    ```shell
   python manage.py migrate
   ```
4. Run server

   ```shell
   python manage.py runserver
   ```
   
5. Viewing apis
vist the url
http://localhost:8001/api/url-view/
a) To get shortened urls
GET
```
 /api/url-view/

```

b) To Shorten A Url
POST
```

{
    "short_code": "",
    "long_url": "",
    "visits_count": null,
    "is_expired": false
}

```

c) To get One url 

GET 

```
http://localhost:8001/api/url-view/W3NN/
```

Sample response

```json
{
    "id": 23,
    "short_code": "W3NN",
    "long_url": "https://youtube.com",
    "visits_count": 1,
    "created_at": "2024-08-20T07:39:19.179022Z",
    "is_expired": false
}
```