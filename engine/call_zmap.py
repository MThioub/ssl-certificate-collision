
<<<<<<< HEAD

<<<<<<< HEAD
@import os
=======
import os 
>>>>>>> e00b8695f8a814c4c69788750ba08932a2071aad
=======
import os
>>>>>>> develop

def check_source():
    REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    zmap_output_file = os.path.join(REPO_DIR, 'data/results.csv')

    if not os.path.exists(zmap_output_file):
        print("create file")
        os.system('sudo zmap/src/zmap -B 10M -p 80 -n 10000 -o data/results.csv')

    print("file already exists")
    return 0
<<<<<<< HEAD
=======


>>>>>>> e00b8695f8a814c4c69788750ba08932a2071aad
