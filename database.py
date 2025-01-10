import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """Establish a database connection."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Successfully connected to the database")
        except Error as e:
            print(f"Error: {e}")
            self.connection = None  # Ensure connection is None on failure

    def close(self):
        """Close the database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")
        else:
            print("No connection to close")

    def execute_query(self, query):
        """Execute a single query."""
        if self.connection is None:
            print("No connection established. Cannot execute query.")
            return
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error: {e}")

    def fetch_all(self, query):
        """Fetch all results from a query."""
        if self.connection is None:
            print("No connection established. Cannot fetch results.")
            return []
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

# Example usage
if __name__ == "__main__":
    db = Database(host='localhost', user='dkb096', password='subzero', database='hospital_management');
    db.connect()
    # Example query execution
    # db.execute_query("YOUR SQL QUERY HERE")
    db.close()
