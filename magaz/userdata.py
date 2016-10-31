from django.conf import settings


class UserData(object):

    def __init__(self, request):
        self.session = request.session
        userdata = request.session.get(settings.USER_DATA_SESSION_ID)
        if not userdata:
            userdata = self.session[settings.USER_DATA_SESSION_ID] = {'valute': 'uah', 'develop': 'selfescape'}
        self.userdata = userdata

    def setdolar(self):
        self.userdata['valute'] = 'usd'

    def setuah(self):
        self.userdata['valute'] = 'uah'

    def setnewpost(self):
        self.userdata['develop'] = 'newpost'

    def setselfescape(self):
        self.userdata['develop'] = 'selfescape'

