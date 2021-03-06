import httplib2
import os
import apiclient
import oauth2client
import argparse
flags = argparse.ArgumentParser(
    parents=[oauth2client.tools.argparser]
).parse_args()

import base64
from email.mime.text import MIMEText
from email.utils import formatdate
import traceback

SCOPES = "https://www.googleapis.com/auth/gmail.send"
CLIENT_SECRET_FILE = "client_secret.json"
APPLICATION_NAME = "junno00_tools"


MAIL_FROM = "imai@molcure.io"
MAIL_TO = "junno0418@gmail.com"

def get_credentials():
    script_dir = os.path.abspath(os.path.dirname(__file__))
    credential_dir = os.path.join(script_dir,".credentials")

    if not os.path.exists(credential_dir):
        os.mkdirs(credential_dir)

    credential_path = os.path.join(credential_dir,
                                   "my_gmail_sender.json")

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()

    if not credentials or credentials.invalid:
        flow = oauth2client.client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = oauth2client.tools.run_flow(flow, store, flags)
        print("Storing credentials to " + credential_path)

    return credentials


def create_message():
    message = MIMEText("メールのテストです。")
    message["from"] = MAIL_FROM
    message["to"] = MAIL_TO
    message["subject"] = "gmail_api_test"
    message["Date"] = formatdate(localtime=True)

    byte_msg = message.as_string().encode(encoding="UTF-8")
    byte_msg_b64encoded = base64.urlsafe_b64encode(byte_msg)
    str_msg_b64encoded = byte_msg_b64encoded.decode(encoding="UTF-8")

    return {"raw": str_msg_b64encoded}

if __name__ == '__main__':
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build("gmail","v1",http=http)

    try:
        result = service.users().messages().send(
            userId=MAIL_FROM,
            body=create_message()
            ).execute()
        print("Message Id: {}".format(result["id"]))

    except apiclient.error.HttpError:
        print("======Start trace======")
        traceback.print_exc()
        print("======End trace======")








