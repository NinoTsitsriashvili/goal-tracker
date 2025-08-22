import os
import psycopg2
from dotenv import load_dotenv
import uuid

load_dotenv()

def create_user(email, password, first_name):
    # Generate unique ID
    user_id = str(uuid.uuid4())
    
    # Connect to database
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = conn.cursor()
    
    try:
        # INSERT statement here - you write this part
        # cursor.execute("INSERT INTO users ...")
        
        conn.commit()
        print(f"User {email} created successfully!")
        return user_id
        
    except Exception as e:
        print(f"Error creating user: {e}")
        return None
        
    finally:
        conn.close()

# Test it
create_user("test@example.com", "password123", "John")