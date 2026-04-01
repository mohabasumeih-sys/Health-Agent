import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    print("Missing SUPABASE_URL or SUPABASE_KEY in .env")
    exit(1)

supabase = create_client(url, key)

tables = ["users", "chat_sessions", "chat_messages"]
for table in tables:
    try:
        response = supabase.table(table).select("count", count="exact").limit(1).execute()
        print(f"Table '{table}' exists.")
    except Exception as e:
        print(f"Table '{table}' does NOT exist or error: {e}")
