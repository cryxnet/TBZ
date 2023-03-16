# Using Ubuntu as Docker Image
FROM ubuntu:latest as base

# Identify the maintainer of an image
LABEL maintainer="cryxnet"

# Base installation
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install postgresql postgresql-contrib

# Building stage
FROM base as builder

# Create a PostgreSQL user and database
RUN postgresql start && \
    postgres psql -c "CREATE USER myuser WITH PASSWORD 'mypassword';" && \
    postgres createdb -O myuser mydatabase

# Expose the PostgreSQL port
EXPOSE 5432

# Production stage
FROM builder as prod

# Start the PostgreSQL service
CMD ["service", "postgresql", "start"]