# coding: utf-8
import httplib
import json

from django.conf import settings
from django.shortcuts import render_to_response, HttpResponse
from django.template.context import RequestContext
import os
from django.core.servers.basehttp import FileWrapper

from kidness.models import Client, ClientOpinion, ClientOpinionCatalog
from program.models import Program
from django.core.mail import send_mail
import lfc.utils
import re
from program.models import Program

def handle_htc_file(request):
    filename = os.path.dirname(__file__) + "/../kidness_theme/static/pie/PIE.htc"
    wrapper = FileWrapper(open(filename))
    response = HttpResponse(wrapper, content_type='text/x-component')
    response['Content-Length'] = os.path.getsize(filename)
    return response

def validateEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return 1
    return 0

def consult_form(request):
    errors = {}
    if request.method == "POST":
        program_id = request.POST.get("program", None)
        if not request.POST.get("phone"):
            errors["phone"] = u"Введите номер телефона"
        if not request.POST.get("name"):
            errors["name"] = u"Введите имя"
        if request.POST.get("email"):
            if not validateEmail(request.POST.get("email")):
                errors["email"] = u"Введите email правильно"
        if errors:
            return HttpResponse(json.write({"errors": errors}), mimetype="application/json")
        portal = lfc.utils.get_portal()
        if program_id:
            program = Program.objects.get(id=program_id)
            subject = u"Заявка со страницы программы " + program.title
            message = u"Заявка со страницы программы " + program.title + " http://kidness.ru/" + program.get_absolute_url() + "\n"
        else:
            subject = u"Заявка"
            message = u"Заявка со страницы " + request.POST.get("url", "") + u"\n"
        message += u"Имя: " + request.POST.get("name") + u"\n"
        message += u"Телефон: " + request.POST.get("phone") + u"\n"
        message += u"Email: " + request.POST.get("email", "-") + u"\n"
        if request.POST.get("email", False):
            if request.POST.get("getnews", False):
                message += u"хочет плучать новости по email\n"
            else:
                message += u"НЕ хочет плучать новости по email\n"
        message += u"Комментарий: " + request.POST.get("comment", "-") + u"\n"
        from_email = portal.from_email
        recipient_list = portal.get_notification_emails()
        send_mail(subject, message, from_email, recipient_list,
                      fail_silently=False)
        return HttpResponse(json.write({ }), mimetype="application/json")


def vklogin(request):
    response_data = {}
    if "code" in request.GET:
        code = request.GET["code"]
        response_data["code"] = code
        host_ = "oauth.vk.com"
        url_ = "/access_token?client_id=" + settings.VK_CLIENT_ID + "&client_secret=" + settings.VK_SECRET_KEY + "&code=" + code
        conn = httplib.HTTPSConnection(host_)
        conn.request("GET", url_)
        res = conn.getresponse()
        response = res.read()
        response_dict = json.read(response)
        access_token = response_dict.get("access_token", "her")
        user_id = response_dict.get("user_id", "her")
        api_host = "api.vk.com"
        api_url = "/method/users.get?uids=" + str(user_id) + "&fields=uid,first_name,last_name,nickname,screen_name,sex,bdate,city,country,timezone,photo&access_token=" + str(access_token)
        conn = httplib.HTTPSConnection(api_host)
        conn.request("GET", api_url)
        res = conn.getresponse()
        new_response = res.read()
        new_response_list = json.read(new_response)
        new_response_list = new_response_list.get("response")
        program_list = Program.objects.all()
        if new_response_list:
            new_response_dict = new_response_list[0]
            client, created = Client.objects.get_or_create(ext_id=new_response_dict.get("uid"), service="vk")
            if new_response_dict.get("photo", ""):
                client.path_to_photo =  new_response_dict.get("photo", "")
            client.first_name =  new_response_dict.get("first_name", "")
            client.last_name =  new_response_dict.get("last_name", "")
            client.save()
        else:
            client = {}
        return render_to_response(
                              "kidness_theme/opinion_page.html", 
                              RequestContext(request, {
                                "client" : client,
                                "program_list": program_list,
                            }));
    return render_to_response(
                              "kidness_theme/opinion_page.html", 
                              RequestContext(request, {
                                "client" : None,
                                "program_list": [],
                            }));
#    return HttpResponse(u"{url:" +url_ + u",new_response:" + unicode(new_response_dict) + "}", mimetype="application/json")

def save_opinion(request):
    text = request.POST.get("opinion")
    client_id = request.POST.get("client")
    program_id = request.POST.get("program")
    if text and client_id and program_id:
        try:
            opinioncatalog, created = ClientOpinionCatalog.objects.get_or_create(content_type="clientopinioncatalog")
            if created:
                opinioncatalog.title = u"Отзывы клиентов"
                opinioncatalog.slug = "/opinions-catalog"
                opinioncatalog.exclude_from_navigation = 1
                opinioncatalog.save()
            slug_ = opinioncatalog.children.count()
            client = Client.objects.get(id=client_id)
            program = Program.objects.get(id=program_id)
            opinion = ClientOpinion()
            opinion.client = client
            opinion.title = program.title + u" " + client.last_name + u" " + client.first_name
            opinion.slug = slug_
            opinion.program = program
            opinion.text = text
            opinion.to_publish = False
            opinion.parent = opinioncatalog
            opinion.save()
        except (Exception,), inst:
            return HttpResponse(json.write({'error':unicode(inst)}), mimetype="application/json")
    return HttpResponse(json.write({}), mimetype="application/json")
