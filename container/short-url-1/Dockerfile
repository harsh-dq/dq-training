FROM node:14-alpine


LABEL maintainer="hasharma@deqode.com"
LABEL org.label-schema.schema-version="1.0"

LABEL description="This is a Node.JS web application powered by Express that provides the main functionality that you'd expect from a URL Shortener service"

# Create and set applicarion directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
# Copy Package.json
COPY package*.json ./

# Installing Dependencies 
RUN npm install -d
# If you are building your code for production
# RUN npm ci --only=production

# Coppying  app source
COPY . .

# Exposing port for container
EXPOSE 5000

CMD [ "node", "app.js" ]