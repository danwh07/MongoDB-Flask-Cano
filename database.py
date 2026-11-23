from pymongo import MongoClient
import certifi

ca = certifi.where()
MONGO_URI = "mongodb+srv://daniacano_db_user:4dXR7SQ8ta01NC5J@cluster0.zruodre.mongodb.net/"
def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client['dbproductosapp']
    except ConnectionError:
        print("Error de conexión con la base de datos")

    return db
