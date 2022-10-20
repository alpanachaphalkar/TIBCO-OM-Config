#!/usr/bin/env python

import os


authorization_svc = os.environ.get("AUTHORIZATION_SERVICE")
tenant_id = os.environ.get("DEFAULT_TENANT_ID")
configurator_svc = os.environ.get("CONFIGURATOR_SERVICE")

x_api_appid = os.environ.get("X_API_APPID", default="")
x_api_key = os.environ.get("X_API_KEY", default="")
auth_credentials = os.environ.get("AUTH_CREDENTIAL")
om_admin_username = os.environ.get("OM_ADMIN_USER_NAME", default="")
om_admin_password = os.environ.get("OM_ADMIN_USER_PASSWORD", default="")
om_apiuser_username = os.environ.get("OM_API_USER_NAME", default="")
om_apiuser_password = os.environ.get("OM_API_USER_PASSWORD", default="")
