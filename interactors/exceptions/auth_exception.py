class AuthException(Exception):
    pass

class AuthenticationFailed(AuthException):
    pass

class IdentityProviderError(AuthException):
    pass
