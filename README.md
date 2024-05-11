# Deduplicator

This Python script is designed to find and delete duplicate .mp3 or .mp4 files in a specified directory. The script identifies duplicates based on their MD5 hash, which is a widely used cryptographic hash function that produces a 128-bit (16-byte) hash value. It is commonly used to verify data integrity.

## How It Works

The script works by walking through the specified directory and its subdirectories, calculating an MD5 hash for each .mp3 or .mp4 file, and storing the hashes in a dictionary. If it encounters a file with a hash that's already in the dictionary, it deletes the file.

The script uses the os and hashlib libraries to traverse the directory, calculate the hashes, and delete duplicate files.

## Usage

To use the script, simply run it with Python and it will automatically start checking for duplicate files in the specified directory. The directory is hardcoded in the script, so you'll need to modify the script to specify the directory you want to check.

The script prints out a message for each duplicate file it finds and deletes, and it prints out a "Deduplication Completed" message when it has finished checking the entire directory.

## Important Note

This script deletes files permanently. It's recommended to test this script on a backup or dummy data before using it on important files. Always ensure you have a backup of your data before running any script that modifies or deletes files.
