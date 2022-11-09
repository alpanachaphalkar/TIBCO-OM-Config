#!/usr/bin/env python

import requests
import environment as env
import oauth
import logging.config

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('post-install')

authorization_service_url = f"{env.authorization_svc}/oauth/token"

oauth_request_headers = {
    "Authorization": f"Basic {env.auth_credentials}"
}
oauth_request_payload = {
    "grant_type": "password",
    "scope": "read write",
    "password": env.om_apiuser_password,
    "username": env.om_apiuser_username,
    "tenantId": env.tenant_id
}

oauth_token = oauth.generate_token(url=authorization_service_url, req_headers=oauth_request_headers,
                                   req_body=oauth_request_payload, logger=logger)

configs_dir = "../seed-data/config-files"
app_properties_dir = "../seed-data/app-properties"

configurator_config_uri = f"{env.configurator_svc}/v1/configuration/configFile/"
configurator_app_uri = f"{env.configurator_svc}/v1/configuration/"
configurator_refresh_config_url = f"{env.configurator_svc}/management/refresh"

config_files_dict = {
    "aopd": ["logback_aopd.xml", "aopd_config.xml"],
    "archival": ["logback_arch.xml"],
    "catalog": ["logback_catalog.xml"],
    "dataservice": ["logback_dataservice.xml"],
    "jeopardy": ["logback_jeopardy.xml", "tibeds_config.xml"],
    "omsui": ["OMSUILog4j.xml", "customDomainExt.xml"],
    "orch": ["logback_orch.xml"]
}

app_properties_files_dict = {
    "aopd": "ConfigValues_AopdService.json",
    "archival": "ConfigValues_ArchivalService.json",
    "catalog": "ConfigValues_CatalogService.json",
    "common": "ConfigValues_Common.json",
    "dataservice": "ConfigValues_DataService.json",
    "jeopardy": "ConfigValues_Jeopardy.json",
    "omsui": "ConfigValues_OMSUI.json",
    "orch": "ConfigValues_OrchService.json"
}


def is_file_uploaded(response: requests.Response, file: str) -> None:
    if response.status_code == 200:
        logger.info(f"{'* ' * 15} File {file} uploaded {'* ' * 15}")
    else:
        logger.error(f"Something went wrong while uploading file {file}")
        raise Exception(f"{response.__dict__}")


def upload_config_files(configs: dict[str, list[str]]) -> None:
    for app, config_files in configs.items():
        configurator_config_url = configurator_config_uri + app
        logger.info(f"{'* ' * 15} Uploading files {'* ' * 15}")
        logger.info(f"URL: {configurator_config_url}")
        for config_file in config_files:
            logger.info(f"File: {config_file}")
            req_file = [
                ("file", (config_file,
                          open(
                              f"{configs_dir}/{config_file}",
                              "rb"),
                          "text/xml"))
            ]
            req_headers = {
                "Authorization": f"Bearer {oauth_token}"
            }
            upload_response = requests.post(url=configurator_config_url, headers=req_headers, files=req_file)
            is_file_uploaded(response=upload_response, file=config_file)


def upload_properties_files(properties: dict[str, str]) -> None:
    for app, properties_file in properties.items():
        configurator_app_url = configurator_app_uri + app
        logger.info(f"{'* ' * 15} Uploading files {'* ' * 15}")
        logger.info(f"URL: {configurator_app_url}")
        logger.info(f"File: {properties_file}")

        req_headers = {
            "Authorization": f"Bearer {oauth_token}",
            "tenantID": env.tenant_id,
            'Content-Type': 'application/json'
        }

        req_body = open(f"{app_properties_dir}/{properties_file}", 'rb')

        upload_response = requests.post(url=configurator_app_url, headers=req_headers, data=req_body)
        is_file_uploaded(response=upload_response, file=properties_file)


def refresh_config():
    logger.info("Refreshing configurations")
    refresh_response = requests.post(url=configurator_refresh_config_url)
    if refresh_response.status_code == 200:
        logger.info("Configurations are refreshed")
    else:
        logger.error("Something went wrong while refreshing configurations")
        raise Exception(refresh_response.__dict__)


upload_config_files(config_files_dict)
upload_properties_files(app_properties_files_dict)
refresh_config()