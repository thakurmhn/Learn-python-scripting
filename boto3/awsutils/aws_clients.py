import logging

import os
import time

import boto3

LOG = logging.getLogger(__name__)

class AWSClients:
    """A class for generating aws clients and resources"""

    @staticmethod
    def account_id():
        """Given an instance of AWSClients
        when invoked, then returns account ID of role/profile that instance is configured for"""
        sts_client = aws_clients.client('sts')
        caller_arn = sts_client.get_caller_identity()['Arn']
        return caller_arn.split(':')[4]

    def __init__(self, profile_name=None, region_name='us-east-1', role_arn=None, initial_credentials=None):
        self.profile_name = profile_name
        self.region_name = region_name
        self.role_arn = role_arn
        self.initial_credentials = initial_credentials

    def _boto_parameters(self, override_region):
        params = {
            'region_name': override_region if override_region else self.region_name
        }
        if self.profile_name:
            params['profile_name'] = self.profile_name
        elif self.initial_credentials:
            params['aws_access_key_id'] = self.initial_credentials['AccessKeyId']
            params['aws_secret_access_key'] = self.initial_credenctials['SecretAccessKey']
            params['aws_session_token'] = self.initial_credentials['SessionToken']

        return params
    def client(self, client_name, region_name):
        params = self._boto_parameters(region)
        return boto3.Session(**params).client(client_name)

    def resource(self, service_name, region_name):
        params = self._boto_parameters(region)
        return boto3.Session(**params).resource(service_name)


myconn = AWSClients(profile_name='default', region_name='us-east-1')

print(myconn.client(client_name='s3', region_name='us-east-1'))