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