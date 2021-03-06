import json, traceback, re, random, string
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from ipaddress import ip_address
from datetime import date, datetime, timedelta
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError, EmailMessage, EmailMultiAlternatives
from django.template import RequestContext
from django.http import HttpRequest, JsonResponse, HttpResponse, Http404
from django.shortcuts import render, redirect, render_to_response
from put.models import *
from putiton import settings


def index(request):
    try:
        client_address = request.META.get('HTTP_X_FORWARDED_FOR')
        # client_address = request.META.get('REMOTE_ADDR')
        print(client_address)
        sqlbp = Product.objects.all().order_by(
            '-date')
        # sqlbp = Product.objects.all()
        paginator = Paginator(sqlbp, 20)
        try:
            page = int(request.GET.get('page', '1'))
            cout = Supplier.objects.all().count()
            cout = cout + 10
        except ValueError:
            page = 1
            cout = None
        try:
            list = paginator.page(page)
        except (EmptyPage, InvalidPage):
            list = paginator.page(paginator.num_pages)

        return render(request, 'index.html', {"list": list, "cout": cout, })
    except Exception:
        context = locals()
        template = '404.html'
        return render(request, template, context)


def coming(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = 'comingsoon.html'
        return render(request, templates, context)
    elif request.method == 'POST':
        xpres = XpresSoft()
        x_name = "XpresSoft"
        x_email = request.POST.get('email')
        x_phone = "XpresSoft"
        x_message = "Subscribe"

        match = re.match("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"
                         + "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$", x_email)
        if match:
            xpres.name = x_name
            xpres.email = x_email
            xpres.phone = x_phone
            xpres.message = x_message
            xpres.save()

            context = {
                'msg': "Subscription Successful",
            }
            templates = 'comingsoon.html'
            return render(request, templates, context)
        else:
            context = {
                'msg': "Invalid Email",
            }
            templates = 'comingsoon.html'
            return render(request, templates, context)


def det(request, d_id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        try:
            details = Product.objects.get(id=d_id)
            name = details.supp_user.username
            del_details = Product.objects.filter(supp_user__username=name).order_by('-date')[:2]
            a = details.post_view + 1
            details.post_view = a
            details.save()
            print(a)
            if details:
                name = details.supp_user.username
                context = {
                    'del': details,
                    'ses': name,
                    'del2': del_details,
                }
                templates = 'det.html'
                return render(request, templates, context)
            else:
                context = {
                    'msg': "Error",
                }
                return redirect('/', context)

        except Product.DoesNotExist:
            context = locals()
            templates = '500.html'
            return render(request, templates, context)
        except Exception:
            context = locals()
            templates = 'err.html'
            return render(request, templates, context)


def beads(request):
    if request.method == 'GET':
        try:
            sqlbp = Product.objects.filter(category="Beads", moderate="Yes").order_by(
                '-date')
            paginator = Paginator(sqlbp, 20)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                list = paginator.page(page)
            except (EmptyPage, InvalidPage):
                list = paginator.page(paginator.num_pages)
            if list:
                return render_to_response('beads.html', {"list": list})
            else:
                err = "No Available stock ,Register to be the first Beads Supplier"
                return render_to_response('beads.html', {"err": err})
        except Exception:
            context = locals()
            templates = 'err.html'
            return render(request, templates, context)


def bags(request):
    if request.method == 'GET':
        try:
            sqlbp = Product.objects.filter(category="Bags", moderate="Yes").order_by(
                '-date')
            paginator = Paginator(sqlbp, 20)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                list = paginator.page(page)
            except (EmptyPage, InvalidPage):
                list = paginator.page(paginator.num_pages)
            if list:
                return render_to_response('Bags.html', {"list": list})
            else:
                err = "No Available stock ,Register to be the first Bags Supplier"
                return render_to_response('Bags.html', {"err": err})
        except Exception:
            context = locals()
            templates = 'err.html'
            return render(request, templates, context)


def clothing(request):
    if request.method == 'GET':
        try:
            sqlbp = Product.objects.filter(category="Clothing", moderate="Yes").order_by(
                '-date')
            paginator = Paginator(sqlbp, 20)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                list = paginator.page(page)
            except (EmptyPage, InvalidPage):
                list = paginator.page(paginator.num_pages)
            if list:
                return render_to_response('Clothing.html', {"list": list})
            else:
                err = "No Available stock ,Register to be the first Clothing Supplier"
                return render_to_response('Clothing.html', {"err": err})

        except Exception:
            context = locals()
            templates = 'err.html'
            return render(request, templates, context)


def hairstylist(request):
    if request.method == 'GET':
        try:
            sqlbp = Product.objects.filter(category="Hairstylist", moderate="Yes").order_by(
                '-date')
            paginator = Paginator(sqlbp, 20)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                list = paginator.page(page)
            except (EmptyPage, InvalidPage):
                list = paginator.page(paginator.num_pages)
            if list:
                return render_to_response('Hairstylist.html', {"list": list})
            else:
                err = "No Available stock ,Register to be the first Haristylist"
                return render_to_response('Hairstylist.html', {"err": err})
        except Exception:
            context = locals()
            templates = 'err.html'
            return render(request, templates, context)


def jewelry(request):
    if request.method == 'GET':
        try:
            sqlbp = Product.objects.filter(category="Jewelry", moderate="Yes").order_by(
                '-date')
            paginator = Paginator(sqlbp, 20)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                list = paginator.page(page)
            except (EmptyPage, InvalidPage):
                list = paginator.page(paginator.num_pages)
            if list:
                return render_to_response('Jewelry.html', {"list": list})
            else:
                err = "No Available stock ,Register to be the first jewellry Supplier"
                return render_to_response('Jewelry.html', {"err": err})
        except Exception:
            context = locals()
            templates = 'err.html'
            return render(request, templates, context)


def makeupArtist(request):
    if request.method == 'GET':
        try:
            sqlbp = Product.objects.filter(category="MakeupArtist", moderate="Yes").order_by(
                '-date')
            paginator = Paginator(sqlbp, 20)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                list = paginator.page(page)
            except (EmptyPage, InvalidPage):
                list = paginator.page(paginator.num_pages)
            if list:
                return render_to_response('MakeupArtist.html', {"list": list})
            else:
                err = "No Available stock ,Register to be the first Makeup-Artist"
                return render_to_response('MakeupArtist.html', {"err": err})
        except Exception:
            context = locals()
            templates = 'err.html'
            return render(request, templates, context)


def shoes(request):
    if request.method == 'GET':
        try:
            sqlbp = Product.objects.filter(category="Shoes", moderate="Yes").order_by(
                '-date')
            paginator = Paginator(sqlbp, 20)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                list = paginator.page(page)
            except (EmptyPage, InvalidPage):
                list = paginator.page(paginator.num_pages)
            if list:
                return render_to_response('Shoes.html', {"list": list})
            else:
                err = "No Available stock ,Register to be the first Shoes Supplier"
                return render_to_response('Shoes.html', {"err": err})
        except Exception:
            context = locals()
            templates = 'err.html'
            return render(request, templates, context)


def watches(request):
    if request.method == 'GET':
        try:
            sqlbp = Product.objects.filter(category="Watches", moderate="Yes").order_by(
                '-date')
            paginator = Paginator(sqlbp, 20)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                list = paginator.page(page)
            except (EmptyPage, InvalidPage):
                list = paginator.page(paginator.num_pages)
            if list:
                return render_to_response('Watches.html', {"list": list})
            else:
                err = "No Available stock ,Register to be the first Watches Supplier"
                return render_to_response('Watches.html', {"err": err})
        except Exception:
            context = locals()
            templates = 'err.html'
            return render(request, templates, context)


def weddingwears(request):
    if request.method == 'GET':
        try:
            sqlbp = Product.objects.filter(category="WeddingWears", moderate="Yes").order_by(
                '-date')
            paginator = Paginator(sqlbp, 20)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                list = paginator.page(page)
            except (EmptyPage, InvalidPage):
                list = paginator.page(paginator.num_pages)
            if list:
                return render_to_response('WeddingWears.html', {"list": list})
            else:
                err = "No Available stock ,Register to be the first Wedding gown Supplier"
                return render_to_response('WeddingWears.html', {"err": err})
        except Exception:
            context = locals()
            templates = 'err.html'
            return render(request, templates, context)


def store(request, user):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        try:
            prof = Product.objects.filter(supp_user__username=user, moderate="Yes").order_by(
                    '-date')
            aseet = Supplier.objects.get(username=user)
            a = aseet.store_visit + 1
            aseet.store_visit = a
            aseet.save()
            print(aseet.store_visit)
            if prof and aseet:
                paginator = Paginator(prof, 20)
                try:
                    page = int(request.GET.get('page', '1'))
                except ValueError:
                    page = 1
                try:
                    list = paginator.page(page)
                except (EmptyPage, InvalidPage):
                    list = paginator.page(paginator.num_pages)
                if list:
                    context = {
                        'name': aseet.company,
                        'offer': aseet.offer,
                        'hmm': aseet,
                        'list': list,
                    }
                    return render_to_response('store.html', context)
                else:

                    context = {
                        'err': "No Available stock ,Register to be the first Wedding gown Supplier"
                    }
                    return render_to_response('store.html', context)
            else:

                context = {
                    'error': "Store doesn't Exist,Kindly check your username",
                }
                templates = 'store.html'
                return render(request, templates, context)
        except Exception:
            context = locals()
            templates = 'err.html'
            return render(request, templates, context)


def shop(request, user, user_id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        try:
            try:
                prof = Product.objects.get(id=user_id)
                supp_name = user
                aseet = Supplier.objects.get(username=user)
            except:
                prof = None
                aseet = None
                supp_name = None

            if prof and aseet:
                context = {
                    'sql1': prof,
                    'name': supp_name,
                    'hmm': aseet,
                }
                templates = 'shop.html'
                return render(request, templates, context)
            else:
                context = {
                    'sql': "Oops Invalid Store name,Kindly Check your store name",
                }
                templates = 'shop.html'
                return render(request, templates, context)
        except Exception:
            context = locals()
            templates = 'err.html'
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


def contact(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        con = Contact()
        sub = request.POST.get('subject')
        em = request.POST.get('Email')
        ms = request.POST.get('message')
        if sub and em and ms:
            con.subject = request.POST.get('subject')
            con.Email = request.POST.get('Email')
            con.message = request.POST.get('message')
            con.save()
            subject = [sub, em]
            message = ms
            from_mail = settings.EMAIL_HOST_USER
            to_list = [from_mail]
            try:
                send_mail(subject=subject, message=message, from_email=from_mail, recipient_list=to_list,
                          fail_silently=False)
                context = {
                    'msg': "Response successsfully submitted",
                }
                return redirect(request.META.get('HTTP_REFERER'), context)
            except BadHeaderError:
                context = {
                    'msg': "Invalid header found",
                }
                return redirect(request.META.get('HTTP_REFERER'), context)

        else:
            context = {
                'msg': "Inputs can not be empty",
            }
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
        try:
            query = request.POST.get('search')
            result1 = Product.objects.filter(product_name__icontains=query, moderate="Yes")
            result2 = Product.objects.filter(supp_user__state__icontains=query, moderate="Yes")
            result3 = Product.objects.filter(supp_user__location__icontains=query, moderate="Yes")
            result4 = Product.objects.filter(category__icontains=query, moderate="Yes")
            rel = Product.objects.all().order_by('-date')
            if result1:
                paginator = Paginator(result1, 20)
                try:
                    page = int(request.GET.get('page', '1'))
                except ValueError:
                    page = 1
                try:
                    list = paginator.page(page)
                except (EmptyPage, InvalidPage):
                    list = paginator.page(paginator.num_pages)

                return render_to_response('search.html', {"list": list}, )


            elif result2:
                paginator = Paginator(result2, 20)
                try:
                    page = int(request.GET.get('page', '1'))
                except ValueError:
                    page = 1
                try:
                    list = paginator.page(page)
                except (EmptyPage, InvalidPage):
                    list = paginator.page(paginator.num_pages)

                return render_to_response('search.html', {"list": list}, )

            elif result3:
                paginator = Paginator(result3, 20)
                try:
                    page = int(request.GET.get('page', '1'))
                except ValueError:
                    page = 1
                try:
                    list = paginator.page(page)
                except (EmptyPage, InvalidPage):
                    list = paginator.page(paginator.num_pages)

                return render_to_response('search.html', {"list": list}, )
            elif result4:
                paginator = Paginator(result4, 20)
                try:
                    page = int(request.GET.get('page', '1'))
                except ValueError:
                    page = 1
                try:
                    list = paginator.page(page)
                except (EmptyPage, InvalidPage):
                    list = paginator.page(paginator.num_pages)

                return render_to_response('search.html', {"list": list}, )

            elif rel:
                paginator = Paginator(rel, 20)
                try:
                    page = int(request.GET.get('page', '1'))
                except ValueError:
                    page = 1
                try:
                    list = paginator.page(page)
                except (EmptyPage, InvalidPage):
                    list = paginator.page(paginator.num_pages)

                    return render_to_response('search.html', {"list": list}, )
        except Exception:
            context = locals()
            templates = 'err.html'
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
        templates = 'supplier_reg.html'
        return render(request, templates, context)

    elif request.method == 'POST':
        sup_name = request.POST.get('name')
        sup_email = request.POST.get('email')
        o = request.POST.get('phone')
        sup_phone = o[1:11]
        sup_company = request.POST.get('company')
        sup_address = request.POST.get('address')
        sup_state = request.POST.get('state')
        sup_pack = "Free"
        a = request.POST.get('username')
        b = a.replace(' ', '')
        punct = set(string.punctuation)
        f = ''.join(x for x in b if x not in punct)
        g = f.lower()
        sup_user = g
        sup_occ = request.POST.get('occupation')
        sup_gender = request.POST.get('gender')
        print(sup_pack)
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
        supp_confirm = request.POST.get('con_password')
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
        if sup_password == supp_confirm:
            if not rst and match is not None:
                sup = Supplier()
                sup.name = sup_name
                sup.Email = sup_email
                if not rsp:
                    if not rstp:
                        sup.gender = sup_gender
                        sup.Phone = sup_phone
                        sup.company = sup_company
                        sup.address = sup_address
                        sup.state = sup_state
                        sup.username = sup_user
                        sup.store_visit = 0
                        sup.status = sup_pack
                        sup.location = sup_location
                        sup.password = sup_password
                        sup.con_password = supp_confirm
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
        else:
            print("damn")
            context = {
                'errmsg': "Oops!!!,Password don't match.Try Again",
            }
            templates = 'supplier_reg.html'
            return render(request, templates, context)


def dashboard(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'email' in request.session:
            try:
                info = message.objects.all()
                pics = Supplier.objects.get(username=request.session['user'])
                dm = chat.objects.filter(Email=request.session['email'])
            except:
                info = None
                val = None
                pics = None
                dm = None
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
            cout = dm.count()
            print(cout)
            em = request.session['user']
            if info:
                context = {
                    'read': info,
                    'email': em,
                    'n': cout,
                }
                print('hre')
                template = 'dashboard.html'
                return render(request, template, context)
            else:
                context = {
                    'kit': "lobe",
                    'email': em,
                    'n': cout,
                }
                template = 'dashboard.html'
                return render(request, template, context)
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
                request.session['user'] = sql.username
                print(sql.password)
                return render(request, templates, context)
            else:
                context = {
                    'errmsg': "Oops !! Invalid Password",
                }
                templates = 'supplier_log.html'
                return render(request, templates, context)
        else:
            print('am here')
            context = {
                'errmsg': "Oops !! Invalid Email",
            }
            templates = 'supplier_log.html'
            return render(request, templates, context)


def supplier_logout(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        del request.session['userid']
        del request.session['email']
        return redirect('/supplier_log/')


def subscription(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        try:
            if 'email' in request.session:
                em = request.session['user']
                try:
                    stat = Supplier.objects.get(Email=request.session['email'])
                    dm = chat.objects.filter(Email=request.session['email']).count()
                except:
                    stat = None
                    dm = None
                if stat.status is not None:
                    context = {
                        'email': em,
                        'lo': stat.status,
                        'p': stat.id,
                        'h': stat.confirm,
                        'd': stat.exp_date,
                        'n': dm
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
        except Exception:
            context = locals()
            templates = 'err.html'
            return render(request, templates, context)
        
    elif request.method == 'POST':
        try:
            if 'email' in request.session:
                t_pack = request.POST.get('pack')
                pack = Supplier.objects.get(Email=request.session['email'])
                trans = transaction()
                today = date.today()
                em = request.session['email']
                uem = request.session['user']
                # if t_pack == 'Free':
                #     sub_price = 0
                #     sub_stat = 'Free'
                #     pack.status = sub_stat
                #     pack.prices = sub_price
                #     pack.save()
                #     em = request.session['user']
                #     context = {
                #         'email': em,
                #         'msg': "You have successfully subscribe for free package,Your next subscription is in the next 6months",
                #     }
                #     template = 'subscription.html'
                #     return render(request, template, context)
                if t_pack == 'Silver':
                    if request.FILES['image1']:
                        sub_bank = request.POST.get('silver2')
                        sub_image = request.FILES['image1']
                        sub_price = request.POST.get('silver1')
                        sub_stat = t_pack
                        date_after = today + timedelta(31)
                        stat = Supplier.objects.get(Email=em)
                        if sub_price == '500':
                            pack.prices = sub_price
                            pack.status = sub_stat
                            trans.supp_user = stat
                            pack.sub_date = today
                            pack.exp_date = date_after
                            trans.bank = sub_bank
                            trans.image = sub_image
                            trans.save()
                            pack.save()
                            context = {
                                'email': uem,
                                'msg': "You have successfully Submitted Silver Package Subscription, Kindly wait for two working days for Subscription activation",
                            }
                            template = 'subscription.html'
                            return render(request, template, context)
                        else:
                            context = {
                                'email': uem,
                                'msg': "Invalid amount,Kindly input the correct amount e.g 500",
                            }
                            template = 'subscription.html'
                            return render(request, template, context)
                    else:
                        context = {
                            'email': uem,
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
                        print(t_pack)
                        date_after = today + timedelta(31)
                        stat = Supplier.objects.get(Email=em)
                        if sub_price == '1000':
                            pack.prices = sub_price
                            pack.status = sub_stat
                            trans.supp_user = stat
                            pack.sub_date = today
                            pack.exp_date = date_after
                            trans.bank = sub_bank
                            trans.image = sub_image
                            trans.save()
                            pack.save()
                            context = {
                                'email': uem,
                                'msg': "You have successfully Submitted Gold Package Subscription, Kindly wait for two working days for Subscription activation",
                            }
                            template = 'subscription.html'
                            return render(request, template, context)
                        else:
                            context = {
                                'email': uem,
                                'msg': "Invalid amount,Kindly input the correct amount e.g 1000",
                            }
                            template = 'subscription.html'
                            return render(request, template, context)
                    else:
                        context = {
                            'email': uem,
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
                        date_after = today + timedelta(31)
                        stat = Supplier.objects.get(Email=em)
                        if sub_price == '2000':
                            pack.prices = sub_price
                            pack.status = sub_stat
                            trans.supp_user = stat
                            pack.sub_date = today
                            pack.exp_date = date_after
                            trans.bank = sub_bank
                            trans.image = sub_image
                            trans.save()
                            pack.save()
                            context = {
                                'email': uem,
                                'msg': "You have successfully Submitted Silver Package Subscription, Kindly wait for two working days for Subscription activation",
                            }
                            template = 'subscription.html'
                            return render(request, template, context)
                        else:
                            context = {
                                'email': uem,
                                'msg': "Invalid amount,Kindly input the correct amount e.g 2000",
                            }
                            template = 'subscription.html'
                            return render(request, template, context)
                    else:
                        context = {
                            'email': uem,
                            'msg': "Kindly Upload A Valid Image",
                        }
                        template = 'subscription.html'
                        return render(request, template, context)
            else:
                return redirect('/supplier_log/')
        except Exception:
            context = locals()
            templates = 'err.html'
            return render(request, templates, context)


def del_sub(request, del_id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'email' in request.session:
            em = request.session['email']
            try:
                k = Supplier.objects.get(id=del_id)
            except:
                k = None
            if k:
                del k.status
                del k.confirm
                del k.exp_date
                del k.sub_date
                p = "NoSub"
                t = "Nil"
                k.status = p
                k.confirm = t
                k.save()
                context = {
                    'email': em,
                    'lo': k.status,
                    'p': k.id,
                }
                templates = 'subscription.html'
                return render(request, templates, context)

            else:
                context = {
                    'email': em,
                    'lo': k.status,
                    'p': k.id,
                    'err': "Activation not successful",
                }
                templates = 'subscription.html'
                return render(request, templates, context)


def Ads(request):
    if request.method == 'GET':
        if 'email' in request.session:
            try:
                supp_id = request.session['userid']
                mail = request.session['email']
                user = request.session['user']
                try:
                    stat = Supplier.objects.get(Email=request.session['email'])
                    cout = Product.objects.filter(supp_user__Email=mail)
                    dm = chat.objects.filter(Email=request.session['email']).count()
                except:
                    stat = None
                    cout = None
                    dm = None
                remainder = cout.count()
                if stat:
                    if stat.status == "Free":
                        if cout.count() != 10:
                            remainder = cout.count()
                            context = {
                                'email': user,
                                'val': "Valid",
                                'rem': remainder,
                                'n': dm,
                            }
                            templates = "Ads.html"
                            return render(request, templates, context)
                        else:
                            context = {
                                'email': user,
                                'n': dm,
                                'fail': "You have exceeded the maximun number to be submited on Trial package",
                            }
                            templates = "Ads.html"
                            return render(request, templates, context)
                    elif stat.status == "Silver" and stat.confirm == "APPROVED":
                        today = datetime.today()
                        k = str(stat.exp_date)
                        print(remainder)
                        p = datetime.strptime(k, "%Y-%m-%d")
                        print(p)
                        if today <= p:
                            context = {
                                'email': user,
                                'val': "Valid",
                                'n': dm,
                                'srem': remainder,
                            }
                            templates = "Ads.html"
                            return render(request, templates, context)
                        else:
                            context = {
                                'email': user,
                                'n': dm,
                                'fail': "Your Subscription has expired,Kindly Re-Subscribe for another 1month",
                            }
                            templates = "Ads.html"
                            return render(request, templates, context)
                    elif stat.status == "Gold" and stat.confirm == "APPROVED":
                        today = datetime.today()
                        k = str(stat.exp_date)
                        p = datetime.strptime(k, "%Y-%m-%d")
                        print(p)
                        if today <= p:
                            context = {
                                'email': user,
                                'val': "Valid",
                                'srem': remainder,
                                'n': dm,
                            }
                            templates = "Ads.html"
                            return render(request, templates, context)
                        else:
                            context = {
                                'email': user,
                                'n': dm,
                                'fail': "Your Subscription has expired,Kindly Re-Subscribe for another 2month",
                            }
                            templates = "Ads.html"
                            return render(request, templates, context)
                    elif stat.status == "Platinum" and stat.confirm == "APPROVED":
                        today = datetime.today()
                        k = str(stat.exp_date)
                        p = datetime.strptime(k, "%Y-%m-%d")
                        print(p)
                        if today <= p:
                            context = {
                                'email': user,
                                'val': "Valid",
                                'srem': remainder,
                                'n': dm,
                            }
                            templates = "Ads.html"
                            return render(request, templates, context)
                        else:
                            context = {
                                'email': user,
                                'n': dm,
                                'fail': "Your Subscription has expired,Kindly Re-Subscribe for another 3month",
                            }
                            templates = "Ads.html"
                            return render(request, templates, context)
                    elif stat.status == 'NoSub' and stat.confirm == 'Nil':
                        context = {
                            'email': user,
                            'n': dm,
                            'msg': "Yet to subscribe to any packages or Waiting for Payment Approval,Click to subscribe",
                        }
                        templates = "Ads.html"
                        return render(request, templates, context)
                    else:
                        context = {
                            'email': user,
                            'n': dm,
                            'msg': "Yet to subscribe to any packages or Waiting for Payment Approval,Click to subscribe",
                        }
                        templates = "Ads.html"
                        return render(request, templates, context)

                else:
                    context = {
                        'email': user,
                        'msg': "Yet to subscribe to any packages or Waiting for Payment Approval,Click to subscribe",
                    }
                    templates = "Ads.html"
                    return render(request, templates, context)
            except Exception:
                context = locals()
                templates = 'err.html'
                return render(request, templates, context)
        else:
            return redirect('/supplier_log/')

    elif request.method == 'POST':
        if 'email' in request.session:
            try:
                mail = request.session['email']
                dm = chat.objects.filter(Email=request.session['email']).count()
                if request.FILES['image1'] and request.FILES['image2'] and request.FILES['image3']:
                    stat = Supplier.objects.get(Email=request.session['email'])
                    rst = Product()
                    rst.supp_user = stat
                    rst.post_view = 0
                    rst.price = request.POST.get('price')
                    rst.product_name = request.POST.get('product_name')
                    rst.category = request.POST.get('category')
                    rst.color = request.POST.get('color')
                    rst.text = request.POST.get('wtext')
                    rst.size = request.POST.get('size')
                    rst.descrip = request.POST.get('descrip')
                    rst.image1 = request.FILES['image1']
                    rst.image2 = request.FILES['image2']
                    rst.image3 = request.FILES['image3']
                    rst.save()
                    context = {
                        'email': mail,
                        'n': dm,
                        'succes': "You have successfully submitted an Ads ,Kindly wait for the next three working day for verification and publication on our website.Thanks",
                    }
                    templates = "Ads.html"
                    return render(request, templates, context)
                else:
                    context = {
                        'email': mail,
                        'n': dm,
                        'succes': "One Image slot or All images slot is empty,Kindly upload an image",
                    }
                    templates = "Ads.html"
                    return render(request, templates, context)
            except Exception:
                context = locals()
                templates = 'err.html'
                return render(request, templates, context)
        else:
            return redirect('/supplier_log/')


def cus_store(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'user' in request.session:
            try:
                try:
                    foo = Supplier.objects.get(username=request.session['user'])
                    dm = chat.objects.filter(Email=request.session['email']).count()
                except:
                    foo = None
                    dm = None
                em = request.session['user']
                if foo.offer is not None:
                    context = {
                        'email': em,
                        'dis': foo,
                        'n': dm,
                    }
                    templates = 'customize.html'
                    return render(request, templates, context)
                else:
                    context = {
                        'email': em,
                        'b': "Empty",
                        'n': dm,
                    }
                    templates = 'customize.html'
                    return render(request, templates, context)
            except Exception:
                context = locals()
                templates = 'err.html'
                return render(request, templates, context)
        else:
            return redirect('/supplier_log/')

    elif request.method == 'POST':
        if 'user' in request.session:
            try:
                try:
                    off = Supplier.objects.get(username=request.session['user'])
                    dm = chat.objects.filter(Email=request.session['email']).count()
                except:
                    off = None
                    dm = None
                offer = request.POST.get('offer')
                off.offer = offer
                off.save()
                dis = Supplier.objects.get(username=request.session['user'])
                em = request.session['user']
                context = {
                    'dis': dis,
                    'email': em,
                    'n': dm,

                }
                templates = 'customize.html'
                return render(request, templates, context)
            except Exception:
                context = locals()
                templates = 'err.html'
                return render(request, templates, context)
        else:
            return redirect('/supplier_log/')


def views_ads(request):
    if request.method == 'GET':
        if 'user' in request.session:
            view = Product.objects.filter(supp_user__username=request.session['user'])
            dm = chat.objects.filter(Email=request.session['email']).count()
            em = request.session['user']
            if view:
                context = {
                    'email': em,
                    'v': view,
                    'n': dm,
                }
                templates = 'views_ads.html'
                return render(request, templates, context)
            else:
                context = {
                    'email': em,
                    'n': dm,
                }
                templates = 'views_ads.html'
                return render(request, templates, context)


def editads(request, edit_id):
    if request.method == 'POST':
        if 'user' in request.session:
            em = request.session['user']
            rst = Product.objects.get(id=edit_id)
            rst.price = request.POST.get('price')
            rst.product_name = request.POST.get('product_name')
            rst.category = request.POST.get('category')
            rst.color = request.POST.get('color')
            rst.text = request.POST.get('wtext')
            rst.size = request.POST.get('size')
            rst.descrip = request.POST.get('descrip')
            rst.save()
            vi = Product.objects.filter(supp_user__username=request.session['user'])
            dm = chat.objects.filter(Email=request.session['email']).count()
            context = {
                'email': em,
                'v': vi,
                'n': dm,
                'succes': "Products Updated Successfully",
            }
            templates = "views_ads.html"
            return render(request, templates, context)


def prod(request, del_id):
    if request.method == 'GET':
        rst = Product.objects.get(id=del_id)
        rst.delete()
        em = request.session['user']
        vi = Product.objects.filter(supp_user__username=request.session['user'])
        dm = chat.objects.filter(Email=request.session['email']).count()
        context = {
            'v': vi,
            'n': dm,
            'email': em,
            'succes': "Product Successfully deleted",
        }
        templates = 'views_ads.html'
        return render(request, templates, context)


def supplier_prof(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'email' in request.session:
            prof = Supplier.objects.get(Email=request.session['email'])
            dm = chat.objects.filter(Email=request.session['email']).count()
            em = request.session['user']
            context = {
                'profile': prof,
                'n': dm,
                'email': em,
            }
            templates = 'supplier_prof.html'
            return render(request, templates, context)
        else:
            return redirect('/supplier_log/')
    elif request.method == 'POST':
        if 'email' in request.session:
            doc_user = request.session['user']
            prof = Supplier.objects.get(Email=request.session['email'])
            dm = chat.objects.filter(Email=request.session['email']).count()
            doc_image = request.FILES['image']
            if doc_image:
                try:
                    d = Supplier.objects.get(username=doc_user)
                except:
                    d = None
                if d:
                    d.image = doc_image
                    d.save()
                    print('am here')
                    context = {
                        'msg': "image uploaded successfully",
                        'profile': prof,
                        'n': dm,
                        'email': doc_user,
                    }
                    return redirect('/supplier_prof/', context)
                else:
                    context = {
                        'msg': "image uploaded not successful",
                        'profile': prof,
                        'n': dm,
                    }
                    return redirect('/supplier_prof/', context)

            else:
                prof = Supplier.objects.get(username=request.session['user'])
                dm = chat.objects.filter(Email=request.session['email']).count()
                doc_user = request.session['user']
                context = {
                    'msg': "Image can't be empty",
                    'profile': prof,
                    'email': doc_user,
                    'n': dm,
                }
                templates = 'supplier_prof.html'
                return render(request, templates, context)


def edit_prof(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        if 'user' in request.session:
            doc_user = request.session['user']
            prof = Supplier.objects.get(Email=request.session['email'])
            doc_fname = request.POST.get('name')
            doc_email = request.POST.get('email')
            doc_gender = request.POST.get('gender')
            # o = request.POST.get('phone')
            # doc_phone = o[1:11]
            doc_state = request.POST.get('state')
            doc_local = request.POST.get('local')
            doc_address = request.POST.get('address')
            try:
                d = Supplier.objects.get(username=doc_user)
                dm = chat.objects.filter(Email=request.session['email']).count()
            except:
                d = None
                dm = None
            if d:
                d.name = doc_fname
                d.Email = doc_email
                # d.Phone = doc_phone
                d.address = doc_address
                d.state = doc_state
                d.location = doc_local
                d.gender = doc_gender
                d.save()
                print('am here')
                context = {
                    'msg': "Profile successfully Updated",
                    'profile': Supplier.objects.get(Email=request.session['email']),
                    'email': doc_user,
                    'n': dm,
                }
                templates = 'supplier_prof.html'
                return render(request, templates, context)
            else:
                context = {
                    'msg': "Profile Update not successful",
                    'profile': prof,
                    'email': doc_user,
                    'n': dm,
                }
                templates = 'supplier_prof.html'
                return render(request, templates, context)


def forget_pass(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = 'forget_pass.html'
        return render(request, templates, context)
    elif request.method == 'POST':
        user_email = request.POST.get('email')
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
        if 'email' in request.session:
            rest_pass = request.POST.get('password')
            user = request.session['email']
            userid = request.session['userid']
            try:
                u_pass = Supplier.objects.get(Email=user)
            except:
                u_pass = None
            if u_pass:
                u_pass.password = createHash(rest_pass)
                u_pass.con_password = rest_pass
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
                dm = chat.objects.filter(Email=request.session['email']).count()
            except:
                rst = None
                dm = None
            em = request.session['user']
            if rst:

                context = {
                    'msg': rst,
                    'email': em,
                    'n': dm,
                }
                templates = 'complains.html'
                return render(request, templates, context)
            else:
                context = {
                    'email': em,
                    'msgs': "No Message",
                    'n': dm,
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
                dm = chat.objects.filter(Email=request.session['email']).count()
            except:
                em = None
                dm = None
            mail = request.session['user']
            if em:
                com.supp_user = em
                com.full_com = com_full
                com.sub_com = com_sub
                com.save()
                context = {
                    'twp': "Complains / Feedback submitted successfully!! Hope to get back to you Soon.",
                    'email': mail,
                    'n': dm,
                }
                templates = 'complains.html'
                return render(request, templates, context)
            else:
                mail = request.session['user']
                context = {
                    'email': mail,
                    'n': dm,
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
        x_subject = request.POST.get('subject')
        x_phone = request.POST.get('phone')
        x_message = request.POST.get('message')
        if x_name and x_email and x_subject and x_phone and x_message:
            match = re.match("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"
                             + "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$", x_email)
            if match:
                xpres.name = x_name
                xpres.email = x_email
                xpres.phone = x_phone
                xpres.message = x_message
                subject = [x_subject, x_email]
                message = x_message
                from_mail = settings.EMAIL_HOST_USER
                to_list = [from_mail]
                xpres.save()
                try:
                    send_mail(subject=subject, message=message, from_email=from_mail, recipient_list=to_list,
                              fail_silently=False)
                    context = {
                        'msg': "Message Successfully Submitted",
                    }
                    templates = 'MeetTeam.html'
                    return render(request, templates, context)

                except BadHeaderError:
                    context = {
                        'msg': "Message not successfull",
                    }
                    templates = 'MeetTeam.html'
                    return render(request, templates, context)
            else:
                context = {
                    'msg': "Invalid Email",
                }
                templates = 'MeetTeam.html'
                return render(request, templates, context)

        else:
            context = {
                'msg': "Fields can not be empty",
            }
            templates = 'MeetTeam.html'
            return render(request, templates, context)


def about(request):
    if request.method == 'GET':
        context = locals()
        templates = 'AboutUs.html'
        return render(request, templates, context)


def faqx(request):
    if request.method == 'GET':
        context = locals()
        templates = 'faqx.html'
        return render(request, templates, context)


def user_complains(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = 'contact.html'
        return render(request, templates, context)

    elif request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and message and subject:
            user = Users_Complains()
            user.phone = phone
            user.name = name
            user.Email = email
            user.message = message
            user.save()
            subject = [subject, email, phone]
            message = message
            from_mail = settings.EMAIL_HOST_USER
            to_list = [from_mail]
            try:
                send_mail(subject=subject, message=message, from_email=from_mail, recipient_list=to_list,
                          fail_silently=False)
                context = {
                    'msg': "Response successsfully submitted",
                }
                return redirect(request.META.get('HTTP_REFERER'), context)
            except BadHeaderError:
                context = {
                    'msg': "Invalid header found",
                }
                return redirect(request.META.get('HTTP_REFERER'), context)

        else:
            context = {
                'msg': "Inputs can not be empty",
            }
            return redirect(request.META.get('HTTP_REFERER'), context)


def attachsend(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        content = request.FILES['file']
        if name and email and subject and message and content:
            subject = [subject, phone]
            from_mail = settings.EMAIL_HOST_USER
            contacat = ['nevogold.official@gmail.com']
            try:
                email = EmailMultiAlternatives(
                    subject,
                    message,
                    from_mail,
                    contacat,
                    headers={'Reply-To': contacat}
                )
                email.attach(content, content.file.read(), content.content_type)
                email.send()
            except BadHeaderError:
                context = {
                    'msg': "Invalid header found",
                }
                return redirect(request.META.get('HTTP_REFERER'), context)

        context = {
            'msg': "Inputs can not be empty",
        }
        return redirect(request.META.get('HTTP_REFERER'), context)


def handler404(request):
    response = render_to_response('404.html', context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', context_instance=RequestContext(request))
    response.status_code = 500
    return response


def handler403(request):
    response = render_to_response('403.html', context_instance=RequestContext(request))
    response.status_code = 403
    return response


def handler400(request):
    response = render_to_response('400.html', context_instance=RequestContext(request))
    response.status_code = 400
    return response
