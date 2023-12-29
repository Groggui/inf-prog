import os
import shutil


class FileManager:
    def __init__(self, current_directory):
        self.current_directory = current_directory

    def view_directory(self):
        file_list = os.listdir(self.current_directory)
        for file in file_list:
            print(file)

    def create_directory(self, directory_name):
        new_directory = os.path.join(self.current_directory, directory_name)
        os.mkdir(new_directory)

    def delete(self, item_path):
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            print("Пуи существует или не является файлом")

    def copy(self, source_path, destination_path):
        if os.path.isfile(source_path):
            shutil.copy2(source_path, destination_path)
        elif os.path.isdir(source_path):
            shutil.copytree(source_path, destination_path)
        else:
            print("Пути не существует или не является файлом")

    def move(self, source_path, destination_path):
        shutil.move(source_path, destination_path)

    def search_file(self, filename):
        for root, dirs, files in os.walk(self.current_directory):
            if filename in files:
                return os.path.join(root, filename)
        print("Не найдено")

    def change_permission(self, item_path, permission):
        os.chmod(item_path, permission)

q = FileManager(current_directory=r'C:\Users\username\PycharmProjects\q')