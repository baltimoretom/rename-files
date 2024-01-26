import os

folder_path = 'path/to/your/pdf/files'   # path to your folder

for filename in os.listdir(folder_path):
    if filename.startswith('modified_'):
        original_path = os.path.join(folder_path, filename)
        new_name = filename.replace('modified_', '')
        new_path = os.path.join(folder_path, new_name)
        os.rename(original_path, new_path)
