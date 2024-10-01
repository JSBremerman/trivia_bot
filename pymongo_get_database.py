from pymongo import MongoClient
def get_database():
    CONNECTION_STRING = "mongodb+srv://user:pass@cluster.mongodb.net/triviaBot"
    client = MongoClient(CONNECTION_STRING)
    return client['questions']

if __name__ == "__main__":
    dbname = get_database()