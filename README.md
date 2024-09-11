
# Sistema de Cifrado Híbrido Brosgor (AES-256 + RSA)

Este proyecto es un sistema de cifrado híbrido que combina cifrado simétrico (AES-256) y cifrado asimétrico (RSA) para proteger archivos. Utiliza la librería `PyCryptodome` para implementar la criptografía y proporciona una interfaz de línea de comandos (CLI) sencilla para cifrar y descifrar archivos.

## Descripción del proyecto

El sistema permite:

- **Cifrar archivos**: Los archivos se cifran con una clave AES-256 generada aleatoriamente. La clave AES se cifra utilizando RSA con claves públicas y privadas generadas dinámicamente. El archivo cifrado resultante tiene la extensión `.lock`, mientras que la clave AES cifrada se guarda en un archivo con la extensión `.key`.
- **Descifrar archivos**: Utilizando la clave privada RSA, el sistema descifra la clave AES y luego descifra el archivo original, devolviéndolo a su formato original.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- PyCryptodome

Puedes instalar las dependencias con el siguiente comando, usando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/lpedraoss/CipherBox.git
cd cipherbox
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Linux/MacOS
venv\Scripts\activate  # En Windows
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

### Cifrar un archivo

1. Coloca los archivos que deseas cifrar en la carpeta `central`.
2. Ejecuta el programa:

```bash
python main.py
```

3. Selecciona la opción **"1. Cifrar un archivo"** y sigue las instrucciones en pantalla para elegir un archivo y especificar un alias para las claves y archivos cifrados.

### Descifrar un archivo

1. Ejecuta el programa:

```bash
python main.py
```

2. Selecciona la opción **"2. Descifrar un archivo"** y elige el archivo `.lock` que deseas descifrar.

### Limpiar la consola

El programa limpiará automáticamente la consola según el sistema operativo que utilices:

- **Windows**: Utiliza `cls`.
- **Linux/MacOS**: Utiliza `clear`.

## Archivos generados

El programa generará varios archivos:

- `.lock`: El archivo cifrado.
- `.key`: La clave AES cifrada con RSA.
- `.extinfo`: Información adicional cifrada, como la extensión original del archivo.
- `.private.key`: La clave privada RSA.
- `.public.key`: La clave pública RSA.

## Dependencias

Asegúrate de tener las siguientes dependencias en el archivo `requirements.txt`:

```
pycryptodome
```

## Archivo `requirements.txt`

Asegúrate de tener este contenido en tu archivo `requirements.txt`:

```plaintext
pycryptodome
```

## Uso del Entorno Virtual

Para crear y activar un entorno virtual, sigue estos pasos:

1. Crea el entorno virtual:

```bash
python -m venv venv
```

2. Activa el entorno virtual:

- En Linux/MacOS:

```bash
source venv/bin/activate
```

- En Windows:

```bash
venv\Scripts\activate
```

3. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

## Contribución

Si deseas contribuir a este proyecto, puedes hacer un fork del repositorio y enviar un pull request con tus mejoras.


