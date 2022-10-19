#!/usr/bin/env python

import environment as env

users = [
    {
        "user": env.om_admin_username,
        "password": env.om_admin_password,
        "tenant": env.tenant_id,
        "roles": [
            "ROLE_ADMIN",
            "ROLE_USER"
        ]
    },
    {
        "user": env.om_apiuser_username,
        "password": env.om_apiuser_password,
        "tenant": env.tenant_id,
        "roles": [
            "ROLE_ADMIN",
            "ROLE_USER"
        ]
    },
    {
        "user": "newuser@alpsintech.com",
        "password": "",
        "tenant": env.tenant_id,
        "roles": [
            "ROLE_USER"
        ]
    },
    {
        "user": "first.last@alpsintech.com",
        "password": "",
        "tenant": env.tenant_id,
        "roles": [
            "ROLE_USER"
        ]
    }
]
