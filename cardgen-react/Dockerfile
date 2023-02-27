FROM nginx:1.21-alpine

FROM node:18 as build-stage

RUN mkdir -p /app
WORKDIR /app
# No need to move Nginx in its own folder, its better form if you leave it in the root of this "app" folder
# Therefore we need to adjust the COPY to hit the root folder we are currently in only]
# also since we are going to copy the entire folder anyway may as well do it now and not just the package.json
COPY . .
RUN npm ci
# Same thing as above we are already in the folder we want, we don't need to move around at all
RUN npm run build 
# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:1.23
# needed to remove the front slash on cardgen-react/build/ because it was already in the right folder
COPY --from=build-stage app/build/ /usr/share/nginx/html
# Removed the --from=build-stage because this isn't coming from the node docker image from step 0, but from the root folder in our project
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf