from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.gdrive import create_file


@api_view(['POST'])
def create_gdrive_file(request):
    """
    Creates new file on Google Drive using given name and data params of the request
    """
    try:
        file_name = request.data['name']
        file_content = request.data['data']
    except KeyError:
        return Response({'message': 'You have to provide \'name\' and \'data\' parameters'})
    else:
        create_file(file_name, file_content)
        return Response({'message': f'File \'{file_name}.txt\' was created on google drive'})
