import pickle
import os.path
import os
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from traffic.shared.credentials import APP_SECRET_DIRECTORY, \
     CREDENTIAL_DIRECTORY
import threading


class GoogleCredsManager():

    self.fileLock = threading.Lock()

    def GetFilenameForCreds(self, credsName):
        return CREDENTIAL_DIRECTORY + credsName + ".json"

    def GetCredentialsFromGoogle(self, scopes):
        flow = InstalledAppFlow.from_client_secrets_file(
            APP_SECRET_DIRECTORY + "appCredentials.json",
            scopes)
        return flow.run_local_server()

    def LoadCredsFromFile(self, credsFileName):
        self.fileLock.acquire()
        try:
            with open(credsFileName, 'rb') as token:
                creds = pickle.load(token)
            return creds
        finally:
            self.fileLock.release()

    def OnUserCredsNotExist(self, fileName, scopes):
        creds = self.GetCredentialsFromGoogle(scopes)
        self.SaveCredentials(creds, fileName)
        return creds

    def OnUserHasCreds(self, fileName):
        creds = self.LoadCredsFromFile(fileName)
        if creds.expired:
            creds.refresh(Request())
        if not creds.valid:
            creds = self.GetCredentialsFromGoogle(scopes)
            self.SaveCredentials(creds, fileName)
        return creds

    def GetCredentials(self, scopes, credsName):
        fileName = self.GetFilenameForCreds(credsName)
        if not os.path.exists(fileName):
            return self.OnUserCredsNotExist(scopes, credsName)
        return self.OnUserHasCreds(fileName)

    def SaveCredentials(self, creds, credsFile):
        self.fileLock.acquire()
        try:
            with open(credsFile, 'wb') as file:
                pickle.dump(creds, file)
        finally:
            self.fileLock.release()
