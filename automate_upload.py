import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'code_secret_client.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
upload_date_time = (datetime.datetime.today() - datetime.timedelta(hours=1)).isoformat(timespec='seconds') + '.000Z'
const_tags = ['among us', 'among us gameplay', 'among us funny moments', 'among us funny',\
'among us best impostor', 'among us best', 'among us review', 'among us impostor', 'among us toast'\
'among us imposter', 'among us twitch', 'twitch clips', 'among us with friends', 'among us game', 'among us impostor gameplay']
request_body = {
    'snippet': {
        'categoryId': 20,
        'title': 'Among us funny moments #1',
        'description': '',
        'tags': const_tags,
    },
    'status': {
    'privacyStatus': 'private',
        'publishAt': upload_date_time,
        'selfDeclaredMadeForKids': False,
    },
    'notifySubscribers': True
}
mediaFile = MediaFileUpload('theout.mp4')
response_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediaFile
).execute()
