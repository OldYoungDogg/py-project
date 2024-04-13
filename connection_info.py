from cryptography.fernet import Fernet

def encrypt_data(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

# Пример использования:
key = Fernet.generate_key()
connection_info = {
    "dbname":"postgres",
    "user":"postgres",#postgres
    "password":"Derek27042001",
    "host":"89.42.142.218",
    "port":"5432"
}

encrypted_data = encrypt_data(str(connection_info), key)

# Запись зашифрованных данных в файл
with open("connection_info.txt", "wb") as f:
    f.write(encrypted_data)
    
    
    
    
def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data.decode()

# Чтение зашифрованных данных из файла
with open("connection_info.txt", "rb") as f:
    encrypted_data = f.read()

# Дешифрование данных
decrypted_data = decrypt_data(encrypted_data, key)
connection_info = eval(decrypted_data)  # Преобразование строки обратно в словарь

# Пример использования данных подключения
print(connection_info["dbname"])
print(connection_info["user"])
print(connection_info["password"])
print(connection_info["host"])
print(connection_info["port"])
print("ключ 64бит, который вставить в код:",key.decode())


# И т.д.
