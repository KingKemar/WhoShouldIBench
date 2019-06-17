FROM node:10.9-slim

# not mandatory if you EXPORT a fixed port. See below.


WORKDIR /usr/wsib


EXPOSE 3000

USER node

COPY . .
# switch to npm if you chose it as package manager
CMD ["yarn", "serve"]
