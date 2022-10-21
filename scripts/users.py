#!/usr/bin/env python

import environment as env

users = [
    {
        "user": env.om_admin_username,
        "password": "",
        "tenant": env.tenant_id,
        "roles": [
            "az_tibco_om_dev_admin_role"
        ]
    },
    {
        "user": env.om_apiuser_username,
        "password": "",
        "tenant": env.tenant_id,
        "roles": [
            "az_tibco_om_dev_admin_role"
        ]
    },
    {
        "user": "newuser@alpsintech.com",
        "password": "",
        "tenant": env.tenant_id,
        "roles": [
            "az_tibco_om_dev_user_role"
        ]
    },
    {
        "user": "first.last@alpsintech.com",
        "password": "",
        "tenant": env.tenant_id,
        "roles": [
            "az_tibco_om_dev_user_role"
        ]
    }
]
