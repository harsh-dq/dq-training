
# Python Deqode Task 1

### "Create a microservice serving REST API with GET calls returning 100 records starting from the newest JSON format with pagination Add a post call as well to add a record, connect with a Postgres DB Use Python or GoLang"


## Run App

1. Make sure you have `postgres` Database connection  or run it using docker using following command

```shell 
docker run -d -p 5433:5432 -e POSTGRES_PASSWORD=password  -e POSTGRES_DB=pythondb --name postgres postgres
```
2. Set ENV `DATABASE_URL` to  `postgres://<user>:<password>@localhost:5432/pythondb` in `.env` file

3. Create Table in Database using `create_table.py` script by following command

```shell
python3 create_table.py
```

4. Finaly you can run app by using follwing command

```shell
python3 app.py
```


## Run And Deploy using `docker-compose.yaml`

```shell
docker-compose up -d
```






## Extra Things Done For this Projects 

1. Pg Admin ( For Data visualization)





