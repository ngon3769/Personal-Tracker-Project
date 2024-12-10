from database_models import Base, engine

if __name__ == "__main__":
    print("Creating database...")
    Base.metadata.create_all(engine)
    print("Database created successfully!")