import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
# Create your views here.
def index(request):
    return render(request,"myapp/index.html")

def resp01(request):
    return HttpResponse("一个简单的视图")

def resp02(request):
    # 直接返回一个404,没有去加载404的模板页面
    return HttpResponseNotFound('<h1>Page not found</h1>')

    # 可以直接返回一个status状态码
    # return HttpResponse(status=403)

    # 返回一个404的错误页面
    #raise Http404("Poll does not exist")

#重定向
def resp03(request):
    # redirect重定向  reverse反向解析url地址
    return redirect(reverse('resp01'))

    # 执行一段js代码，用js进行重定向
    # return HttpResponse('<script>alert("添加成功");location.href = "/resp01"; </script>')

    # 加载一个提醒信息的跳转页面
    context = {'info':'数据添加成功','u':'/resp01'}
    return render(request,'info.html',context)

class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

def resp05(request):
    data = [
        {'id':1001,'name':"zhangsan",'age':20},
         {'id':1001,'name':"zhangsan",'age':20},
    ]
    return JsonResponse({"data":data})

def resp06(request):
    # 获取当前的 响应对象
    response = HttpResponse('cookie的设置')

    # 使用响应对象进行cookie的设置
    response.set_cookie('a','abc')

    # 返回响应对象
    return response

#测试
def resp07(request):
    print("请求路径",request.path)
    print("请求方法",request.method)
    print("请求编码",request.encoding)
    return HttpResponse("测试request请求对象")

def verifycode(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象
    font = ImageFont.truetype('static/msyh.ttf', 23)
    #font = ImageFont.load_default().font
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    #request.session['verifycode'] = rand_str
    #内存文件操作
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def timed(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)