import configuration
import requests
import data
from configuration import CREATE_USER_PATH




def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers)


def post_new_kit_in_new_user(kit_body):
    response_new_user = post_new_user(data.body)
    auth_token = response_new_user.json()["authToken"]
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=headers)