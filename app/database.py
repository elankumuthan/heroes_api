from sqlmodel import SQLModel, Session, create_engine
from app.models import Hero  # Import the Hero model
from sqlalchemy import text
import os

# Database connection setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Gets the absolute path of the script
sqlite_file_name = os.path.join(BASE_DIR, "heros.db")  # Uses absolute path

sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

# Function to create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    insert_initial_data()

# Function to insert predefined heroes if the table is empty

def insert_initial_data():
    with Session(engine) as session:
        # Execute the count query
        result = session.exec(text("SELECT COUNT(*) FROM hero"))
        row = result.first()  # Fetch the first row **only once**
        count = row[0] if row else 0  # Extract count safely

        if count > 0:
            return  # Skip inserting data if already present

        # Predefined heroes
        heroes = [
            Hero(name="Superman", age=35, secret_power="Flight", gender="Male", real_name="Clark Kent"),
            Hero(name="Batman", age=40, secret_power="Genius", gender="Male", real_name="Bruce Wayne"),
            Hero(name="Wonder Woman", age=5000, secret_power="Super Strength", gender="Female", real_name="Diana Prince"),
            Hero(name="Iron Man", age=45, secret_power="Advanced Armor", gender="Male", real_name="Tony Stark"),
            Hero(name="Spider-Man", age=18, secret_power="Wall Climbing", gender="Male", real_name="Peter Parker"),
        ]

        session.add_all(heroes)
        session.commit()


# Dependency to get a session
def get_session():
    with Session(engine) as session:
        yield session
