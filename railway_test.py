import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Debug: Check what's being loaded
database_url = os.getenv("DATABASE_URL")
print(f"Database URL: {database_url}")

if database_url:
    try:
        conn = psycopg2.connect(database_url)
        print("✅ Railway connection successful!")
        conn.close()
    except Exception as e:
        print(f"❌ Connection failed: {e}")
else:
    print("❌ DATABASE_URL not found in environment variables")