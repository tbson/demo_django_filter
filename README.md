# Demo django filter
## Setup
```
cd docker
./exec build
./exec up
./exec manage.py migrate
./exec manage.py article_seeding
./exec manage.py bserver
```
## Try
```
- http://localhost:4000/api/v1/article
- http://localhost:4000/api/v1/article?category__isnull=true
- http://localhost:4000/api/v1/article?category=1
- http://localhost:4000/api/v1/article?category_uid=uid_3
- http://localhost:4000/api/v1/article?ordering=id
- http://localhost:4000/api/v1/article?ordering=-id
- http://localhost:4000/api/v1/article?ordering=category
- http://localhost:4000/api/v1/article?ordering=-category
```
