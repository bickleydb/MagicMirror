from django.http import HttpResponse


class FluentResponseCreator:

    def __init__(self):
        self.response = HttpResponse()

    def set_content(self, content):
        self.response.content = content
        return self

    def set_status_code(self, statusCode):
        self.response.status_code = statusCode
        return self

    def set_cookie(self, cookieName, cookieValue, expiration=None, MaxAge=None, Domain=None, Path=None, Secure=None, HttpOnly=None, SameSite=None):
        self.response["Set-Cookie"] = FluentResponseCreator.create_cookie_str(cookieName, cookieValue, expiration=expiration, maxAge=MaxAge, domain=Domain, path=Path, secure=Secure, httpOnly=HttpOnly, sameSite=SameSite)
        return self

    def to_response(self):
        return self.response

    @staticmethod
    def create_cookie_str(cookieName, cookieValue, expiration=None, maxAge=None, domain=None, path=None, secure=None, httpOnly=None, sameSite=None):
        cookieStr = f'{cookieName}={cookieValue};'
        if expiration is not None:
            cookieStr = cookieStr + f'Expires={expiration};'
        if maxAge is not None:
            cookieStr = cookieStr + f'Max-Age={maxAge};'
        if domain is not None:
            cookieStr = cookieStr + f'Domain={domain};'
        if path is not None:
            cookieStr = cookieStr + f'Path={path};'
        if secure is not None:
            cookieStr = cookieStr + f'Secure;'
        if httpOnly is not None:
            cookieStr = cookieStr + f'HttpOnly;'
        if sameSite is not None:
            cookieStr = cookieStr + f'SameSite={sameSite};'
        return cookieStr
