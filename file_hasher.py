import csv
import hashlib
import os
from datetime import datetime
import sys

#Creating argument for directory path:  file_hasher.py <directory>
path = sys.argv[1]

#Timestamp to use in file name to mark when evidence was hashed
timestamp = datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")

src_dir = sys.argv[1]

def file_hash_hex(file_path, hash_func):
    with open(file_path, 'rb') as f:
        return hash_func(f.read()).hexdigest()

def recursive_file_listing(base_dir):
    for directory, subdirs, files in os.walk(base_dir):
        for filename in files:
            yield directory, filename, os.path.join(directory, filename)

if __name__ == "__main__":

    with open('Evidence_Hashes_' + timestamp + '.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["File Name","Path","SHA256","SHA1","MD5"])
        for directory, filename, path in recursive_file_listing(src_dir):
            writer.writerow((filename,directory, file_hash_hex(path, hashlib.sha256),file_hash_hex(path, hashlib.sha1),file_hash_hex(path, hashlib.md5)))
