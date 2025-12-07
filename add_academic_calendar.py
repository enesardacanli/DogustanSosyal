"""
Add Academic Calendar Data to MongoDB
Adds 2025-2026 academic year calendar
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

akademik_takvim_data = {
    "egitim_ogretim_yili": "2025-2026",
    "not": "Yükseköğretim Kurumu'ndan yapılacak değişiklikler ve yeni kararlara uygun olarak akademik takvimde güncellemeler yapılabilecektir.",
    "genel_not": "Tüm işlemler için Öğrenci Bilgi Sistemi (OBS) 16:00'da kapanacaktır.",
    "donemler": [
        {
            "ad": "Güz Dönemi",
            "kayit_ve_basvurular": [
                {"tarih": "10-30 Temmuz 2025", "etkinlik": "Kurum Dışı Yatay Geçiş (Başarı Ortalaması ile) Başvuru Tarihleri"},
                {"tarih": "01-15 Ağustos 2025", "etkinlik": "Yatay Geçiş Yönetmelik Ek Madde-1 Uyarınca Merkezi Yerleştirme Puanına Göre Yatay Geçiş Başvuru Tarihleri (Kurum İçi Ek Madde-1 Başvuruları Dahil)"},
                {"tarih": "08-10 Eylül 2025", "etkinlik": "Başarı Ortalaması ile Kurum İçi Yatay Geçiş Başvuru Tarihleri"},
                {"tarih": "10-12 Eylül 2025", "etkinlik": "Çift Anadal ve Yandal Programlarına Başvuru Tarihleri"},
                {"tarih": "16-19 Eylül 2025", "etkinlik": "Ders Kayıt Tarihleri"}
            ],
            "sinavlar": [
                {"tarih": "15 Eylül 2025", "etkinlik": "Doğuş Üniversitesi Yeterlik Sınavı (DÜİYES)"},
                {"tarih": "3-9 Kasım 2025", "etkinlik": "Ön Lisans Güz Dönemi Ara Sınav Tarihleri"},
                {"tarih": "13-16 Kasım 2025", "etkinlik": "Lisans Güz Dönemi Ara Sınav Tarihleri"},
                {"tarih": "29 Aralık 2025-11 Ocak 2026", "etkinlik": "Güz Dönemi Final Sınavı Tarihleri"},
                {"tarih": "19-27 Ocak 2026", "etkinlik": "Güz Dönemi Bütünleme Sınavı Tarihleri"}
            ],
            "baslangic_bitis": [
                {"tarih": "22 Eylül 2025", "etkinlik": "Güz Dönemi Derslerinin Başlaması (Oryantasyon Programı dahil)"},
                {"tarih": "26 Aralık 2025", "etkinlik": "Güz Yarıyılı Derslerinin Sonu"}
            ]
        },
        {
            "ad": "Bahar Dönemi",
            "kayit_ve_basvurular": [
                {"tarih": "26 Ocak-06 Şubat 2026", "etkinlik": "Kurum Dışı Başarı Ortalaması (Ön Lisans) ve Merkezi Yerleştirme Puanına Göre Yatay Geçiş Başvuru Tarihleri (Ek Madde-1, Kurum İçi dahil)"},
                {"tarih": "28 Ocak-06 Şubat 2026", "etkinlik": "Kurum İçi Başarı Ortalamasına Göre Yatay Geçiş Başvuru Tarihleri"},
                {"tarih": "28 Ocak-06 Şubat 2026", "etkinlik": "Çift Anadal ve Yandal Başvuru Tarihleri"},
                {"tarih": "10-13 Şubat 2026", "etkinlik": "Bahar Dönemi Ders Kayıt Tarihleri"}
            ],
            "sinavlar": [
                {"tarih": "30 Mart-5 Nisan 2026", "etkinlik": "Ön Lisans Bahar Dönemi Ara Sınav Tarihleri"},
                {"tarih": "30 Mart-11 Nisan 2026", "etkinlik": "Lisans Bahar Dönemi Ara Sınav Tarihleri"},
                {"tarih": "01-14 Haziran 2026", "etkinlik": "Bahar Yarıyılı Final Sınav Tarihleri"},
                {"tarih": "22-30 Haziran 2026", "etkinlik": "Bütünleme Sınavı Tarihleri"},
                {"tarih": "22 Haziran 2026", "etkinlik": "Doğuş Üniversitesi İngilizce Yeterlik Sınavı (DÜİYES)"}
            ],
            "baslangic_bitis": [
                {"tarih": "16 Şubat 2026", "etkinlik": "Bahar Dönemi Derslerinin Başlaması"},
                {"tarih": "25 Mayıs 2026", "etkinlik": "Bahar Yarıyılı Derslerinin Sonu"}
            ]
        },
        {
            "ad": "Yaz Öğretimi",
            "kayit_ve_basvurular": [
                {"tarih": "7-9 Temmuz 2026", "etkinlik": "Yaz Döneminde Açılacak Derslerin Belirlenmesi İçin Ders Seçimi ve Mali Kayıt"}
            ],
            "sinavlar": [
                {"tarih": "27 Temmuz - 1 Ağustos 2026", "etkinlik": "Yaz Dönemi Ara Sınav Tarihleri"},
                {"tarih": "31 Ağustos-5 Eylül 2026", "etkinlik": "Yaz Dönemi Final Sınavı Tarihleri"},
                {"tarih": "08-12 Eylül 2026", "etkinlik": "Bütünleme Sınavı Tarihleri"}
            ],
            "baslangic_bitis": [
                {"tarih": "13 Temmuz 2026", "etkinlik": "Yaz Dönemi Derslerinin Başlangıcı (Cumartesi günleri dahil)"},
                {"tarih": "22 Ağustos 2026", "etkinlik": "Yaz Dönemi Derslerinin Son Günü (Cumartesi günleri dahil)"}
            ]
        }
    ],
    "resmi_tatiller": [
        {"tarih": "28 (Yarım Gün) - 29 Ekim 2025", "etkinlik": "Cumhuriyet Bayramı"},
        {"tarih": "10 Kasım 2025", "etkinlik": "Atatürk'ü Anma Günü"},
        {"tarih": "1 Ocak 2026", "etkinlik": "Yılbaşı"},
        {"tarih": "19 (Arife Gün) - 22 Mart 2026", "etkinlik": "Ramazan Bayramı"},
        {"tarih": "23 Nisan 2026", "etkinlik": "Ulusal Egemenlik ve Çocuk Bayramı"},
        {"tarih": "1 Mayıs 2026", "etkinlik": "Emek ve Dayanışma Günü"},
        {"tarih": "19 Mayıs 2026", "etkinlik": "Atatürk'ü Anma Gençlik ve Spor Bayramı"},
        {"tarih": "26 (Arife Gün) - 30 Mayıs 2026", "etkinlik": "Kurban Bayramı"},
        {"tarih": "15 Temmuz 2026", "etkinlik": "Demokrasi ve Milli Birlik Günü"},
        {"tarih": "30 Ağustos 2026", "etkinlik": "Zafer Bayramı"}
    ]
}

print("=" * 80)
print("Akademik Takvim Verileri MongoDB'ye Ekleniyor")
print("=" * 80)

# Tüm etkinlikleri düz liste olarak ekle
etkinlikler = []

# Dönemlerdeki tüm etkinlikleri ekle
for donem in akademik_takvim_data['donemler']:
    donem_adi = donem['ad']
    
    # Kayıt ve başvurular
    for item in donem.get('kayit_ve_basvurular', []):
        etkinlikler.append({
            'tip': 'kayit_basvuru',
            'donem': donem_adi,
            'tarih': item['tarih'],
            'baslik': item['etkinlik'],
            'kategori': 'Kayıt ve Başvurular',
            'egitim_ogretim_yili': akademik_takvim_data['egitim_ogretim_yili'],
            'olusturma_tarihi': datetime.now()
        })
    
    # Sınavlar
    for item in donem.get('sinavlar', []):
        etkinlikler.append({
            'tip': 'sinav',
            'donem': donem_adi,
            'tarih': item['tarih'],
            'baslik': item['etkinlik'],
            'kategori': 'Sınavlar',
            'egitim_ogretim_yili': akademik_takvim_data['egitim_ogretim_yili'],
            'olusturma_tarihi': datetime.now()
        })
    
    # Başlangıç/Bitiş
    for item in donem.get('baslangic_bitis', []):
        etkinlikler.append({
            'tip': 'donem',
            'donem': donem_adi,
            'tarih': item['tarih'],
            'baslik': item['etkinlik'],
            'kategori': 'Dönem Başlangıç/Bitiş',
            'egitim_ogretim_yili': akademik_takvim_data['egitim_ogretim_yili'],
            'olusturma_tarihi': datetime.now()
        })

# Resmi tatiller
for item in akademik_takvim_data['resmi_tatiller']:
    etkinlikler.append({
        'tip': 'tatil',
        'donem': 'Genel',
        'tarih': item['tarih'],
        'baslik': item['etkinlik'],
        'kategori': 'Resmi Tatiller',
        'egitim_ogretim_yili': akademik_takvim_data['egitim_ogretim_yili'],
        'olusturma_tarihi': datetime.now()
    })

# Önce mevcut akademik takvim verilerini temizle
db.akademik_etkinlikler.delete_many({'egitim_ogretim_yili': '2025-2026'})

# Yeni verileri ekle
if etkinlikler:
    db.akademik_etkinlikler.insert_many(etkinlikler)
    print(f"\n[OK] {len(etkinlikler)} akademik takvim etkinliği eklendi!")
    
    # Kategorilere göre özet
    print("\n" + "=" * 80)
    print("Kategori Özeti:")
    print("=" * 80)
    
    kategoriler = {}
    for etk in etkinlikler:
        kat = etk['kategori']
        kategoriler[kat] = kategoriler.get(kat, 0) + 1
    
    for kategori, sayi in sorted(kategoriler.items()):
        print(f"  {kategori}: {sayi} etkinlik")

print("\n" + "=" * 80)
print("Toplam Etkinlik Sayısı:", db.akademik_etkinlikler.count_documents({}))
print("=" * 80)
print("\nAkademik takvimi görmek için:")
print("http://localhost:8000/Akademik/canli-akademik-takvim/")
print("\nMongoDB Atlas:")
print("Collections -> dogustansosyalDB -> akademik_etkinlikler")
