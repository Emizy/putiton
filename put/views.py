import json, traceback, re, random
from django.contrib import messages
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render, redirect, render_to_response
from put.models import *


# Create your views here.
def index(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'Email' in request.session:
            sqlmp = Product.objects.filter(category="men").order_by(
                '-date')[:4]
            sqlwp = Product.objects.filter(category="women").order_by(
                '-date')[:4]
            sqlmcp = Product.objects.filter(category="men_acc").order_by(
                '-date')[:4]
            sqlbp = Product.objects.filter(category="beads").order_by(
                '-date')[:4]
            sqlmkp = Product.objects.filter(category="makeup").order_by(
                '-date')[:4]
            sqlmka = Product.objects.filter(category="makeupArtist").order_by(
                '-date')[:4]
            sqlmkh = Product.objects.filter(category="hairstyle").order_by(
                '-date')[:4]
            sup = Supplier.objects.all()
            count = sup.count()
            context = {
                'mp': sqlmp,
                'wp': sqlwp,
                'mcp': sqlmcp,
                'bp': sqlbp,
                'mkp': sqlmkp,
                'mka': sqlmka,
                "mkh": sqlmkh,
            }
            templates = 'index.html'
            return render(request, templates, context)
        else:
            try:
                sqlmp = Product.objects.filter(category="men").order_by(
                    '-date')[:4]
                sqlwp = Product.objects.filter(category="women").order_by(
                    '-date')[:4]
                sqlmcp = Product.objects.filter(category="men_acc").order_by(
                    '-date')[:4]
                sqlbp = Product.objects.filter(category="beads").order_by(
                    '-date')[:4]
                sqlmkp = Product.objects.filter(category="makeup").order_by(
                    '-date')[:4]
                sqlmka = Product.objects.filter(category="makeupArtist").order_by(
                    '-date')[:4]
                sqlmkh = Product.objects.filter(category="hairstyle").order_by(
                    '-date')[:4]
                sup = Supplier.objects.all()

            except:
                sqlmp = None
                sqlwp = None
                sqlmcp = None
                sqlbp = None
                sqlmkp = None
                sqlmka = None
                sqlmkh = None
                sup = None
            cout = sup.count()
            cout = 20 + cout
            if sqlmp or sqlbp or sqlmcp or sqlmkp or sqlwp or sqlmka or sqlmkh:
                context = {
                    'mp': sqlmp,
                    'wp': sqlwp,
                    'mcp': sqlmcp,
                    'bp': sqlbp,
                    'mkp': sqlmkp,
                    'mka': sqlmka,
                    'mkh': sqlmkh,
                    'ct': cout,
                }
                templates = 'index.html'
                return render(request, templates, context)
            else:
                context = locals()
                templates = 'index.html'
                return render(request, templates, context)


def f_details(request, women_id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        sql = Product.objects.get(id=women_id)
        name = sql.supplier
        sqlwp = Product.objects.filter(supplier=name).order_by('-date')
        if sql:
            context = {
                'sql1': sql,
                'rel': sqlwp,
                'ses': name,
            }
            template = 'f_details.html'
            return render(request, template, context)
        else:
            context = {
                'msg': "No stock available",
            }
            template = 'f_details.html'
            return render(request, template, context)


def women(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'Email' in request.session:
            email = request.session['Email']
            try:
                sqlwp = Product.objects.filter(category='women')
            except:
                sqlwp = None
            if sqlwp:
                context = {
                    'wp': sqlwp,
                    'mail': email,
                }
                template = 'women.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'women.html'
                return render(request, template, context)
        else:
            try:
                sqlwp = Product.objects.filter(category='women')
            except:
                sqlwp = None
            if sqlwp:
                context = {
                    'wp': sqlwp,
                }
                template = 'women.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'women.html'
                return render(request, template, context)


def beads(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'Email' in request.session:
            email = request.session['Email']
            try:
                sqlbp = Product.objects.filter(category='beads')
            except:
                sqlbp = None
            if sqlbp:
                context = {
                    'bp': sqlbp,
                    'mail': email,
                }
                template = 'beads.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'beads.html'
                return render(request, template, context)
        else:
            try:
                sqlbp = Product.objects.filter(category='beads')
            except:
                sqlbp = None
            if sqlbp:
                context = {
                    'bp': sqlbp,
                }
                template = 'beads.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'beads.html'
                return render(request, template, context)


def makeup(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'Email' in request.session:
            email = request.session['Email']
            try:
                sqlmkp = Product.objects.filter(category='makeup')
            except:
                sqlmkp = None
            if sqlmkp:
                context = {
                    'mkp': sqlmkp,
                    'mail': email,
                }
                template = 'makeup.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'makeup.html'
                return render(request, template, context)
        else:
            try:
                sqlmkp = Product.objects.filter(category='makeup')
            except:
                sqlmkp = None
            if sqlmkp:
                context = {
                    'mkp': sqlmkp,
                }
                template = 'makeup.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'makeup.html'
                return render(request, template, context)


def makeup_artist(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'Email' in request.session:
            email = request.session['Email']
            try:
                sqlmkp = Product.objects.filter(category='makeupArtist')
            except:
                sqlmkp = None
            if sqlmkp:
                context = {
                    'mka': sqlmkp,
                    'mail': email,
                }
                template = 'makeup_artist.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'makeup_artist.html'
                return render(request, template, context)
        else:
            try:
                sqlmkp = Product.objects.filter(category='makeupArtist')
            except:
                sqlmkp = None
            if sqlmkp:
                context = {
                    'mka': sqlmkp,
                }
                template = 'makeup_artist.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'makeup_artist.html'
                return render(request, template, context)


def stylist(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'Email' in request.session:
            email = request.session['Email']
            try:
                sqlmkp = Product.objects.filter(category='hairstyle')
            except:
                sqlmkp = None
            if sqlmkp:
                context = {
                    'mks': sqlmkp,
                    'mail': email,
                }
                template = 'stylist.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'stylist.html'
                return render(request, template, context)
        else:
            try:
                sqlmkp = Product.objects.filter(category='hairstyle')
            except:
                sqlmkp = None
            if sqlmkp:
                context = {
                    'mks': sqlmkp,
                }
                template = 'stylist.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'stylist.html'
                return render(request, template, context)


def men(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'Email' in request.session:
            email = request.session['Email']
            try:
                sqlmp = Product.objects.filter(category="men")
            except:
                sqlmp = None
            if sqlmp:
                context = {
                    'mp': sqlmp,
                    'mail': email,
                }
                template = 'men.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'men.html'
                return render(request, template, context)
        else:
            try:
                sqlmp = Product.objects.filter(category="men")
            except:
                sqlmp = None
            if sqlmp:
                context = {
                    'mp': sqlmp,
                }
                template = 'men.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'men.html'
                return render(request, template, context)


def men_acc(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'Email' in request.session:
            email = request.session['Email']
            try:
                sqlmcp = Product.objects.filter(category='men_acc')
            except:
                sqlmcp = None
            if sqlmcp:
                context = {
                    'mcp': sqlmcp,
                    'mail': email,
                }
                template = 'men_acc.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'men_acc.html'
                return render(request, template, context)
        else:
            try:
                sqlmcp = Product.objects.filter(category='men_acc')
            except:
                sqlmcp = None
            if sqlmcp:
                context = {
                    'mcp': sqlmcp,
                }
                template = 'men_acc.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'men_acc.html'
                return render(request, template, context)


def acc_details(request, acc_id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        sql = Product.objects.get(id=acc_id)
        name = sql.supplier
        sql2 = Product.objects.filter(supplier=name).order_by('-date')[:4]
        if sql:
            context = {
                'sql1': sql,
                'menacc': sql2,
                'ses': name,
            }
            template = 'acc_details.html'
            return render(request, template, context)
        else:
            context = {'msg': "No stock available", }
            template = 'm_details.html'
            return render(request, template, context)


def m_details(request, men_id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        sql = Product.objects.get(id=men_id)
        name = sql.username
        sql2 = Product.objects.filter(username=name).order_by('-date')[:4]
        if sql:
            context = {
                'sql1': sql,
                'rel': sql2,
                'ses': name,
            }
            template = 'm_details.html'
            return render(request, template, context)
        else:
            context = {'msg': "No stock available", }
            template = 'm_details.html'
            return render(request, template, context)


def r_beads(request, bead_id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        sql = Product.objects.get(id=bead_id)
        name = sql.username
        request.session['supp'] = name
        sql3 = Product.objects.filter(username=name).order_by('-date')[:2]
        if sql:
            context = {
                'sql1': sql,
                'bead': sql3,
                'ses': name,
            }
            template = 'r_beads.html'
            return render(request, template, context)
        else:
            context = {
                'msg': "No stock available",
            }
            template = 'r_beads.html'
            return render(request, template, context)


# def p_makeup(request, make_id):
#     sql = Product.objects.get(id=make_id)
#     sql2 = Product.objects.filter(category="makeup", status="Platinum").order_by('-date')[:4]
#     email = None
#     if sql:
#         context = {
#             'sql1': sql,
#             'rel': sql2,
#             'e': email,
#         }
#         template = 'p_makeup.html'
#         return render(request, template, context)
#     else:
#         context = {
#             'msg': "No stock available",
#         }
#         template = 'p_makeup.html'
#         return render(request, template, context)


def a_makeup(request, art_id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        sql = Product.objects.get(id=art_id)
        name = sql.supplier
        sql3 = Product.objects.filter(supplier=name).order_by('-date')[:4]
        if sql:
            context = {
                'sql1': sql,
                'rel': sql3,
                'ses': name,
            }
            template = 'a_makeup.html'
            return render(request, template, context)
        else:
            context = {
                'msg': "No stock available",
            }
            template = 'a_makeup.html'
            return render(request, template, context)


def d_stylist(request, sty_id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'Email' in request.session:
            sql = Product.objects.get(id=sty_id)
            email = request.session['Email']
            sql2 = Product.objects.filter(category="makeupArtist", status="Platinum").order_by('-date')[:4]
            if sql:
                context = {
                    'sql1': sql,
                    'rel': sql2,
                    'mail': email,
                }
                template = 'p_makeup.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'p_makeup.html'
                return render(request, template, context)
        else:
            sql = Product.objects.get(id=sty_id)
            sql2 = Product.objects.filter(category="makeupArtist", status="Platinum").order_by('-date')[:4]
            email = None
            if sql:
                context = {
                    'sql1': sql,
                    'rel': sql2,
                    'e': email,
                }
                template = 'p_makeup.html'
                return render(request, template, context)
            else:
                context = {
                    'msg': "No stock available",
                }
                template = 'p_makeup.html'
                return render(request, template, context)


def store(request, user):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        prof = Product.objects.filter(username=user)
        supp_name = user
        if prof:
            context = {
                'rst': prof,
                'name': supp_name,
            }
            templates = 'store.html'
            return render(request, templates, context)
        else:
            context = {
                'rst': "No Search Query",
            }
            templates = 'store.html'
            return render(request, templates, context)


# def shop(request, user , user_id):
#     assert isinstance(request, HttpRequest)
#     if request.method == 'GET':
#         prof = Product.objects.filter(username=user)
#         supp_name = user
#         if prof:
#             context = {
#                 'rst': prof,
#                 'name': supp_name,
#             }
#             templates = 'store.html'
#             return render(request, templates, context)
#         else:
#             context = {
#                 'rst': "No Search Query",
#             }
#             templates = 'store.html'
#             return render(request, templates, context)

def shop(request, user, user_id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        prof = Product.objects.get(id=user_id)
        supp_name = user
        if prof:
            context = {
                'sql1': prof,
                'name': supp_name,
            }
            templates = 'shop.html'
            return render(request, templates, context)
        else:
            context = {
                'sql1': "No Search Query",
            }
            templates = 'shop.html'
            return render(request, templates, context)


def login(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = 'login.html'
        return render(request, templates, context)
    elif request.method == 'POST':
        email = request.POST.get('email')
        try:
            sql = reg.objects.get(Email=email)
        except:
            sql = None
            print(traceback.print_exc())
        if sql:
            if sql.password == createHash(request.POST.get('password')):
                print(createHash(request.POST.get('password')))
                print(sql.password)
                request.session['userid'] = sql.id
                request.session['Email'] = sql.Email
                return redirect('/', request.session['Email'])
            else:
                print('am here')
                messages.error(request, 'Sorry! invalid password')
                return redirect('/login/')
        else:
            print('am here')
            messages.error(request, 'Sorry! invalid Email')
            return redirect('/login/')


def register(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = "register.html"
        return render(request, templates, context)
    elif request.method == 'POST':
        Register = reg()
        Register.Name = request.POST.get('fname')
        Register.Email = request.POST.get('email')
        Register.Phone = request.POST.get('phone')
        Register.password = request.POST.get('password')
        Register.save()
        context = {'successmsg': "Registration successfull Continue to login", 'user': request.POST.get('email'), }
        templates = 'register.html'
        return render(request, templates, context)


def contact(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        con = Contact()
        context = {'cmsg': "Thanks for contacting us hope to get back to you soon", }
        con.subject = request.POST.get('subject')
        con.Email = request.POST.get('Email')
        con.message = request.POST.get('message')
        con.save()
        # subject = [con.subject, con.Email]
        # message = con.message
        # from_mail = settings.EMAIL_HOST_USER
        # to_list = [from_mail]
        # send_mail(subject=subject, message=message, from_email=con.Email, recipient_list=to_list, fail_silently=False)
        return redirect(request.META.get('HTTP_REFERER'), context)


def logout(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        del request.session['userid']
        del request.session['Email']
        return redirect('/')


def profile(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'Email' in request.session:
            prof = reg.objects.get(Email=request.session['Email'])
            email = request.session['Email']

            context = {
                'profile': prof,
                'mail': email,
            }
            templates = 'profile.html'
            return render(request, templates, context)
    elif request.method == 'POST':
        if 'Email' in request.session:
            prof = reg.objects.get(id=request.session['userid'])
            print('am here')
            user_email = request.POST.get('Email')
            user_phone = request.POST.get('phone')
            match = re.match("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"
                             + "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$", user_email)
            if match != None:
                prof.Email = user_email
                prof.Phone = user_phone
                request.session['Email'] = user_email
                prof.save()
                messages.success(request, 'Profile Successfully Updated')
                return redirect('/profile/')
            else:
                messages.success(request, 'Invalid Email')
                return redirect('/profile/')


def search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        result1 = Product.objects.filter(product_name__icontains=query)
        result2 = Product.objects.filter(state__icontains=query)
        result3 = Product.objects.filter(color__icontains=query)
        result5 = Product.objects.filter(location__icontains=query)
        result6 = Product.objects.filter(price__icontains=query)
        rel = Product.objects.all().order_by('-date')[:20]
        if result1:
            context = {
                'sch': result1,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result2:
            context = {
                'sch': result2,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result3:
            context = {
                'sch': result3,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result5:
            context = {
                'sch': result5,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result6:
            context = {
                'sch': result6,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif rel:
            context = {
                'sch': rel,
            }
            templates = 'search.html'
            return render(request, templates, context)


def men_search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        result1 = Product.objects.filter(product_name__icontains=query, category="men")
        result2 = Product.objects.filter(state__icontains=query, category="men")
        result3 = Product.objects.filter(color__icontains=query, category="men")
        result5 = Product.objects.filter(location__icontains=query, category="men")
        result6 = Product.objects.filter(price__icontains=query, category="men")
        rel = Product.objects.filter(category="men").order_by('-date')[:20]
        if result1:
            context = {
                'sch': result1,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result2:
            context = {
                'sch': result2,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result3:
            context = {
                'sch': result3,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result5:
            context = {
                'sch': result5,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result6:
            context = {
                'sch': result6,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif rel:
            context = {
                'sch': rel,
            }
            templates = 'search.html'
            return render(request, templates, context)


def women_search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        result1 = Product.objects.filter(product_name__icontains=query, category="women")
        result2 = Product.objects.filter(state__icontains=query, category="women")
        result3 = Product.objects.filter(color__icontains=query, category="women")
        result5 = Product.objects.filter(location__icontains=query, category="women")
        result6 = Product.objects.filter(price__icontains=query, category="women")
        rel = Product.objects.filter(category="women").order_by('-date')[:20]
        if result1:
            context = {
                'sch': result1,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result2:
            context = {
                'sch': result2,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result3:
            context = {
                'sch': result3,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result5:
            context = {
                'sch': result5,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result6:
            context = {
                'sch': result6,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif rel:
            context = {
                'sch': rel,
            }
            templates = 'search.html'
            return render(request, templates, context)


def menacc_search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        result1 = Product.objects.filter(product_name__icontains=query, category="women")
        result2 = Product.objects.filter(state__icontains=query, category="women")
        result3 = Product.objects.filter(color__icontains=query, category="women")
        result5 = Product.objects.filter(location__icontains=query, category="women")
        result6 = Product.objects.filter(price__icontains=query, category="women")
        rel = Product.objects.filter(category="women").order_by('-date')[:20]
        if result1:
            context = {
                'sch': result1,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result2:
            context = {
                'sch': result2,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result3:
            context = {
                'sch': result3,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result5:
            context = {
                'sch': result5,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result6:
            context = {
                'sch': result6,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif rel:
            context = {
                'sch': rel,
            }
            templates = 'search.html'
            return render(request, templates, context)


def makeup_search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        result1 = Product.objects.filter(product_name__icontains=query, category="women")
        result2 = Product.objects.filter(state__icontains=query, category="women")
        result3 = Product.objects.filter(color__icontains=query, category="women")
        result5 = Product.objects.filter(location__icontains=query, category="women")
        result6 = Product.objects.filter(price__icontains=query, category="women")
        rel = Product.objects.filter(category="women").order_by('-date')[:20]
        if result1:
            context = {
                'sch': result1,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result2:
            context = {
                'sch': result2,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result3:
            context = {
                'sch': result3,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result5:
            context = {
                'sch': result5,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result6:
            context = {
                'sch': result6,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif rel:
            context = {
                'sch': rel,
            }
            templates = 'search.html'
            return render(request, templates, context)


def bead_search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        result1 = Product.objects.filter(product_name__icontains=query, category="women")
        result2 = Product.objects.filter(state__icontains=query, category="women")
        result3 = Product.objects.filter(color__icontains=query, category="women")
        result5 = Product.objects.filter(location__icontains=query, category="women")
        result6 = Product.objects.filter(price__icontains=query, category="women")
        rel = Product.objects.filter(category="women").order_by('-date')[:20]
        if result1:
            context = {
                'sch': result1,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result2:
            context = {
                'sch': result2,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result3:
            context = {
                'sch': result3,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result5:
            context = {
                'sch': result5,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result6:
            context = {
                'sch': result6,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif rel:
            context = {
                'sch': rel,
            }
            templates = 'search.html'
            return render(request, templates, context)


def artist_search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        result1 = Product.objects.filter(product_name__icontains=query, category="makeupArtist")
        result2 = Product.objects.filter(state__icontains=query, category="makeupArtist")
        result3 = Product.objects.filter(color__icontains=query, category="makeupArtist")
        result5 = Product.objects.filter(location__icontains=query, category="makeupArtist")
        result6 = Product.objects.filter(price__icontains=query, category="makeupArtist")
        rel = Product.objects.filter(category="makeupArtist").order_by('-date')[:20]
        if result1:
            context = {
                'sch': result1,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result2:
            context = {
                'sch': result2,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result3:
            context = {
                'sch': result3,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result5:
            context = {
                'sch': result5,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif result6:
            context = {
                'sch': result6,
            }
            templates = 'search.html'
            return render(request, templates, context)

        elif rel:
            context = {
                'sch': rel,
            }
            templates = 'search.html'
            return render(request, templates, context)


def edit_delete(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        print('am here')
        show = Product.objects.all()
        content = {'showprod': show, }
        templates = 'edit_delete.html'
        return render(request, templates, content)


def edit(request, edit_id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        print('am here')
        show = Product.objects.filter(id=edit_id)
        content = {'showprod': show, }
        templates = 'edit.html'
        return render(request, templates, content)
        # elif request.method == 'POST' and request.FILES['image']:
        #     if request.POST.get('category') == "":
        #         product = Product.objects.get(id=edit_id)
        #         product.price = request.POST.get('price')
        #         product.product_name = request.POST.get('product_name')
        #         product.section = request.POST.get('section')
        #         product.sup = request.POST.get('sup')
        #         product.image = request.FILES['image']
        #         product.save()
        #     context = {'msg': "Product Successfully Changed", }
        #     return redirect('/change/', context)


def prod_del(request, del_id):
    if request.method == 'GET':
        rst = Product.objects.get(id=del_id)
        rst.delete()
        context = {'msg': "Product Succesfully deleted"}
        return redirect('/change/', context)


def comment(request):
    if request.method == 'GET':
        com = Contact.objects.all()
        context = {'comment': com, }
        template = 'comment.html'
        return render(request, template, context)


def supplier_reg(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = "supplier_reg.html"
        return render(request, templates, context)
    elif request.method == 'POST':
        sup_name = request.POST.get('name')
        sup_email = request.POST.get('email')
        sup_phone = request.POST.get('phone')
        sup_company = request.POST.get('company')
        sup_address = request.POST.get('address')
        sup_state = request.POST.get('state')
        sup_pack = request.POST.get('package')
        sup_user = request.POST.get('username')
        sup_occ = request.POST.get('occupation')

        if sup_state == "Abuja":
            sup_location = request.POST.get('a')
        elif sup_state == "Abia":
            sup_location = request.POST.get('b')
        elif sup_state == "Adamawa":
            sup_location = request.POST.get('c')
        elif sup_state == "AkwaIbom":
            sup_location = request.POST.get('d')
        elif sup_state == "Anambra":
            sup_location = request.POST.get('e')
        elif sup_state == "Bauchi":
            sup_location = request.POST.get('f')
        elif sup_state == "Bayelsa":
            sup_location = request.POST.get('g')
        elif sup_state == "Benue":
            sup_location = request.POST.get('h')
        elif sup_state == "Bornu":
            sup_location = request.POST.get('i')
        elif sup_state == "CrossRiver":
            sup_location = request.POST.get('j')
        elif sup_state == "Delta":
            sup_location = request.POST.get('k')
        elif sup_state == "Ebonyi":
            sup_location = request.POST.get('l')
        elif sup_state == "Edo":
            sup_location = request.POST.get('m')
        elif sup_state == "Ekiti":
            sup_location = request.POST.get('n')
        elif sup_state == "Enugu":
            sup_location = request.POST.get('o')
        elif sup_state == "Gombe":
            sup_location = request.POST.get('p')

        elif sup_state == "Imo":
            sup_location = request.POST.get('q')
        elif sup_state == "Jigawa":
            sup_location = request.POST.get('r')
        elif sup_state == "Kaduna":
            sup_location = request.POST.get('s')
        elif sup_state == "Kano":
            sup_location = request.POST.get('t')
        elif sup_state == "Katsina":
            sup_location = request.POST.get('u')
        elif sup_state == "Kebbi":
            sup_location = request.POST.get('v')
        elif sup_state == "Kogi":
            sup_location = request.POST.get('w')
        elif sup_state == "Kwara":
            sup_location = request.POST.get('x')

        elif sup_state == "Lagos":
            sup_location = request.POST.get('y')
        elif sup_state == "Nasarawa":
            sup_location = request.POST.get('z')
        elif sup_state == "Niger":
            sup_location = request.POST.get('ab')
        elif sup_state == "Ogun":
            sup_location = request.POST.get('ac')
        elif sup_state == "Ondo":
            sup_location = request.POST.get('ad')
        elif sup_state == "Osun":
            sup_location = request.POST.get('ae')
        elif sup_state == "Oyo":
            sup_location = request.POST.get('af')
        elif sup_state == "Plateau":
            sup_location = request.POST.get('ag')

        elif sup_state == "Rivers":
            sup_location = request.POST.get('ah')
        elif sup_state == "Sokoto":
            sup_location = request.POST.get('ai')
        elif sup_state == "Taraba":
            sup_location = request.POST.get('aj')
        elif sup_state == "Yobe":
            sup_location = request.POST.get('ak')
        elif sup_state == "Zamfara":
            sup_location = request.POST.get('al')

        sup_password = request.POST.get('password')
        try:
            rst = Supplier.objects.filter(Email=sup_email)
            rstp = Supplier.objects.filter(Phone=sup_phone)
            rsp = Supplier.objects.filter(username=sup_user)
        except:
            rst = None
            rstp = None
            rsp = None
        match = re.match("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"
                         + "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$", sup_email)
        if not rst and match is not None:
            sup = Supplier()
            sup.name = sup_name
            sup.Email = sup_email
            if not rsp:
                if not rstp:
                    sup.Phone = sup_phone
                    sup.company = sup_company
                    sup.address = sup_address
                    sup.state = sup_state
                    sup.username = sup_user
                    sup.location = sup_location
                    sup.password = sup_password
                    sup.occupation = sup_occ
                    sup.save()
                    context = {
                        'successmsg': "Registration successfull Continue to login",
                        'user': request.POST.get('email'),
                    }
                    templates = 'supplier_reg.html'
                    return render(request, templates, context)
                else:
                    print("false")
                    context = {
                        'errmsg': "Phone Number Already Exit or Invalid Phone Number",
                    }
                    templates = 'supplier_reg.html'
                    return render(request, templates, context)
            else:
                print("damn")
                context = {
                    'errmsg': "Username Already Exist or Invalid Username",
                }
                templates = 'supplier_reg.html'
                return render(request, templates, context)
        else:
            print("damn")
            context = {
                'errmsg': "Email Already Exit or Invalid Email",
            }
            templates = 'supplier_reg.html'
            return render(request, templates, context)


def dashboard(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'email' in request.session:
            try:
                info = message.objects.all()
            except:
                info = None
                val = None
                # if stat is not None:
                #     if stat.status is not None:
                #         try:
                #             info = message.objects.all()
                #         except:
                #             info = None
                #         if info:
                #             kit = stat.status
                #             em = request.session['email']
                #             context = {
                #                 'read': info,
                #                 'email': em,
                #                 'yil': kit,
                #                 'fval':val.count()
                #             }
                #             template = 'dashboard.html'
                #             return render(request, template, context)
                #         else:
                #             kit = stat.status
                #             em = request.session['email']
                #             context = {
                #                 'kit': "lobe",
                #                 'email': em,
                #                 'yil': kit,
                #             }
                #             template = 'dashboard.html'
                #             return render(request, template, context)
                #     else:
            em = request.session['email']
            if info:
                context = {
                    'read': info,
                    'email': em,
                }
                print('hre')
                template = 'dashboard.html'
                return render(request, template, context)
            else:
                context = {
                    'kit': "lobe",
                    'email': em,
                }
                template = 'dashboard.html'
                return render(request, template, context)
        # else:
        #     try:
        #         info = message.objects.all()
        #     except:
        #         info = None
        #     em = request.session['email']
        #     if info:
        #         context = {
        #             'read': info,
        #             'email': em,
        #             'msg': "Kindly Update Your package to either free or Paid in order to Submit Ads"
        #         }
        #         print('fuk')
        #         template = 'dashboard.html'
        #         return render(request, template, context)
        #     else:
        #         context = {
        #             'kit': "lobe",
        #             'email': em,
        #             'msg': "Kindly Update Your package to either free or Paid in order to Submit Ads",
        #         }
        #         print('kd')
        #         template = 'dashboard.html'
        #         return render(request, template, context)
        else:
            return redirect('/supplier_log/')


def supplier_log(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = 'supplier_log.html'
        return render(request, templates, context)
    elif request.method == 'POST':
        try:
            user = request.POST.get('email')
            sql = Supplier.objects.get(Email=user)
        except:
            print(traceback.print_exc())
            sql = None
        if sql:
            if sql.password == createHash(request.POST.get('password')):
                request.session['email'] = sql.Email
                em = request.session['email']
                context = {
                    'mail': sql.Email,
                    'name': sql.name,
                    'email': em,
                }
                templates = 'dashboard.html'
                request.session['userid'] = sql.id
                request.session['email'] = sql.Email
                print(sql.password)
                return render(request, templates, context)
            else:
                messages.error(request, 'Sorry! invalid password')
                return redirect('/supplier_log/')
        else:
            print('am here')
            messages.error(request, 'Sorry! Invalid Email')
            return redirect('/supplier_log/')


def supplier_logout(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        del request.session['userid']
        del request.session['email']
        return redirect('/supplier_log/')


def subscription(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'email' in request.session:
            em = request.session['email']
            try:
                stat = packages.objects.get(supp_user__Email=request.session['email'])
            except:
                stat = None
            if stat:
                context = {
                    'email': em,
                    'lo': stat.status,
                }
                templates = 'subscription.html'
                return render(request, templates, context)
            else:
                context = {
                    'email': em,
                }
                templates = 'subscription.html'
                return render(request, templates, context)
        else:
            return redirect('/supplier_log/')
    elif request.method == 'POST':
        if 'email' in request.session:
            t_pack = request.POST.get('pack')
            pack = packages()
            trans = transaction()
            em = request.session['email']
            if t_pack == 'Free':
                sub_price = 0
                sub_stat = 'Free'
                try:
                    stat = Supplier.objects.get(Email=em)
                except:
                    stat = None
                if stat:
                    pack.status = sub_stat
                    pack.prices = sub_price
                    pack.supp_user = stat
                    pack.save()
                    em = request.session['email']
                    context = {
                        'email': em,
                        'msg': "You have successfully subscribe for free package,Your next subscription is in the next 6months",
                    }
                    template = 'subscription.html'
                    return render(request, template, context)
                else:
                    context = {
                        'msg': "Subscription not successful! Try Again Later",
                    }
                    template = 'subscription.html'
                    return render(request, template, context)
            elif t_pack == 'Silver':
                if request.FILES['image1']:
                    sub_bank = request.POST.get('silver2')
                    sub_image = request.FILES['image1']
                    sub_price = request.POST.get('silver1')
                    sub_stat = t_pack
                    stat = Supplier.objects.get(Email=em)
                    if sub_price == '500':
                        pack.supp_user = stat
                        pack.prices = sub_price
                        pack.status = sub_stat
                        trans.supp_user = stat
                        trans.bank = sub_bank
                        trans.image = sub_image
                        trans.save()
                        pack.save()
                        context = {
                            'email': em,
                            'msg': "You have successfully subscribe for Silver package,You will Recieved an email of Confirmation.Your next subscription is in the next 6months.Thank",
                        }
                        template = 'subscription.html'
                        return render(request, template, context)
                    else:
                        context = {
                            'email': em,
                            'msg': "Invalid amount,Kindly input the correct amount e.g 500",
                        }
                        template = 'subscription.html'
                        return render(request, template, context)
                else:
                    context = {
                        'email': em,
                        'msg': "Kindly Upload A Valid Image",
                    }
                    template = 'subscription.html'
                    return render(request, template, context)
            elif t_pack == 'Gold':
                if request.FILES['image2']:
                    sub_bank = request.POST.get('gold2')
                    sub_image = request.FILES['image2']
                    sub_price = request.POST.get('gold1')
                    sub_stat = t_pack
                    stat = Supplier.objects.get(Email=em)
                    if sub_price == '1000':
                        pack.supp_user = stat
                        pack.prices = sub_price
                        pack.status = sub_stat
                        trans.supp_user = stat
                        trans.bank = sub_bank
                        trans.image = sub_image
                        trans.save()
                        pack.save()
                        context = {
                            'email': em,
                            'msg': "You have successfully subscribe for Gold package,You will Recieved an email of Confirmation,Your next subscription is in the next 6months.Thank",
                        }
                        template = 'subscription.html'
                        return render(request, template, context)
                    else:
                        context = {
                            'email': em,
                            'msg': "Invalid amount,Kindly input the correct amount e.g 1000",
                        }
                        template = 'subscription.html'
                        return render(request, template, context)
                else:
                    context = {
                        'email': em,
                        'msg': "Kindly Upload A Valid Image",
                    }
                    template = 'subscription.html'
                    return render(request, template, context)
            elif t_pack == 'Platinum':
                if request.FILES['image3']:
                    sub_bank = request.POST.get('plat2')
                    sub_image = request.FILES['image3']
                    sub_price = request.POST.get('plat1')
                    sub_stat = t_pack
                    stat = Supplier.objects.get(Email=em)
                    if sub_price == '1500':
                        pack.supp_user = stat
                        pack.prices = sub_price
                        pack.status = sub_stat
                        trans.supp_user = stat
                        trans.bank = sub_bank
                        trans.image = sub_image
                        trans.save()
                        pack.save()
                        context = {
                            'email': em,
                            'msg': "You have successfully subscribe for Platinum package,You will Recieved an email of Confirmation,Your next subscription is in the next 6months.Thank",
                        }
                        template = 'subscription.html'
                        return render(request, template, context)
                    else:
                        context = {
                            'email': em,
                            'msg': "Invalid amount,Kindly input the correct amount e.g 1500",
                        }
                        template = 'subscription.html'
                        return render(request, template, context)
                else:
                    context = {
                        'email': em,
                        'msg': "Kindly Upload A Valid Image",
                    }
                    template = 'subscription.html'
                    return render(request, template, context)
        else:
            return redirect('/supplier_log/')


def Ads(request):
    if request.method == 'GET':
        if 'email' in request.session:
            supp_id = request.session['userid']
            mail = request.session['email']
            try:
                stat = packages.objects.get(supp_user__Email=mail)
                cout = Supp_Ads.objects.filter(supp_user__Email=mail)
            except:
                stat = None
                cout = None
            if stat is not None:
                if stat.status == "Free":
                    if cout.count() != 5:
                        remainder = cout.count()
                        print(remainder)
                        context = {
                            'email': mail,
                            'val': "Valid",
                            'rem': remainder,
                        }
                        templates = "Ads.html"
                        return render(request, templates, context)
                    else:
                        context = {
                            'email': mail,
                            'fail': "You have exceeded the maximun number to be submited on Free packages",
                        }
                        templates = "Ads.html"
                        return render(request, templates, context)
                elif stat.status == "Silver":
                    if cout.count() != 15:
                        remainder = cout.count()
                        context = {
                            'email': mail,
                            'val': "Valid",
                            'srem': remainder,
                        }
                        templates = "Ads.html"
                        return render(request, templates, context)
                    else:
                        context = {
                            'email': mail,
                            'fail': "You have exceeded the maximun number to be submited on Silver package,Kindly Upgrade",
                        }
                        templates = "Ads.html"
                        return render(request, templates, context)
                elif stat.status == "Gold":
                    if cout.count() != 25:
                        remainder = cout.count()
                        context = {
                            'email': mail,
                            'val': "Valid",
                            'grem': remainder,
                        }
                        templates = "Ads.html"
                        return render(request, templates, context)
                    else:
                        context = {
                            'email': mail,
                            'fail': "You have exceeded the maximun number to be submited on Gold package,Kindly Upgrade",
                        }
                        templates = "Ads.html"
                        return render(request, templates, context)
                elif stat.status == "Platinum":
                    if cout.count() != 35:
                        remainder = cout.count()
                        context = {
                            'email': mail,
                            'val': "Valid",
                            'prem': remainder,
                        }
                        templates = "Ads.html"
                        return render(request, templates, context)
                    else:
                        context = {
                            'email': mail,
                            'fail': "You have exceeded the maximun number to be submited on Platinum package,Kindly Order for package renewal",
                        }
                        templates = "Ads.html"
                        return render(request, templates, context)
            else:
                context = {
                    'email': mail,
                    'msg': "Yet to subscribe to any packages ,Click to subscribe",
                }
                templates = "Ads.html"
                return render(request, templates, context)
        else:
            return redirect('/supplier_log/')

    elif request.method == 'POST':
        if 'email' in request.session:
            mail = request.session['email']
            if request.FILES['image1'] or request.FILES['image2'] or request.FILES['image3']:
                stat = Supplier.objects.get(Email=request.session['email'])
                pack = packages.objects.get(supp_user__Email=request.session['email'])
                packss = pack.status
                rst = Supp_Ads()
                rst.supp_user = stat
                rst.stats = packss
                rst.price = request.POST.get('price')
                rst.product_name = request.POST.get('product_name')
                rst.category = request.POST.get('category')
                rst.color = request.POST.get('color')
                rst.size = request.POST.get('size')
                rst.descrip = request.POST.get('descrip')
                rst.image1 = request.FILES['image1']
                rst.image2 = request.FILES['image2']
                rst.image3 = request.FILES['image3']
                rst.save()
                context = {
                    'email': mail,
                    'succes': "You have successfully submitted an Ads ,Kindly wait for the next three working day for verification and publication on our website.Thanks",
                }
                templates = "Ads.html"
                return render(request, templates, context)
            else:
                context = {
                    'email': mail,
                    'succes': "Images can't be empty,Kindly upload an image",
                }
                templates = "Ads.html"
                return render(request, templates, context)
        else:
            return redirect('/Ads/')


def supplier_prof(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'email' in request.session:
            prof = Supplier.objects.get(Email=request.session['email'])
            email = request.session['email']
            context = {
                'profile': prof,
                'mail': email,
            }
            templates = 'supplier_prof.html'
            return render(request, templates, context)
        else:
            return redirect('/supplier_log/')


def forget_pass(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = 'forget_pass.html'
        return render(request, templates, context)
    elif request.method == 'POST':
        user_email = request.POST.get('Email')
        try:
            user = Supplier.objects.get(Email=user_email)
        except:
            user = None
        if user is not None:
            print(user.Email)
            request.session['email'] = user.Email
            request.session['userid'] = user.id
            messages.error(request, 'Email Verified ,Kindly Enter Your New Password')
            return redirect('/change_pass/', request.session['email'], request.session['userid'])
        else:
            context = {
                'msg': "Email not verified",
            }
            return redirect('/forget_pass/', context)


def change_pass(request):
    if request.method == 'GET':
        context = locals()
        templates = 'change_pass.html'
        return render(request, templates, context)
    elif request.method == 'POST':
        rest_pass = request.POST.get('pass')
        user = request.session['email']
        userid = request.session['userid']
        try:
            u_pass = Supplier.objects.get(Email=user)
        except:
            u_pass = None
        if u_pass:
            u_pass.password = createHash(rest_pass)
            i = u_pass.password
            u_pass.save()
            context = {
                'success': "Password Reset Successfully"
            }
            templates = 'success.html'
            return render(request, templates, context)
        else:
            context = {
                'errmsg': "Password Reset Not Successfully try Again",
            }
            return redirect('/forget_pass/', context)


def success(request):
    if request.method == 'GET':
        context = locals()
        templates = 'success.html'
        return render(request, templates, context)


def complains(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'email' in request.session:
            try:
                rst = chat.objects.filter(Email=request.session['email'])
            except:
                rst = None
            if rst:
                mail = request.session['email']
                context = {
                    'msg': rst,
                    'email': mail,
                }
                templates = 'complains.html'
                return render(request, templates, context)
            else:
                context = {
                    'msgs': "No Message",
                }
                templates = 'complains.html'
                return render(request, templates, context)
    elif request.method == 'POST':
        if 'email' in request.session:
            com = sup_complains()
            com_sub = request.POST.get('sub_me')
            com_full = request.POST.get('sub_desp')
            try:
                em = Supplier.objects.get(Email=request.session['email'])
            except:
                em = None
            mail = request.session['email']
            if em:
                com.supp_user = em
                com.full_com = com_full
                com.sub_com = com_sub
                com.save()
                context = {
                    'twp': "Complains / Feedback submitted successfully!! Hope to get back to you Soon.",
                    'email': mail,
                }
                templates = 'complains.html'
                return render(request, templates, context)
            else:
                mail = request.session['email']
                context = {
                    'email': mail,
                    'twps': "Error in sending Complains / Feedback submitted,Try Again!!!",
                }
                templates = 'complains.html'
                return render(request, templates, context)


def t(request):
    if request.method == 'GET':
        templates = 't.html'
        context = locals()
        return render(request, templates, context)


def MeetTeam(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = 'MeetTeam.html'
        return render(request, templates, context)
    elif request.method == 'POST':
        xpres = XpresSoft()
        x_name = request.POST.get('name')
        x_email = request.POST.get('email')
        x_phone = request.POST.get('phone')
        x_message = request.POST.get('message')

        match = re.match("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"
                         + "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$", x_email)
        if match:
            xpres.name = x_name
            xpres.email = x_email
            xpres.phone = x_phone
            xpres.message = x_message
            xpres.save()

            context = {
                'msg': "Message Successfully Submitted",
            }
            templates = 'MeetTeam.html'
            return render(request, templates, context)
        else:
            context = {
                'msg': "Invalid Email",
            }
            templates = 'MeetTeam.html'
            return render(request, templates, context)
