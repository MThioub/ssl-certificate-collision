import os

def check_source():
    REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    zmap_output_file = os.path.join(REPO_DIR, 'data/results.csv')

    if not os.path.exists(zmap_output_file):
        print("create file")
        os.system('sudo zmap/src/zmap -B 10M -p 80 -n 10000 -o data/results.csv')

    print("file already exists")
    return 0
