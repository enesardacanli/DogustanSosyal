"""
Create Test User Script
Automatically creates a test superuser for Django application
"""

import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DoEvent.settings')
django.setup()

from django.contrib.auth.models import User

print("=" * 60)
print("Creating Test User")
print("=" * 60)

# Test user credentials
username = 'admin'
email = 'admin@test.com'
password = 'admin123'

# Check if user already exists
if User.objects.filter(username=username).exists():
    print(f"\n[INFO] User '{username}' already exists!")
    user = User.objects.get(username=username)
    print(f"  Username: {user.username}")
    print(f"  Email: {user.email}")
    print(f"  Is superuser: {user.is_superuser}")
else:
    # Create superuser
    user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print(f"\n[OK] Superuser created successfully!")
    print(f"  Username: {username}")
    print(f"  Email: {email}")
    print(f"  Password: {password}")

print("\n" + "=" * 60)
print("Test User Summary")
print("=" * 60)
print(f"\nLogin credentials:")
print(f"  Username: {username}")
print(f"  Password: {password}")
print(f"\nYou can now login to:")
print(f"  - Django Admin: http://localhost:8000/admin")
print(f"  - Application: http://localhost:8000/")
print("\nTo start the server, run:")
print("  py manage.py runserver")
