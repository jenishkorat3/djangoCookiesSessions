from django.shortcuts import render


def set_cookie(request):
    response = render(request, 'cookies/set_cookies.html')
    response.set_cookie('name', 'jeka', max_age=60*60*24*2)
    return response


def get_cookie(request):
    token = request.COOKIES.get('name')
    return render(request, 'cookies/get_cookies.html', {'token': token})


def delete_cookie(request):
    response = render(request, 'cookies/delete_cookies.html')
    response.delete_cookie('name')
    return response


def set_signed_cookie(request):
    response = render(request, 'cookies/set_signed_cookies.html')
    response.set_signed_cookie('name', 'jeka', salt='jeka', max_age=60*60*24*10)
    return response


def get_signed_cookie(request):
    token = request.get_signed_cookie('name', salt='jeka')
    return render(request, 'cookies/get_signed_cookies.html', {'token': token})
