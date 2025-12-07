from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Core.mongodb_utils import get_db, serialize_mongo_docs
from datetime import datetime

@login_required(login_url='/Kullanıcılar/login/')
def akademik_takvim(request):
    db = get_db()
    
    # Tüm akademik etkinlikleri getir
    etkinlikler = list(db.akademik_etkinlikler.find({'egitim_ogretim_yili': '2025-2026'}))
    
    # Kategorilere göre ayır
    sinavlar = []
    tatiller = []
    kayit_basvurular = []
    donem_tarihleri = []
    
    for etk in etkinlikler:
        etkinlik_obj = {
            'baslik': etk.get('baslik'),
            'tarih': etk.get('tarih'),
            'tip': etk.get('tip'),
            'kategori': etk.get('kategori'),
            'donem': etk.get('donem')
        }
        
        if etk.get('tip') == 'sinav':
            sinavlar.append(etkinlik_obj)
        elif etk.get('tip') == 'tatil':
            tatiller.append(etkinlik_obj)
        elif etk.get('tip') == 'kayit_basvuru':
            kayit_basvurular.append(etkinlik_obj)
        elif etk.get('tip') == 'donem':
            donem_tarihleri.append(etkinlik_obj)
    
    # Diğer önemli tarihler (kayıt + dönem)
    diger = kayit_basvurular + donem_tarihleri
    
    context = {
        'sinavlar': sinavlar,
        'tatiller': tatiller,
        'diger': diger,
        'yaklasan_etkinlikler': (sinavlar[:5] + tatiller[:3] + diger[:2])[:10],  # İlk 10 etkinlik
    }
    return render(request, 'canliAkademikTakvim.html', context)

@login_required(login_url='/Kullanıcılar/login/')
def canliAkademikTakvim(request):
    return akademik_takvim(request)
