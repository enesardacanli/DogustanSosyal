"""
Create Test Users and Admins
Creates 2 admins and 2 regular users for testing
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
print("Creating Test Users and Admins")
print("=" * 60)

# Create 2 admin users
admins = [
    {'username': 'admin1', 'email': 'admin1@test.com', 'password': 'admin123', 'first_name': 'Admin', 'last_name': 'Bir'},
    {'username': 'admin2', 'email': 'admin2@test.com', 'password': 'admin123', 'first_name': 'Admin', 'last_name': 'İki'},
]

# Create 2 regular users
users = [
    {'username': 'user1', 'email': 'user1@test.com', 'password': 'user123', 'first_name': 'Kullanıcı', 'last_name': 'Bir'},
    {'username': 'user2', 'email': 'user2@test.com', 'password': 'user123', 'first_name': 'Kullanıcı', 'last_name': 'İki'},
]

print("\n" + "-" * 60)
print("Creating Admin Users")
print("-" * 60)

for admin_data in admins:
    if User.objects.filter(username=admin_data['username']).exists():
        print(f"[INFO] Admin '{admin_data['username']}' already exists")
    else:
        user = User.objects.create_superuser(
            username=admin_data['username'],
            email=admin_data['email'],
            password=admin_data['password'],
            first_name=admin_data['first_name'],
            last_name=admin_data['last_name']
        )
        print(f"[OK] Admin created: {admin_data['username']} / {admin_data['password']}")

print("\n" + "-" * 60)
print("Creating Regular Users")
print("-" * 60)

for user_data in users:
    if User.objects.filter(username=user_data['username']).exists():
        print(f"[INFO] User '{user_data['username']}' already exists")
    else:
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name']
        )
        print(f"[OK] User created: {user_data['username']} / {user_data['password']}")

print("\n" + "=" * 60)
print("Summary - All Users in Database")
print("=" * 60)

all_users = User.objects.all()
print(f"\nTotal users: {all_users.count()}\n")

print("Admins (Superusers):")
for user in User.objects.filter(is_superuser=True):
    print(f"  - {user.username} ({user.get_full_name()}) - {user.email}")

print("\nRegular Users:")
for user in User.objects.filter(is_superuser=False):
    print(f"  - {user.username} ({user.get_full_name()}) - {user.email}")

print("\n" + "=" * 60)
print("Login Credentials")
print("=" * 60)
print("\nAdmins:")
print("  admin1 / admin123")
print("  admin2 / admin123")
print("\nUsers:")
print("  user1 / user123")
print("  user2 / user123")
print("\nYou can login at: http://localhost:8000/")
