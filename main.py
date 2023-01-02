import os
from zipfile import ZipFile

__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# dank voor de eerder gegeven feedback. Het os.path.join is me nog niet geheel duidelijk. Iemand moet dan wel in de "winc" map aan hetw erk zijn toch?
# anders zegt python dat de map niet bestaat.

path_files = os.path.join(os.getcwd(), 'files')
path_cache = os.path.join(os.getcwd(), 'files', 'cache')
path_zipfile = os.path.join(os.getcwd(), 'files', 'data.zip')

# Part 1
def clean_cache():
    os.chdir(path_files) 
    if os.path.exists(path_cache):
        os.chdir(path_cache)
        for items in os.listdir():
            os.remove(items)
    else:
        os.mkdir(path_cache)
    return 



# Part 2
def cache_zip(path_zipfile, path_cache): 
    with ZipFile(path_zipfile, 'r') as zipobj:
        zipobj.extractall(path_cache)
    return 

# Part 3

def cached_files():
    filepath = []
    os.chdir(path_cache)
    for files in os.listdir():
        filepath.append(os.path.abspath(files))
    return filepath

# Part 4

def find_password(geheugen):
    for items in geheugen:
        with open(items, 'r') as inhoud:
            for l_no, line in enumerate(inhoud): # l_lo wordt niet gebruikt, maar als ik hem weghaal klopt de code niet....
                if 'password' in line:
                    begin = line.find(' ')
                    end = line.find("\\n")
                    final_password = line[begin+1:end]
                    print(final_password)
                    break
    return final_password


if __name__ == "__main__":
    clean_cache()           
    cache_zip(path_zipfile, path_cache)
    cached_files()
    find_password(cached_files())
