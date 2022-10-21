#!/usr/bin/env python

import environment as env

users = [
    {
        "user": env.om_admin_username,
        "password": "",
        "tenant": env.tenant_id,
        "roles": [
            "azure-tibco-om-dev-admin-role",
            "ROLE_ADMIN"
        ]
    },
    {
        "user": env.om_apiuser_username,
        "password": "",
        "tenant": env.tenant_id,
        "roles": [
            "azure-tibco-om-dev-admin-role",
            "ROLE_ADMIN"
        ]
    },
    {
        "user": "newuser@alpsintech.com",
        "password": "",
        "tenant": env.tenant_id,
        "roles": [
            "azure-tibco-om-dev-user-role",
            "ROLE_USER"
        ]
    },
    {
        "user": "first.last@alpsintech.com",
        "password": "",
        "tenant": env.tenant_id,
        "roles": [
            "azure-tibco-om-dev-user-role",
            "ROLE_USER"
        ]
    }
]
