# FastApi Authorization service

## Create Container Postgresql
```shell
docker-compose up -d
```

## Generate private and public key
```shell
openssl genrsa -out jwt-private.pem 2048
```

```shell
openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem
```

## Python
- Сreate and activate virtual enviroment
- Install dependencies
```shell
python3.10 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
```

## Alembiс migrations
```shell
alembic upgrade head
```

## Python
- Launching the application
```shell
python3.10 main.py
```