# Library django 
## Project deploy dev
```bash
docker-compose build
docker-compose up -d
```
## Project deploy prod
```bash
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml up -d
```
### Go to the bash of the container
```bash
docker exec -it <container name> bash
```
### Execute manage.py script
```bash
docker exec -it <container name> python manage.py <script>
```