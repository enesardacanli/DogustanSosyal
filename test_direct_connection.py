"""
Direct MongoDB Connection Test
Tests the connection string directly without Django
"""
import os
from decouple import config
from pymongo import MongoClient

print("=" * 60)
print("Direct MongoDB Connection Test")
print("=" * 60)

# Load environment variables
MONGODB_URI = config('MONGODB_URI')
MONGODB_DB_NAME = config('MONGODB_DB_NAME', default='doevent_db')

print(f"\nDatabase Name: {MONGODB_DB_NAME}")
print(f"Connection URI (masked): mongodb+srv://***:***@{MONGODB_URI.split('@')[1] if '@' in MONGODB_URI else 'INVALID'}")

print("\n" + "-" * 60)
print("Testing MongoDB Connection...")
print("-" * 60)

try:
    # Create client
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    
    # Test connection
    client.admin.command('ping')
    print("[OK] MongoDB connection successful!")
    
    # List databases
    print("\nAvailable databases:")
    for db_name in client.list_database_names():
        print(f"  - {db_name}")
    
    # Test write operation
    print(f"\n" + "-" * 60)
    print(f"Testing write to '{MONGODB_DB_NAME}' database...")
    print("-" * 60)
    
    db = client[MONGODB_DB_NAME]
    test_collection = db['test_connection']
    
    result = test_collection.insert_one({
        'test': 'data',
        'message': 'MongoDB connection is working!'
    })
    
    print(f"[OK] Write successful! Document ID: {result.inserted_id}")
    
    # Test read operation
    doc = test_collection.find_one({'_id': result.inserted_id})
    print(f"[OK] Read successful! Document: {doc}")
    
    # Cleanup
    test_collection.delete_one({'_id': result.inserted_id})
    print(f"[OK] Cleanup successful!")
    
    print("\n" + "=" * 60)
    print("ALL TESTS PASSED!")
    print("=" * 60)
    print("\nYour MongoDB connection is working correctly.")
    print("The authentication issue may be with MongoEngine configuration.")
    
except Exception as e:
    print(f"\n[ERROR] Connection failed!")
    print(f"Error: {e}")
    print("\n" + "=" * 60)
    print("TROUBLESHOOTING STEPS:")
    print("=" * 60)
    print("1. Check MongoDB Atlas Dashboard:")
    print("   - Database Access: User exists with correct password")
    print("   - Network Access: Your IP is whitelisted (or 0.0.0.0/0)")
    print("\n2. Check .env file:")
    print("   - MONGODB_URI format is correct")
    print("   - No extra spaces or quotes")
    print("\n3. Get new connection string from MongoDB Atlas:")
    print("   - Cluster > Connect > Connect your application")
    print("   - Copy the full string and update .env")
