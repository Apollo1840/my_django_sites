from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, AutoReconnect


def stop_mongo_service():
    try:
        # Connect to MongoDB (set a short timeout to avoid long waits)
        client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)

        # Access the admin database
        admin_db = client.admin

        # Issue the shutdown command
        admin_db.command('shutdown')

    except AutoReconnect as e:
        # AutoReconnect is expected because the server shuts down and closes the connection
        if 'connection closed' in str(e):
            print("MongoDB service stopped successfully.")
        else:
            print(f"Unexpected error: {e}")

    except ServerSelectionTimeoutError:
        # This occurs if MongoDB is unreachable (e.g., already stopped)
        print("Could not connect to MongoDB. Is it already stopped?")

    except Exception as e:
        # Other errors
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    stop_mongo_service()
