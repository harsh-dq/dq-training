FROM python:3.8

# set the working directory 
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .
RUN  pip install psycopg2-binary
# install dependencies
RUN pip install -r requirements.txt

# copy the source to working directory 
COPY . .

# command to run on container start
CMD [ "python", "./app.py" ]

