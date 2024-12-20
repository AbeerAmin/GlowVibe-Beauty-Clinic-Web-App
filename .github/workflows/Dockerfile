# Use a base image with Node.js
FROM node:20-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package files and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the port your application runs on
EXPOSE 3000

# Command to start the application
CMD ["npm", "start"]
