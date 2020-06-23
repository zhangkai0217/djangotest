from django.http import HttpResponse
import json
from web.models.md_us import us



def add_args(a, b):
    return a + b


# 接口函数
def post(request):

    # postgrees test
    md_pg = us.all

    md_pg = us(id=10003, name='2')
    md_pg.save()


    if request.method == 'POST':  # 当提交表单时
        dic = {}
        # 判断是否传参
        if request.POST:
            a = request.POST.get('a', 0)
            b = request.POST.get('b', 0)
            # 判断参数中是否含有a和b
            if a and b:
                res = add_args(a, b)
                dic['number'] = res
                dic = json.dumps(dic)
                return HttpResponse(dic)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')

    else:
        return HttpResponse('方法错误')
