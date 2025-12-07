"""
Admin Authentication with Role-Based Access Control
"""

from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from decouple import config

# Admin users with roles
ADMIN_USERS = {
    config('ADMIN_USERNAME_1', default='admin'): {
        'password': config('ADMIN_PASSWORD_1', default='admin123'),
        'role': 'superadmin'
    },
    config('ADMIN_USERNAME_2', default='superadmin'): {
        'password': config('ADMIN_PASSWORD_2', default='super123'),
        'role': 'superadmin'
    },
    'kulup1': {
        'password': 'kulup123',
        'role': 'club_moderator'
    },
    'kulup2': {
        'password': 'kulup123',
        'role': 'club_moderator'
    },
}

def authenticate_admin(username, password):
    """Authenticate admin user and return role"""
    user = ADMIN_USERS.get(username)
    if user and user['password'] == password:
        return user['role']
    return None

def admin_required(view_func):
    """Decorator to check if user is admin (any role)"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('is_admin'):
            messages.error(request, 'Bu sayfaya erişim için admin girişi gereklidir.')
            return redirect('admin_login')
        return view_func(request, *args, **kwargs)
    return wrapper

def superadmin_required(view_func):
    """Decorator to check if user is superadmin"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('is_admin'):
            messages.error(request, 'Bu sayfaya erişim için admin girişi gereklidir.')
            return redirect('admin_login')
        
        if request.session.get('admin_role') != 'superadmin':
            messages.error(request, 'Bu sayfaya erişim yetkiniz yok. Sadece superadmin erişebilir.')
            return redirect('admin_dashboard')
        
        return view_func(request, *args, **kwargs)
    return wrapper

def club_moderator_required(view_func):
    """Decorator to check if user is club moderator or superadmin"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('is_admin'):
            messages.error(request, 'Bu sayfaya erişim için admin girişi gereklidir.')
            return redirect('admin_login')
        
        role = request.session.get('admin_role')
        if role not in ['club_moderator', 'superadmin']:
            messages.error(request, 'Bu sayfaya erişim yetkiniz yok.')
            return redirect('admin_dashboard')
        
        return view_func(request, *args, **kwargs)
    return wrapper
