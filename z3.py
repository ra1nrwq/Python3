import os
from datetime import datetime, timedelta

# Задание 1: Работа с датой и временем
def datetime_info(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        
        formatted_date = date_obj.strftime('%d-%m-%Y')
        
        day_of_week = date_obj.strftime('%A')
        
        next_year_start = datetime(date_obj.year + 1, 1, 1)
        days_until_next_year = (next_year_start - date_obj).days
        
        return {
            'formatted_date': formatted_date,
            'day_of_week': day_of_week,
            'days_until_next_year': days_until_next_year
        }
    except ValueError:
        return "Ошибка: введите дату в формате 'YYYY-MM-DD'."

# Задание 2: Чтение и запись в файл
def write_and_read_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        
        with open(filename, 'r') as file:
            return file.read()
    except IOError:
        return "Ошибка: не удалось выполнить операции с файлом."

# Задание 3: Работа с каталогами
def list_files_in_directory(directory_path):
    try:
        return [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    except FileNotFoundError:
        return "Ошибка: указанный каталог не найден."

# Задание 4: Проверка и создание каталогов
def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        return f"Каталог {directory_path} создан."
    else:
        return f"Каталог {directory_path} уже существует."

# Задание 5: Работа с мета-данными файлов
def file_stats(filepath):
    try:
        file_info = os.stat(filepath)
        
        last_modified = datetime.fromtimestamp(file_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')

        filename = os.path.basename(filepath)
        file_size = file_info.st_size
        name, extension = os.path.splitext(filename)
        
        return {
            'size': file_size,
            'last_modified': last_modified,
            'name': name,
            'extension': extension
        }
    except FileNotFoundError:
        return "Ошибка: указанный файл не найден."


def main():
    # Задание 1
    date_str = input("Введите дату в формате 'YYYY-MM-DD': ")
    print("Информация о дате:", datetime_info(date_str))

    # Задание 2
    filename = input("Введите имя файла для записи и чтения: ")
    content = input("Введите текст для записи в файл: ")
    print("Содержимое файла после записи:", write_and_read_file(filename, content))

    # Задание 3
    directory_path = input("Введите путь к каталогу: ")
    print("Список файлов в каталоге:", list_files_in_directory(directory_path))

    # Задание 4
    directory_path = input("Введите путь к каталогу для проверки: ")
    print(ensure_directory_exists(directory_path))

    # Задание 5
    filepath = input("Введите путь к файлу для получения мета-данных: ")
    print("Мета-данные файла:", file_stats(filepath))

main()
