from datetime import date

from django.http import HttpResponse
from web.db.models import User, Us_pwd, Ustest
import json


def add_args(a, b):
    return a + b


# 接口函数
def post(request):
    if request.method == 'POST':  # 当提交表单时
        user_list = []
        for i in range(10):
            user = {}
            user['age'] = i
            user['no'] = i
            user_list.append(user)
        return HttpResponse(json.dumps(user_list))

    else:
        return HttpResponse('方法错误')


def add_user(request):
    tm_us = User(name="zk_dj1", sex=1, start_time=date.today(), money=1500.962)
    tm_us.save()
    return HttpResponse('Success')


def add_pwd(request):
    tmp_pwd = Us_pwd(user_name='zktest3', password='1zc51f5d1f5d5ds5s')
    tmp_pwd.save()
    return HttpResponse('Success')

def add_ustest(request):
    tmp_pwd = Ustest(us='zktest3')
    tmp_pwd.save()
    return HttpResponse('Success')
