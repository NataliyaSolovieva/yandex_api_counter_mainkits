import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


def post_new_client_kit(kit_body):
    auth_token = post_new_user(data.user_body).json()["authToken"]
    headers_with_token = data.headers.copy()
    headers_with_token["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_MAIN_KITS_PATH,  # подставляем полный url
                         json=kit_body,  # тут тело
                         headers=headers_with_token)  # а здесь заголовки




