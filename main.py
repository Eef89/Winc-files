import os
from zipfile import ZipFile

__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Part 1
def clean_cache():
    os.chdir('/Users/evert/Documents/Winc/files')
    if os.path.exists('cache'):
        os.chdir('cache')
        for items in os.listdir():
            os.remove(items)
    else:
        os.mkdir('cache')
    return 

# Part 2
def cache_zip(zippie, zappie): 
    with ZipFile(zippie, 'r') as zipobj:
        zipobj.extractall(zappie)
    return 

# Part 3

def cached_files():
    path = '/Users/evert/Documents/Winc/files/cache'
    filepath = []
    os.chdir(path)
    for files in os.listdir():
        filepath.append(os.path.abspath(files))
    return filepath

# Part 4

def find_password(geheugen):
    for items in geheugen:
        with open(items, 'r') as inhoud:
            for l_no, line in enumerate(inhoud):
                if 'password' in line:
                    begin = line.find(' ')
                    end = line.find("\\n")
                    final_password = line[begin+1:end]
                    break
    return final_password

# Test scripts :-)

print(clean_cache())            
zipfile_path = '/Users/evert/Documents/Winc/files/data.zip'
cache_path = '/Users/evert/Documents/Winc/files/cache'
print(cache_zip(zipfile_path, cache_path))
print(cached_files())
print(find_password(cached_files()))
