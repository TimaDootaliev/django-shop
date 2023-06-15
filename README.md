# Setup

Create file ".env.prod" and fill it with your own data like in ".env.template" file

## How to run

```bash
docker-compose up

docker-compose exec web python3 manage.py migrate && python3 manage.py collectstatic --no-input
```

