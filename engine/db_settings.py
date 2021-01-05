import os

DATABASES = {
        'database': os.getenv("DB_NAME"),
        'user': os.getenv("DB_USER"),
        'password': os.getenv("DB_PASSWORD"),
        'host': os.getenv("DB_HOST"),
        'port': os.getenv("DB_PORT"),
}
<<<<<<< HEAD
print(DATABASES)
=======
>>>>>>> e00b8695f8a814c4c69788750ba08932a2071aad
