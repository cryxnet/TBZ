I choose the [Docker Hub](https://hub.docker.com/) repository
1. Build image: `docker build -t <name> -f <filename> .`
2. Tag the image: `docker tag <name> <username>/<name>:<tag>`
3. Login: `docker login`
4. Push image: `docker push <username>/<name>:<tag>`