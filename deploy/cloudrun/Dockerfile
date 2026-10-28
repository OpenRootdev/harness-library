FROM nginx/nginx-unprivileged@sha256:969ccb55136a85056874e579908584bc0a39217a72ebf819a4ef4f44a62c9dda
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY public/ /usr/share/nginx/html/
EXPOSE 8080
