from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Core.mongodb_utils import get_db
from datetime import datetime

@login_required(login_url='/Kullanıcılar/login/')
def kulupOner(request):
    if request.method == 'POST':
        ad = request.POST.get('ad')
        kategori = request.POST.get('kategori')
        aciklama = request.POST.get('aciklama')
        
        try:
            db = get_db()
            db.kulupler.insert_one({
                'ad': ad,
                'kategori': kategori,
                'aciklama': aciklama,
                'kurucu_id': request.user.id,
                'kurucu_username': request.user.username,
                'uye_ids': [],
                'olusturma_tarihi': datetime.now()
            })
            messages.success(request, 'Kulüp öneriniz başarıyla gönderildi!')
            return redirect('kulupler')
        except Exception as e:
            messages.error(request, f'Kulüp oluşturulurken bir hata oluştu: {str(e)}')
    
    return render(request, "kulupOner.html")
