import psycopg2
from psycopg2 import Error
from config import * 


def get_connexion():
    try:
        con = psycopg2.connect(
            dbname = DATABASE, 
            user = USER, 
            password = PASSWORD, 
            host = HOST, 
            port = PORT
        )
        return con
    except Error: 
        print("Erreur de connexion")

def close_connexion(con): 
    try: 
        con.close()
        print("Fermuture de la connexion ")
    except Error: 
        print("Erreur de Fermuture ")

def get_users(con): 
    cur = con.cursor()
    requete = "select * from users"
    cur.execute(requete)
    users = cur.fetchall()
    return users 


if __name__ == "__main__": 
    con = get_connexion()
    print(get_users(con))
    close_connexion(con)


