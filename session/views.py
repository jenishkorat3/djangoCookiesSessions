from django.shortcuts import render


def set_session(request):
    request.session['name'] = 'jeka'
    request.session['last name'] = 'korat'
    # request.session.set_expiry(10)
    # request.session.set_expiry(0) #get_expire_at_browser_close:True
    return render(request, 'session/set_session.html')


def get_session(request):
    token = request.session.get('name')
    # token = request.session.get('name', 'guest')   #set default value
    return render(request, 'session/get_session.html', {'token': token})


def delete_session(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'session/delete_session.html')


def flush_session(request):
    request.session.flush()
    return render(request, 'session/flush_session.html')


def sessionmethodsinview(request):
    keys = request.session.keys()
    print(keys)

    items = request.session.items()
    print(items)

    age = request.session.setdefault('age', 31)
    print(age)

    session_cookie_age = request.session.get_session_cookie_age()
    print(session_cookie_age)

    expire_age = request.session.get_expiry_age()
    print(expire_age)

    expire_date = request.session.get_expiry_date()
    print(expire_date)

    expire_at_browser_close = request.session.get_expire_at_browser_close()
    print(expire_at_browser_close)
    return render(request, 'session/sessionmethodsinview.html')


def sessionclear(request):
    request.session.clear_expired()  # delete entry from database of expired sessions
    return render(request, 'session/sessionclear.html')


def sessionmethodsintemplate(request):
    keys = request.session.keys()
    items = request.session.items()
    return render(request, 'session/sessionmethodsintemplate.html', {'keys': keys, 'items': items})


def settestcookie(request):
    request.session.set_test_cookie()
    return render(request, 'session/settestcookie.html')


def checktestcookie(request):
    print(request.session.test_cookie_worked())
    return render(request, 'session/checktestcookie.html')


def deletetestcookie(request):
    print(request.session.delete_test_cookie())
    return render(request, 'session/deletetestcookie.html')
