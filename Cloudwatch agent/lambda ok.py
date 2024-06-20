import boto3
import json
import logging
import os

from base64 import b64decode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# The base-64 encoded, encrypted key (CiphertextBlob) stored in the kmsEncryptedHookUrl environment variable
ENCRYPTED_HOOK_URL = "https://hooks.slack.com/services/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"
# The Slack channel to send a message to stored in the slackChannel environment variable
SLACK_CHANNEL = "system_alerts"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Event: " + str(event))
    brand = "*Helix*"
    message = json.loads(event["Records"][0]["Sns"]["Message"])
    subject = message["AlarmName"]
    description = message["AlarmDescription"]
    #newStateReason = message["NewStateReason"]
    region = message["Region"]
       
    slack_message = {
        'channel': SLACK_CHANNEL,
        'text': ":large_green_circle: %s - %s \n :large_green_circle: %s - Normalized \n :large_green_circle: %s \n" % (brand, subject, description, region)
    }

    req = Request(ENCRYPTED_HOOK_URL, json.dumps(slack_message).encode('utf-8'))
    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
