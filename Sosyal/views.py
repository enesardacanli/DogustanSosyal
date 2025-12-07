from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Core.mongodb_utils import get_db, serialize_mongo_docs
from datetime import datetime

@login_required(login_url='/Kullanıcılar/login/')
def etkinlikler(request):
    db = get_db()
    
    # Kategori filtreleme
    kategori = request.GET.get('kategori')
    query = {}
    if kategori:
        query['kategori'] = kategori
    
    etkinlik_listesi = list(db.etkinlikler.find(query).sort('tarih', -1))
    etkinlik_listesi = serialize_mongo_docs(etkinlik_listesi)
    
    context = {
        'etkinlikler': etkinlik_listesi,
    }
    return render(request, 'etkinlikler.html', context)

@login_required(login_url='/Kullanıcılar/login/')
def kulupler(request):
    db = get_db()
    
    # Kategori filtreleme
    kategori = request.GET.get('kategori')
    query = {}
    if kategori:
        query['kategori'] = kategori
    
    kulup_listesi = list(db.kulupler.find(query).sort('ad', 1))
    kulup_listesi = serialize_mongo_docs(kulup_listesi)
    
    context = {
        'kulupler': kulup_listesi,
    }
    return render(request, 'kulupler.html', context)

@login_required(login_url='/Kullanıcılar/login/')
def duyurular(request):
    db = get_db()
    
    # Kategori filtreleme
    kategori = request.GET.get('kategori')
    query = {}
    if kategori:
        query['kategori'] = kategori
    
    duyuru_listesi = list(db.duyurular.find(query).sort('olusturma_tarihi', -1))
    duyuru_listesi = serialize_mongo_docs(duyuru_listesi)
    
    context = {
        'duyurular': duyuru_listesi,
    }
    return render(request, 'duyurular.html', context)

@login_required(login_url='/Kullanıcılar/login/')
def etkinlik_katil(request, etkinlik_id):
    from django.http import JsonResponse
    from bson import ObjectId
    
    if request.method == 'POST':
        db = get_db()
        
        try:
            etkinlik = db.etkinlikler.find_one({'_id': ObjectId(etkinlik_id)})
            
            if not etkinlik:
                return JsonResponse({'success': False, 'error': 'Etkinlik bulunamadı'})
            
            katilimci_ids = etkinlik.get('katilimci_ids', [])
            user_id = request.user.id
            
            if user_id in katilimci_ids:
                # Kullanıcı zaten katılmış, çıkar
                db.etkinlikler.update_one(
                    {'_id': ObjectId(etkinlik_id)},
                    {'$pull': {'katilimci_ids': user_id}}
                )
                katildi = False
                katilimci_ids.remove(user_id)
            else:
                # Kullanıcıyı ekle
                db.etkinlikler.update_one(
                    {'_id': ObjectId(etkinlik_id)},
                    {'$addToSet': {'katilimci_ids': user_id}}
                )
                katildi = True
                katilimci_ids.append(user_id)
            
            return JsonResponse({
                'success': True,
                'katildi': katildi,
                'katilimci_sayisi': len(katilimci_ids)
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False})
