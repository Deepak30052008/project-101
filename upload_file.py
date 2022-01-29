import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root,filename)         
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                f=open(local_path,'rb') 
                dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BBBm0HHk9pkOXAnc-4YD7_1Io-1FmZgnOiP27YlbTTRpUjVZiqNPDj6IRec4ivF4r0wZi9TNrBT_lCLsCcGrQHEPYQgdNY5t4q3DIj6-CoAxJlD4TUv42jIo9VeTdIuZnpcQF6tbIpU'
    transferData = TransferData(access_token)
    file_from = str(input('Enter The Folder Path to Transfer:- '))
    file_to = str(input('Enter The Path to upload to dropbox:- '))
    transferData.upload_file(file_from, file_to)
    print('File Has Been Uploaded')

main()