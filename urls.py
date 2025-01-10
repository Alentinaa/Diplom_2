class Urls:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'

    CREATE_USER = f"{MAIN_URL}/api/auth/register"
    LOGIN = f"{MAIN_URL}/api/auth/login"
    GET_USER_DATA = f"{MAIN_URL}/api/auth/user"
    CHANGE_USER_DATA = f"{MAIN_URL}/api/auth/user"
    DELETE_USER = f"{MAIN_URL}/api/auth/user"
    CREATE_ORDER = f"{MAIN_URL}/api/orders"
    GET_ORDER = f"{MAIN_URL}/api/orders"
    headers = {"Content-Type": "application/json"}