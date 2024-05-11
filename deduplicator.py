import os
import hashlib

# Calculat eht hash value of the different files in the directory


def calculate_hash(file_path, block_size=65536):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            hasher.update(block)
    return hasher.hexdigest()

# Find and delete the duplicates in the directory


def find_and_delete_duplicates(directory_path):
    file_hashes = {}
    deleteCount = 0
    for folder, subfolders, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(folder, file)
            if file.endswith('.mp3') or file.endswith('.mp4'):
                file_hash = calculate_hash(file_path)
                if file_hash in file_hashes:
                    print(
                        f'Duplicate found: {file} and {file_hashes[file_hash]}')
                    os.remove(file_path)
                    print(f'Deleted: {file_path}')
                    deleteCount += 1
                else:
                    file_hashes[file_hash] = file_path
    # print the deleteCount along with a string showing number of deleted files
    print(f"The Deleted Files are: {deleteCount}")


# Invoke the "find_and_delete_duplicates" function
find_and_delete_duplicates(
    r'C:\Users\Olatunji Olayinka\Desktop\YinkaVitulaFlashReplica')

# Print the String "Deduplication Completed to the Screen"
print(f'Deduplication Completed...')
