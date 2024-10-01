from pymongo_get_database import get_database
dbname = get_database()
collection_name = dbname["starting_questions"]