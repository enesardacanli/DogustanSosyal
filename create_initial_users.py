"""
Script to create initial users in the kullanicilar table
Run this script once to populate the database with initial users
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DoEvent.settings')
django.setup()

from Kullanıcılar.models import Kullanici
from decouple import config


def create_initial_users():
    """Create initial users for the system"""
    
    print("Creating initial users...")
    
    # List of users to create
    users_to_create = [
        {
            'kullanici_adi': config('ADMIN_USERNAME_1', default='admin'),
            'password': config('ADMIN_PASSWORD_1', default='admin123'),
            'email': 'admin@dogustansosyal.com',
            'rol': 'superadmin',
        },
        {
            'kullanici_adi': config('ADMIN_USERNAME_2', default='superadmin'),
            'password': config('ADMIN_PASSWORD_2', default='super123'),
            'email': 'superadmin@dogustansosyal.com',
            'rol': 'superadmin',
        },
        {
            'kullanici_adi': 'kulup1',
            'password': 'kulup123',
            'email': 'kulup1@dogustansosyal.com',
            'rol': 'club_moderator',
        },
        {
            'kullanici_adi': 'kulup2',
            'password': 'kulup123',
            'email': 'kulup2@dogustansosyal.com',
            'rol': 'club_moderator',
        },
        {
            'kullanici_adi': 'testuser',
            'password': 'test123',
            'email': 'test@dogustansosyal.com',
            'rol': 'user',
        },
    ]
    
    created_count = 0
    skipped_count = 0
    
    for user_data in users_to_create:
        kullanici_adi = user_data['kullanici_adi']
        
        # Check if user already exists
        if Kullanici.objects.filter(kullanici_adi=kullanici_adi).exists():
            print(f"[!] Kullanici zaten mevcut: {kullanici_adi}")
            skipped_count += 1
            continue
        
        # Create new user
        kullanici = Kullanici(
            kullanici_adi=kullanici_adi,
            email=user_data['email'],
            rol=user_data['rol'],
            aktif=True,
        )
        kullanici.set_password(user_data['password'])
        kullanici.save()
        
        print(f"[+] Kullanici olusturuldu: {kullanici_adi} ({kullanici.get_rol_display()})")

        created_count += 1
    
    print(f"\n{'='*50}")
    print(f"Toplam oluşturulan kullanıcı: {created_count}")
    print(f"Atlanan kullanıcı: {skipped_count}")
    print(f"{'='*50}\n")
    
    # Display all users
    print("Mevcut kullanicilar:")
    print(f"{'Kullanici Adi':<20} {'Rol':<20} {'E-posta':<30} {'Aktif'}")
    print("-" * 80)
    for kullanici in Kullanici.objects.all():
        aktif_str = 'Evet' if kullanici.aktif else 'Hayir'
        print(f"{kullanici.kullanici_adi:<20} {kullanici.get_rol_display():<20} {kullanici.email or 'N/A':<30} {aktif_str}")



if __name__ == '__main__':
    create_initial_users()
