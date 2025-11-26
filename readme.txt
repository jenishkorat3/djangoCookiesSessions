HttpResponse.set_cookies(
    key,
    value='',
    max_age=None,     // max_age = 60*60*24*2  // 2 days
    expires=None,     // expires = datetime.utcnow() + timedelta(days=2)
    path='/',         //path="/home"
    domain=None,      //domain="jeka.com"
    secure=False,
    httponly=False,
    samesite=none,
)
