from os import access
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token= access_token
        
    def upload_files(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from, "rb")
        dbx.files_upload(f.read(), file_to)
    
def main():
    access_token="sl.BG0dyDo_n5Vt90qaNJhz-2ycO6iUZ57uO9B8E7VMaJw_efw9dKew_4uvQQZVyzlBijmU9oBEypVKZIF-aoYO-VeOtQ7_Jbjl7G7RWSS1rFfuCH34Y4Cl82FPHANJ1ipSvG7uxYo"
    transfer_data=TransferData(access_token)
    file_from=input("Enter the file path to upload: ")
    file_to=input("Enter the file path for dropbox: ")

    transfer_data.upload_files(file_from, file_to)
    print("File successfully uploaded!")
    
main()
