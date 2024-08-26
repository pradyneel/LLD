class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        # Imagine if this is a database Connection
        self.connection = self._create_connection()
    
    def _create_connection(self):
        # Simulate a database connection
        return "Database connection established"
    
    def query(self, sql: str):
        # Simulate a database query
        return f"Executing query: {sql}"

# Client code
if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    print(db1.query("SELECT * FROM users"))
    print(db2.query("SELECT * FROM orders"))

    # Check if both instances are the same
    print(f"db1 is db2: {db1 is db2}")