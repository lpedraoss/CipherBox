from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import os

class CipherBox:
    def __init__(self, vault_dir):
        self.vault_dir = vault_dir
        self.rsa_key_size = 2048  # Tamaño de la clave RSA

    def secure_pad(self, data):
        return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

    def secure_unpad(self, data):
        return data.rstrip(b"\0")

    # Método para generar y guardar claves RSA (pública y privada)
    def generate_rsa_keys(self, alias):
        key = RSA.generate(self.rsa_key_size)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        # Guardar la clave privada
        private_key_path = os.path.join(self.vault_dir, f"{alias}.private.key")
        with open(private_key_path, 'wb') as file:
            file.write(private_key)
        print(f"Clave privada RSA guardada en {private_key_path}.")

        # Guardar la clave pública
        public_key_path = os.path.join(self.vault_dir, f"{alias}.public.key")
        with open(public_key_path, 'wb') as file:
            file.write(public_key)
        print(f"Clave pública RSA guardada en {public_key_path}.")

        return public_key_path

    # Método para cifrar archivos con AES y RSA
    def lock_file(self, original_file, alias):
        # Generar claves RSA y guardarlas
        public_key_path = self.generate_rsa_keys(alias)
        
        # Cargar la clave pública RSA
        with open(public_key_path, 'rb') as file:
            public_key = RSA.import_key(file.read())

        aes_key = get_random_bytes(32)  # Clave AES-256
        iv = get_random_bytes(16)  # Vector de inicialización (IV)

        # Cifrar los datos con AES
        with open(original_file, 'rb') as file:
            data = file.read()

        cipher_aes = AES.new(aes_key, AES.MODE_CBC, iv)
        encrypted_data = cipher_aes.encrypt(self.secure_pad(data))

        # Guardar el archivo cifrado en .lock
        encrypted_file_path = os.path.join(self.vault_dir, f"{alias}.lock")
        with open(encrypted_file_path, 'wb') as file:
            file.write(iv + encrypted_data)
        print(f"Archivo {original_file} cifrado exitosamente en {encrypted_file_path}.")

        # Cifrar la clave AES con RSA
        cipher_rsa = PKCS1_OAEP.new(public_key)
        encrypted_aes_key = cipher_rsa.encrypt(aes_key)

        # Guardar la clave AES cifrada en .key
        aes_key_path = os.path.join(self.vault_dir, f"{alias}.key")
        with open(aes_key_path, 'wb') as file:
            file.write(encrypted_aes_key)
        print(f"Clave AES cifrada y guardada en {aes_key_path}.")

        # Crear un archivo .extinfo para almacenar información adicional y cifrarlo
        extinfo_content = f"Tipo de archivo original: {os.path.splitext(original_file)[1]}"
        cipher_aes_extinfo = AES.new(aes_key, AES.MODE_CBC, iv)
        encrypted_extinfo = cipher_aes_extinfo.encrypt(self.secure_pad(extinfo_content.encode()))

        extinfo_path = os.path.join(self.vault_dir, f"{alias}.extinfo")
        with open(extinfo_path, 'wb') as file:
            file.write(iv + encrypted_extinfo)
        print(f"Información de extensión cifrada guardada en {extinfo_path}.")

    # Método para descifrar archivos con AES y RSA
    def unlock_file(self, locked_file, alias):
        # Cargar la clave privada RSA
        private_key_path = locked_file.replace(".lock", ".private.key")
        with open(private_key_path, 'rb') as file:
            private_key = RSA.import_key(file.read())

        # Cargar la clave AES cifrada
        aes_key_path = locked_file.replace(".lock", ".key")
        with open(aes_key_path, 'rb') as file:
            encrypted_aes_key = file.read()

        # Descifrar la clave AES con RSA
        cipher_rsa = PKCS1_OAEP.new(private_key)
        aes_key = cipher_rsa.decrypt(encrypted_aes_key)

        # Cargar el archivo cifrado
        with open(locked_file, 'rb') as file:
            iv = file.read(16)  # Los primeros 16 bytes son el IV
            encrypted_data = file.read()

        # Descifrar los datos con AES
        cipher_aes = AES.new(aes_key, AES.MODE_CBC, iv)
        decrypted_data = self.secure_unpad(cipher_aes.decrypt(encrypted_data))

        # Descifrar y mostrar el contenido del archivo .extinfo
        extinfo_path = locked_file.replace(".lock", ".extinfo")
        with open(extinfo_path, 'rb') as file:
            iv = file.read(16)
            encrypted_extinfo = file.read()

        cipher_aes_extinfo = AES.new(aes_key, AES.MODE_CBC, iv)
        decrypted_extinfo = self.secure_unpad(cipher_aes_extinfo.decrypt(encrypted_extinfo))
        print(f"Información del archivo original: {decrypted_extinfo.decode()}")
        
        decrypted_file_path = os.path.join(self.vault_dir, f"{alias}.unlocked")
        with open(decrypted_file_path, 'wb') as file:
            file.write(decrypted_data)
        print(f"Archivo {locked_file} descifrado exitosamente en {decrypted_file_path}.")