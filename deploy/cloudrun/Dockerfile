FROM node:24-alpine
WORKDIR /app/backend
COPY backend/package.json backend/package-lock.json ./
RUN npm ci --omit=dev --ignore-scripts && npm cache clean --force
COPY backend/*.js ./
COPY layout.html /app/site/layout.html
COPY public/ /app/dist/
USER node
EXPOSE 8080
CMD ["node", "server.js"]
