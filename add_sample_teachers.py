"""
Add Sample Teachers to MongoDB
Creates 20 sample teachers for the appointment system
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DoEvent.settings')
django.setup()

from Core.mongodb_utils import get_db
from datetime import datetime

db = get_db()

# 20 örnek öğretim görevlisi
ogretmenler = [
    {'ad': 'Prof. Dr. Ahmet Yılmaz', 'unvan': 'Profesör', 'bolum': 'Bilgisayar Mühendisliği', 'ofis': 'A-301', 'email': 'ahmet.yilmaz@universite.edu.tr'},
    {'ad': 'Doç. Dr. Ayşe Demir', 'unvan': 'Doçent', 'bolum': 'Yazılım Mühendisliği', 'ofis': 'B-205', 'email': 'ayse.demir@universite.edu.tr'},
    {'ad': 'Dr. Öğr. Üyesi Mehmet Kaya', 'unvan': 'Dr. Öğretim Üyesi', 'bolum': 'Bilgisayar Mühendisliği', 'ofis': 'A-412', 'email': 'mehmet.kaya@universite.edu.tr'},
    {'ad': 'Prof. Dr. Fatma Şahin', 'unvan': 'Profesör', 'bolum': 'Elektrik-Elektronik Mühendisliği', 'ofis': 'C-101', 'email': 'fatma.sahin@universite.edu.tr'},
    {'ad': 'Doç. Dr. Ali Çelik', 'unvan': 'Doçent', 'bolum': 'Makine Mühendisliği', 'ofis': 'D-308', 'email': 'ali.celik@universite.edu.tr'},
    {'ad': 'Dr. Öğr. Üyesi Zeynep Arslan', 'unvan': 'Dr. Öğretim Üyesi', 'bolum': 'Endüstri Mühendisliği', 'ofis': 'E-215', 'email': 'zeynep.arslan@universite.edu.tr'},
    {'ad': 'Prof. Dr. Mustafa Öztürk', 'unvan': 'Profesör', 'bolum': 'Bilgisayar Mühendisliği', 'ofis': 'A-505', 'email': 'mustafa.ozturk@universite.edu.tr'},
    {'ad': 'Doç. Dr. Elif Yıldız', 'unvan': 'Doçent', 'bolum': 'Yazılım Mühendisliği', 'ofis': 'B-403', 'email': 'elif.yildiz@universite.edu.tr'},
    {'ad': 'Dr. Öğr. Üyesi Hasan Aydın', 'unvan': 'Dr. Öğretim Üyesi', 'bolum': 'Bilgisayar Mühendisliği', 'ofis': 'A-218', 'email': 'hasan.aydin@universite.edu.tr'},
    {'ad': 'Prof. Dr. Selin Koç', 'unvan': 'Profesör', 'bolum': 'Matematik', 'ofis': 'F-102', 'email': 'selin.koc@universite.edu.tr'},
    {'ad': 'Doç. Dr. Burak Erdoğan', 'unvan': 'Doçent', 'bolum': 'Fizik', 'ofis': 'G-204', 'email': 'burak.erdogan@universite.edu.tr'},
    {'ad': 'Dr. Öğr. Üyesi Deniz Aksoy', 'unvan': 'Dr. Öğretim Üyesi', 'bolum': 'Kimya', 'ofis': 'H-310', 'email': 'deniz.aksoy@universite.edu.tr'},
    {'ad': 'Prof. Dr. Can Yavuz', 'unvan': 'Profesör', 'bolum': 'İnşaat Mühendisliği', 'ofis': 'I-401', 'email': 'can.yavuz@universite.edu.tr'},
    {'ad': 'Doç. Dr. Merve Güneş', 'unvan': 'Doçent', 'bolum': 'Çevre Mühendisliği', 'ofis': 'J-105', 'email': 'merve.gunes@universite.edu.tr'},
    {'ad': 'Dr. Öğr. Üyesi Emre Polat', 'unvan': 'Dr. Öğretim Üyesi', 'bolum': 'Bilgisayar Mühendisliği', 'ofis': 'A-320', 'email': 'emre.polat@universite.edu.tr'},
    {'ad': 'Prof. Dr. Gizem Karaca', 'unvan': 'Profesör', 'bolum': 'Biyomedikal Mühendisliği', 'ofis': 'K-201', 'email': 'gizem.karaca@universite.edu.tr'},
    {'ad': 'Doç. Dr. Onur Tekin', 'unvan': 'Doçent', 'bolum': 'Mekatronik Mühendisliği', 'ofis': 'L-307', 'email': 'onur.tekin@universite.edu.tr'},
    {'ad': 'Dr. Öğr. Üyesi Pınar Acar', 'unvan': 'Dr. Öğretim Üyesi', 'bolum': 'Yazılım Mühendisliği', 'ofis': 'B-112', 'email': 'pinar.acar@universite.edu.tr'},
    {'ad': 'Prof. Dr. Serkan Yurt', 'unvan': 'Profesör', 'bolum': 'Bilgisayar Mühendisliği', 'ofis': 'A-601', 'email': 'serkan.yurt@universite.edu.tr'},
    {'ad': 'Doç. Dr. Tuğba Kılıç', 'unvan': 'Doçent', 'bolum': 'Veri Bilimi', 'ofis': 'M-203', 'email': 'tugba.kilic@universite.edu.tr'},
]

print("=" * 60)
print("MongoDB'ye Örnek Öğretim Görevlileri Ekleniyor")
print("=" * 60)

# Önce mevcut öğretmenleri temizle (isteğe bağlı)
# db.ogretmenler.delete_many({})

added_count = 0
for ogretmen in ogretmenler:
    # Aynı email varsa ekleme
    existing = db.ogretmenler.find_one({'email': ogretmen['email']})
    if not existing:
        ogretmen['olusturma_tarihi'] = datetime.now()
        ogretmen['aktif'] = True
        db.ogretmenler.insert_one(ogretmen)
        print(f"[OK] {ogretmen['ad']} - {ogretmen['bolum']}")
        added_count += 1
    else:
        print(f"[SKIP] {ogretmen['ad']} - Zaten kayıtlı")

print("\n" + "=" * 60)
print(f"Toplam {added_count} öğretim görevlisi eklendi!")
print("=" * 60)

# Toplam öğretmen sayısını göster
total = db.ogretmenler.count_documents({})
print(f"\nMongoDB'de toplam {total} öğretim görevlisi var.")
print("\nÖğretim görevlilerini görmek için:")
print("MongoDB Atlas → Collections → dogustansosyalDB → ogretmenler")
