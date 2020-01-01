#
# HTTP
#
class HTTPRequestError(Exception):
    '''
    Base error for any exceptions caused by communication with remote server
    '''
    pass

class BadRequestError(HTTPRequestError):
    '''
    Error 400
    '''
    pass

class UnauthorizedError(HTTPRequestError):
    '''
    Error 401
    '''
    pass

class TooManyRequestsError(HTTPRequestError):
    '''
    Error 429
    '''
    pass

#
# Local api
#
class BaseMee6PyAPIError(Exception):
    '''
    Base error for any exceptions caused by this api
    '''
    pass

