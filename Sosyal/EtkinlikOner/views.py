from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Core.mongodb_utils import get_db
from datetime import datetime

@login_required(login_url='/Kullanıcılar/login/')
def etkinlikOner(request):
    if request.method == 'POST':
        baslik = request.POST.get('baslik')
        kategori = request.POST.get('kategori')
        tarih = request.POST.get('tarih')
        baslangic_saati = request.POST.get('baslangic_saati')
        bitis_saati = request.POST.get('bitis_saati')
        konum = request.POST.get('konum')
        aciklama = request.POST.get('aciklama')
        
        try:
            db = get_db()
            db.etkinlikler.insert_one({
                'baslik': baslik,
                'kategori': kategori,
                'tarih': tarih,
                'baslangic_saati': baslangic_saati,
                'bitis_saati': bitis_saati,
                'konum': konum,
                'aciklama': aciklama,
                'olusturan_id': request.user.id,
                'olusturan_username': request.user.username,
                'katilimci_ids': [],
                'olusturma_tarihi': datetime.now()
            })
            messages.success(request, 'Etkinlik öneriniz başarıyla gönderildi!')
            return redirect('etkinlikler')
        except Exception as e:
            messages.error(request, f'Etkinlik oluşturulurken bir hata oluştu: {str(e)}')
    
    return render(request, "etkinlikOner.html")
