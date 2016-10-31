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
        self.save()

    def setuah(self):
        self.userdata['valute'] = 'uah'
        self.save()

    def setnewpost(self):
        self.userdata['develop'] = 'newpost'
        self.save()

    def setselfescape(self):
        self.userdata['develop'] = 'selfescape'
        self.save()

    def save(self):
        self.session[settings.USER_DATA_SESSION_ID] = self.userdata
        self.session.modified = True