"""
MongoDB Model Test Script
Test script to verify MongoDB connection and MongoEngine models
"""

import os
import sys
import django
from datetime import datetime

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DoEvent.settings')
django.setup()

print("=" * 60)
print("MongoDB Model Test Script")
print("=" * 60)

# Import MongoDB models
from Sosyal.models_mongo import Etkinlik, Kulup, Duyuru
from Akademik.AkademikTakvim.models_mongo import AkademikEtkinlik
from Akademik.RandevuSistemi.models_mongo import Ogretmen, Randevu
from Akademik.DevamsizlikTakvimi.models_mongo import Ders, Devamsizlik

print("\n[OK] All MongoDB models imported successfully")

# Test 1: Create a test Etkinlik
print("\n" + "-" * 60)
print("Test 1: Creating a test Etkinlik")
print("-" * 60)

try:
    test_etkinlik = Etkinlik(
        baslik="Test Konser",
        aciklama="MongoEngine test etkinligi",
        kategori="konser",
        tarih="2025-12-15",
        baslangic_saati="19:00",
        bitis_saati="22:00",
        konum="Konser Salonu",
        katilimci_ids=[1, 2, 3],
        olusturan_id=1,
        olusturma_tarihi=datetime.now()
    )
    test_etkinlik.save()
    print(f"[OK] Etkinlik created with ID: {test_etkinlik.id}")
    print(f"  Baslik: {test_etkinlik.baslik}")
    print(f"  Katilimci sayisi: {test_etkinlik.katilimci_sayisi()}")
except Exception as e:
    print(f"[ERROR] Error creating Etkinlik: {e}")

# Test 2: Create a test Kulup
print("\n" + "-" * 60)
print("Test 2: Creating a test Kulup")
print("-" * 60)

try:
    test_kulup = Kulup(
        ad="Yazilim Kulubu",
        aciklama="Yazilim gelistirme kulubu",
        kategori="teknoloji",
        uye_ids=[1, 2, 3, 4, 5],
        kurucu_id=1,
        olusturma_tarihi=datetime.now()
    )
    test_kulup.save()
    print(f"[OK] Kulup created with ID: {test_kulup.id}")
    print(f"  Ad: {test_kulup.ad}")
    print(f"  Uye sayisi: {test_kulup.uye_sayisi()}")
except Exception as e:
    print(f"[ERROR] Error creating Kulup: {e}")

# Test 3: Create a test Duyuru
print("\n" + "-" * 60)
print("Test 3: Creating a test Duyuru")
print("-" * 60)

try:
    test_duyuru = Duyuru(
        baslik="Test Duyuru",
        icerik="Bu bir test duyurusudur",
        kategori="genel",
        yazar_id=1,
        olusturma_tarihi=datetime.now(),
        goruntulenme=0
    )
    test_duyuru.save()
    print(f"[OK] Duyuru created with ID: {test_duyuru.id}")
    print(f"  Baslik: {test_duyuru.baslik}")
except Exception as e:
    print(f"[ERROR] Error creating Duyuru: {e}")

# Test 4: Create a test Ders
print("\n" + "-" * 60)
print("Test 4: Creating a test Ders")
print("-" * 60)

try:
    test_ders = Ders(
        ders_kodu="CS101",
        ders_adi="Programlama Temelleri",
        ogretmen="Prof. Dr. Ali Veli",
        kredi=4,
        haftalik_ders_saati=4,
        devam_zorunlulugu=70
    )
    test_ders.save()
    print(f"[OK] Ders created with ID: {test_ders.id}")
    print(f"  Ders: {test_ders.ders_kodu} - {test_ders.ders_adi}")
    print(f"  Toplam ders saati: {test_ders.toplam_ders_saati()}")
except Exception as e:
    print(f"[ERROR] Error creating Ders: {e}")

# Test 5: Query test - List all Etkinlikler
print("\n" + "-" * 60)
print("Test 5: Querying all Etkinlikler")
print("-" * 60)

try:
    all_etkinlikler = Etkinlik.objects.all()
    print(f"[OK] Found {all_etkinlikler.count()} etkinlik(ler)")
    for etkinlik in all_etkinlikler:
        print(f"  - {etkinlik.baslik} ({etkinlik.kategori})")
except Exception as e:
    print(f"[ERROR] Error querying Etkinlikler: {e}")

# Test 6: Query test - Filter Kulupler by kategori
print("\n" + "-" * 60)
print("Test 6: Filtering Kulupler by kategori")
print("-" * 60)

try:
    teknoloji_kulupler = Kulup.objects.filter(kategori='teknoloji')
    print(f"[OK] Found {teknoloji_kulupler.count()} teknoloji kulubu")
    for kulup in teknoloji_kulupler:
        print(f"  - {kulup.ad}")
except Exception as e:
    print(f"[ERROR] Error filtering Kulupler: {e}")

print("\n" + "=" * 60)
print("Test Completed!")
print("=" * 60)
print("\nNote: Test data has been created in MongoDB.")
print("You can view it in MongoDB Atlas or use this script again.")
