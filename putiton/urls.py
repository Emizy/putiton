"""PutItOn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from put import views

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', views.index, name="index"),
                  url(r'^m_details/(?P<men_id>[0-9]+)/$', views.m_details, name='m_details'),
                  url(r'^f_details/(?P<women_id>[0-9]+)/$', views.f_details, name='f_details'),
                  url(r'^r_beads/(?P<bead_id>[0-9]+)/$', views.r_beads, name='r_beads'),
                  url(r'^p_makeup/(?P<make_id>[0-9]+)/$', views.p_makeup, name='p_makeup'),
                  url(r'^acc_details/(?P<acc_id>[0-9]+)/$', views.acc_details, name='acc_details'),
                  url(r'^women/', views.women, name="women"),
                  url(r'^men/', views.men, name="men"),
                  url(r'^men_acc/', views.men_acc, name="men_acc"),
                  url(r'^beads/', views.beads, name="beads"),
                  url(r'^makeup/', views.makeup, name="makeup"),
                  url(r'^search/', views.search, name="search"),
                  url(r'^men_search/', views.men_search, name="men_search"),
                  url(r'^women_search/', views.women_search, name="women_search"),
                  url(r'^menacc_search/', views.menacc_search, name="menacc_search"),
                  url(r'^makeup_search/', views.makeup_search, name="makeup_search"),
                  url(r'^bead_search/', views.bead_search, name="bead_search"),
                  url(r'^checkout/', views.checkout, name="checkout"),
                  url(r'^register/', views.register, name="register"),
                  url(r'^login/', views.login, name="login"),
                  url(r'^profile/', views.profile, name="profile"),
                  url(r'^history/', views.history, name="history"),
                  url(r'^complains/', views.complains, name="complains"),
                  url(r'^logout/', views.logout, name="logout"),
                  url(r'^dashboard/', views.dashboard, name="dashboard"),
                  url(r'^supplier_reg/', views.supplier_reg, name="supplier_reg"),
                  url(r'^subscription/', views.subscription, name="subscription"),
                  url(r'^supplier_log/', views.supplier_log, name="supplier_log"),
                  url(r'^supplier_prof/', views.supplier_prof, name="supplier_prof"),
                  url(r'^supplier_logout/', views.supplier_logout, name="supplier_logout"),
                  url(r'^Ads/', views.Ads, name="Ads"),
                  url(r'^t/', views.t, name="t"),
                  url(r'^contact/', views.contact, name="contact"),
                  url(r'^edit_delete/', views.edit_delete, name="edit_delete"),
                  url(r'^edit/(?P<edit_id>[0-9]+)/$', views.edit, name='edit'),
                  url(r'^prod_del/(?P<del_id>[0-9]+)/$', views.prod_del, name='prod_del'),
                  url(r'^forget_pass/', views.forget_pass, name="forget_pass"),
                  url(r'^change_pass/', views.change_pass, name="change_pass"),
                  url(r'^success/', views.success, name="success"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
