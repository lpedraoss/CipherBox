# Usar la imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de dependencias primero para aprovechar la caché de Docker
COPY requirements.txt .

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos del proyecto
COPY . .

# Copiar las carpetas 'data' y 'central' si son necesarias
COPY data /app/data
COPY central /app/central

# Comando por defecto para ejecutar el programa
CMD ["python", "main.py"]
