from django.shortcuts import render
# import pywhatkit as pwk
from . import groups
from django.views.generic import TemplateView
image = ''    # example image =  'images/Hello.png'

caption = '' # example caption =  'hello'
class Homepage(TemplateView):
    template_name = 'index.html'

def send_image(request, group_id, image, caption):
    if request.method == 'GET':
        print(request.method)
    # for group_id in groups:
    #     pwk.sendwhats_image(group_id, image, caption)

    return render(request, 'index.html', )

# def send_txt(request, group_id, txt):
def send_txt(request, group_id, txt):
    # for group_id in groups:
    #     pwk.sendwhatmsg_to_group_instantly(group_id, txt)

    if request.method == 'GET':
        print(request.method)
    return render(request, 'index.html', )


    # query = request.GET.get('query')
