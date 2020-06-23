from django.http import HttpResponse
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
