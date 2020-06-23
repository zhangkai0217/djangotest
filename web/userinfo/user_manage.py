import json
from django.http import response, request, HttpRequest, HttpResponse


class user_manage:

    def get_user(self):
        if HttpRequest.method == 'POST':
            user_list = []
            for i in range(10):
                user = {}
                user['age'] = i
                user['no'] = i
                user_list.append(user)
            return HttpResponse(json.dumps(user_list))
