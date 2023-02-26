FROM nginx:1.21-alpine

FROM tiangolo/node-frontend:10 as build-stage

WORKDIR /cardgen-build/
COPY cardgen-react/package*.json .
RUN npm install
COPY ./ /cardgen-react/
RUN npm run build 
# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:1.15
COPY --from=build-stage /cardgen-react/build/ /usr/share/nginx/html
# Copy the default nginx.conf provided by tiangolo/node-frontend
COPY --from=build-stage /nginx.conf /etc/nginx/conf.d/default.conf