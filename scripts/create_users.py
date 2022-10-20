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
        logger.info(f"{'* ' * 15} Created User: {user} {'* ' * 15}")
    else:
        logger.error(f"Something went wrong while creating user: {user}")
        raise Exception(f"{response.__dict__}")


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


def create_user(tenant: str, user: str, password: str, roles: list[str]) -> requests.Response:
    logger.info(f"{'* ' * 15} Creating User: {user} {'* ' * 15}")

    headers = {
        'Content-Type': 'application/json;charset=utf-8',
        'X-API-Key': env.x_api_key,
        'X-API-AppId': env.x_api_appid
    }

    req_body = get_user_req_payload(tenant=tenant, user=user, password=password, roles=roles)

    logger.info(f"URL: {authorization_service_url}")
    logger.info(f"User: {user}")
    logger.info(f"Tenant ID: {tenant}")
    logger.info(f"Roles: {roles}")
    return requests.post(authorization_service_url, headers=headers, json=req_body, verify=False)


for u in users:
    create_user_response = create_user(tenant=u["tenant"], user=u["user"],
                                       password=u["password"], roles=u["roles"])
    is_user_created(response=create_user_response, user=u["user"])

