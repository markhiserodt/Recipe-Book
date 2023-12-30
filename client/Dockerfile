FROM node:latest as build

WORKDIR /client

COPY package.json ./

RUN npm install
RUN npm install -g @angular/cli

COPY . .

EXPOSE 4200

RUN ng build
CMD ng serve --host 0.0.0.0 --port 4200

# FROM node:latest as build

# WORKDIR /client

# COPY . .

# RUN npm install

# RUN npm run build

# FROM nginx:latest

# COPY --from=build ./dist /usr/share/nginx/html

# EXPOSE 80
