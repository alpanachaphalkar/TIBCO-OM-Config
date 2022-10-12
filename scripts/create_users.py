import requests
import environment as env
import logging.config

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('post-install')
authorization_service_url = f"{env.authorization_svc}/v1/user"


def is_user_created(response: requests.Response, user: str) -> None:
    if response.status_code == 201:
        logger.info(f"Created User: {user}")
    else:
        logger.error(f"Something went wrong while creating user: {user}")
        raise Exception(f"{response.__dict__}")


headers = {
    'Content-Type': 'application/json;charset=utf-8',
    'X-API-Key': env.x_api_key,
    'X-API-AppId': env.x_api_appid
}

admin_user_payload = {
    "user": [
        {
            "enabled": True,
            "password": env.om_admin_password,
            "tenantId": env.tenant_id,
            "userName": env.om_admin_username,
            "userRoles": [
                "ROLE_ADMIN"
            ]
        }
    ]
}

api_user_payload = {
    "user": [
        {
            "enabled": True,
            "password": env.om_apiuser_password,
            "tenantId": env.tenant_id,
            "userName": env.om_apiuser_username,
            "userRoles": [
                "ROLE_ADMIN"
            ]
        }
    ]
}


def create_user(user: str, req_body: dict) -> requests.Response:
    logger.info(f"Creating User: {user}")
    return requests.post(authorization_service_url, headers=headers, json=req_body, verify=False)


admin_response = create_user(user=env.om_admin_username, req_body=admin_user_payload)
is_user_created(response=admin_response, user=env.om_admin_username)

api_user_response = create_user(user=env.om_apiuser_username, req_body=api_user_payload)
is_user_created(response=api_user_response, user=env.om_apiuser_username)
