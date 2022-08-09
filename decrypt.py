import pyAesCrypt
import os

# Функция шифрования файла
def decpryption(file, password):
    
    # указываем размер буфера
    buffer_size = 512 * 1024
    
    # вызываем метод расшифровки
    pyAesCrypt.encryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )
    
    # Вывод имя шифрованного файла на экран
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' расшифрован]")
    
    # удаляем исходный файл
    os.remove(file)
    
    
# Функция сканирования директорий
def walking_by_dirs(dir, password):
    
    # перебор всех поддиректорий в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        
        # если нахаодим файл - шифруем его
        if os.path.isfile(path):
            try:
                decpryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, повторяем цикл в поисках файла
        else:
            walking_by_dirs(path, password)
                
                
                
password = input("Введите пароль шифрования: ")
walking_by_dirs("", password)