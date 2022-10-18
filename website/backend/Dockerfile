FROM node:current-alpine

RUN mkdir -p /backend

WORKDIR /backend

COPY ./package.json .

RUN npm install

COPY . .

EXPOSE 3665

CMD ["npm", "run", "devStart"]
