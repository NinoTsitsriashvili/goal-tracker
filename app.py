import sqlite3
import uuid
from datetime import datetime

def create_user(email, password, first_name):
    # Generate unique ID
    user_id = str(uuid.uuid4())
    
    # Connect to database
    conn = sqlite3.connect('savings.db')
    cursor = conn.cursor()
    
    try:
        # Insert user into database
        cursor.execute('''
            INSERT INTO users (id, email, password_hash, first_name)
            VALUES (?, ?, ?, ?)
        ''', (user_id, email, password, first_name))
        
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