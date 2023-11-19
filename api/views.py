from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from api.gdrive import create_file


@api_view(['POST'])
def create_gdrive_file(request):
    """
    Creates new file on Google Drive using given
    name and data params of the request
    """
    try:
        file_name = request.data['name']
        file_content = request.data['data']
    except KeyError:
        content = {
            'message': 'You have to provide \'name\' and \'data\' parameters'
        }
        return Response(content, status=HTTP_400_BAD_REQUEST)
    else:
        create_file(file_name, file_content)
        content = {
            'message': f'File \'{file_name}.txt\' was created on google drive'
        }
        return Response(content, status=HTTP_201_CREATED)
