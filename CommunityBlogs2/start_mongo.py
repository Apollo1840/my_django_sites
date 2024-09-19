import os
import subprocess


def start_mongo_service():
    # Path to store MongoDB data within your Django project
    mongo_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mongo_data')

    # Ensure the data directory exists
    if not os.path.exists(mongo_data_path):
        os.makedirs(mongo_data_path)

    # Command to start MongoDB, setting dbpath to the folder within your project
    mongo_command = [
        'mongod',
        '--dbpath', mongo_data_path,  # Use your project-specific directory for the database
        '--bind_ip', '127.0.0.1',  # Bind MongoDB to localhost
        '--port', '27017'  # Set the port for MongoDB
    ]

    try:
        # Start MongoDB as a subprocess
        mongo_process = subprocess.Popen(mongo_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Optionally, you can print out or log the output
        stdout, stderr = mongo_process.communicate()

        if mongo_process.returncode == 0:
            print("MongoDB started successfully.")
        else:
            print(f"Error starting MongoDB: {stderr.decode()}")

    except Exception as e:
        print(f"Failed to start MongoDB: {str(e)}")


if __name__ == "__main__":
    start_mongo_service()
