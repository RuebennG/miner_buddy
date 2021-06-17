import os.path
import pandas as pd

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from google.oauth2 import service_account

class gsheets_api:
    sheet_key = '1sccKwaiKVw6qyaz7Awwv2ztVeedzPdL-jQ_JOuXcnMk'
    pool_sheet_name = 'Pool_Stats'
    hardware_sheet_name = 'Hardware'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    key_doc = 'gsheets/gsheets_api_key/credentials.json'

    def __init__(self):
        self.connection = self.connect()

    def connect(self):
        creds = None
        creds = service_account.Credentials.from_service_account_file(self.key_doc, scopes = self.SCOPES)
        service = build('sheets', 'v4', credentials = creds)
        sheet = service.spreadsheets()

        return sheet

    def get_pool_info(self):
        pool_data = self.connection\
                            .values().get(spreadsheetId = self.sheet_key,
                                range = f'{self.pool_sheet_name}!A:F').execute()\
                                        ['values']

        return pd.DataFrame(pool_data[1:], columns = pool_data[0])

    def update_pool_info(self, pool_updates):
        self.connection\
                .values().append(spreadsheetId = self.sheet_key,
                range = f'{self.pool_sheet_name}!A:F', valueInputOption = 'USER_ENTERED', 
                insertDataOption='INSERT_ROWS', body={"values": pool_updates})\
                        .execute()

    def update_hardware_info(self, hardware_updates):
        self.connection\
                .values().append(spreadsheetId = self.sheet_key,
                 range = f'{self.hardware_sheet_name}!A:F', valueInputOption = 'USER_ENTERED', 
                insertDataOption='INSERT_ROWS', body={"values": hardware_updates})\
                        .execute()






        







         






# If modifying these scopes, delete the file token.json.

# def main():
#     """Shows basic usage of the Docs API.
#     Prints the title of a sample document.
#     """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     service = build('docs', 'v1', credentials=creds)

#     # Retrieve the documents contents from the Docs service.
#     document = service.documents().get(documentId=DOCUMENT_ID).execute()

#     print('The title of the document is: {}'.format(document.get('title')))


# if __name__ == '__main__':
#     main()