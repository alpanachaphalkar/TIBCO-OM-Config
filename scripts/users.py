#!/usr/bin/env python

import environment as env

users = [
    {
        "user": env.om_admin_username,
        "password": "",
        "tenant": env.tenant_id,
        "roles": [
            "AZ_TIBCO_OM_DEV_ROLE_ADMIN"
        ]
    },
    {
        "user": env.om_apiuser_username,
        "password": "",
        "tenant": env.tenant_id,
        "roles": [
            "AZ_TIBCO_OM_DEV_ROLE_ADMIN"
        ]
    },
    {
        "user": "newuser@alpsintech.com",
        "password": "",
        "tenant": env.tenant_id,
        "roles": [
            "AZ_TIBCO_OM_DEV_ROLE_USER"
        ]
    },
    {
        "user": "first.last@alpsintech.com",
        "password": "",
        "tenant": env.tenant_id,
        "roles": [
            "AZ_TIBCO_OM_DEV_ROLE_USER"
        ]
    }
]
