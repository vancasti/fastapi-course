# Nombre del servicio en docker-compose (opcional)
SERVICE=app

# Construye las imágenes y levanta los servicios en segundo plano
up:
	docker-compose up

# Construye las imágenes sin usar la cache
build:
	docker-compose build --no-cache

# Detiene los servicios
down:
	docker-compose down

# Reinicia los servicios (es útil para ver cambios rápidamente)
restart:
	docker-compose restart $(SERVICE)

# Muestra los logs del servicio especificado
logs:
	docker-compose logs -f $(SERVICE)

# Ejecuta un shell dentro del contenedor especificado
shell:
	docker-compose exec $(SERVICE) /bin/sh

# Limpia los contenedores, imágenes y volúmenes no usados
clean:
	docker-compose down -v --rmi all --remove-orphans

# Lista los contenedores activos
ps:
	docker-compose ps