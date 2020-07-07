from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
# 这里写函数
def get_h5(request):  # 这里一定要有一个形参，request这个是标准的写法
    # 这个可以向浏览区返回内容
    return render(request, 'jianai/au.html')
