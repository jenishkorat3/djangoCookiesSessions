from django.shortcuts import render


def set_session(request):
    request.session['name'] = 'jeka'
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
    return render(request, 'session/sessionmethodsinview.html')
