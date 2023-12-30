# FROM node:latest as build

# WORKDIR /client

# COPY package.json ./

# RUN npm install
# RUN npm install -g @angular/cli

# COPY . .

# EXPOSE 4200

# RUN ng build
# CMD ng serve --host 0.0.0.0 --port 4200

FROM node:20-alpine as build

WORKDIR /client

COPY package*.json .

RUN npm ci

COPY . .

RUN npm run build


FROM nginx:alpine

COPY --from=build /client/dist/browser /usr/share/nginx/html

EXPOSE 80
