#!/usr/bin/env python

import requests
import environment as env
import logging.config
from users import users

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


def get_user_req_payload(tenant: str, user: str, password: str, roles: list[str]) -> dict:
    return {
        "user": [
            {
                "enabled": True,
                "password": password,
                "tenantId": tenant,
                "userName": user,
                "userRoles": roles
            }
        ]
    }


def create_user(user: str, req_body: dict) -> requests.Response:
    logger.info(f"Creating User: {user}")
    return requests.post(authorization_service_url, headers=headers, json=req_body, verify=False)


for u in users:
    request_payload = get_user_req_payload(
        tenant=u["tenant"],
        user=u["user"],
        password=u["password"],
        roles=u["roles"]
    )
    create_user_response = create_user(user=u["user"], req_body=request_payload)
    is_user_created(response=create_user_response, user=u["user"])

