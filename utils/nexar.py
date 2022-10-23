#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base64 import urlsafe_b64decode
from dataclasses import dataclass
from json import loads
from requests import post
from requests import session
from time import time
from typing import Optional

def decode_json_web_token(token) -> dict:
    """Decode JSON web token"""
    tok_encoded_b64 = token.split(".")[1] + "=="
    tok_decoded_b64 = urlsafe_b64decode(tok_encoded_b64)
    tok_decoded_utf8 = tok_decoded_b64.decode("utf-8")
    decoded_token = loads(tok_decoded_utf8)
    return decoded_token


@dataclass
class NexarClient:
    """Nexar client interface"""
    
    identity: str
    secret: str
    session: Optional[object] = session()
    expiration: Optional[int] = -1
    api: Optional[str] = "https://api.nexar.com/graphql"
    url: Optional[str] = "https://identity.nexar.com/connect/token" 
    
    def get_token(self) -> dict:
        """Get token"""
        data = {
            "grant_type": "client_credentials",
            "client_id": self.identity,
            "client_secret": self.secret
        }
        token = post(
            url=self.url,
            data=data,
            allow_redirects=False,
        ).json()
        return token
    
    def check_expiration(self) -> None:
        """Check token expiration"""
        if (self.expiration < time() + 300): 
            token = self.get_token()
            access_token = token.get("access_token")
            self.session.headers.update(
                {
                    "token": access_token
                }
            )
            decoded_jwt = decode_json_web_token(access_token)
            self.expiration = decoded_jwt.get("exp")

    def start(self) -> None:
        """Intitialize session"""
        self.session.keep_alive = False
        self.check_expiration()

    def fetch(self, query: str, variables: dict) -> dict:
        """Query Nexar"""
        self.check_expiration()
        resp = self.session.post(
            self.api,
            json={
                "query": query,
                "variables": variables
            }
        ).json()
        return resp["data"]

@dataclass
class NexarLifeCycle:
    """Nexar part lifecycle representation"""
    
    client: NexarClient
    query: str = """
        query Search($mpn: String!) {
            supSearchMpn(q: $mpn, limit: 2) {
              results {
                part {
                  mpn
                  shortDescription
                  manufacturer {
                    name
                  }
                  specs {
                    attribute {
                      shortname
                    }
                    value
                  }
                }
              }
            }
          }
    """
    
    def search(self, mpn: str) -> dict:
        """Query life cycle information by MPN"""
        self.client.start()
        response = self.client.fetch(
            self.query,
            {"mpn": mpn}
        )
        results = response["supSearchMpn"]["results"]
        return results