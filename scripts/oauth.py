#!/usr/bin/env python

import requests
import logging


def generate_token(url: str, req_headers: dict, req_body: dict, logger: logging.Logger) -> str:
    logger.info("Generating OAuth Token")
    oauth_response = requests.post(url=url, headers=req_headers, data=req_body)
    if oauth_response.status_code == 200:
        logger.info("OAuth Token Generated")
        oauth_json_resp = oauth_response.json()
        return oauth_json_resp["access_token"]
    else:
        logger.error("Something went wrong while generating OAuth token")
        raise Exception(f"{oauth_response.__dict__}")

