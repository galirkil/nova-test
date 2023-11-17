from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def create_file(name: str, data: str) -> None:
    """
    Create new .txt file on Google Drive

    :param name: name of the file
    :type name: str
    :param data: text contents of the file
    :type data: str

    :rtype: None
    """
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)

    file1 = drive.CreateFile({'title': f'{name}.txt'})
    file1.SetContentString(data)
    file1.Upload()
