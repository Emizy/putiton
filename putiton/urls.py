from django.conf.urls import url,handler400,handler403,handler404,handler500
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from put import views
import put
hander404 = put.views.handler404
hander500 = put.views.handler500
hander403 = put.views.handler403
hander400 = put.views.handler400

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', views.index, name="index"),
                  url(r'^coming', views.coming, name="coming"),
                  url(r'^det/(?P<d_id>[0-9]+)/$', views.det, name='det'),
                  url(r'^del_sub/(?P<del_id>[0-9]+)/$', views.del_sub, name='del_sub'),
                  url(r'^store/(?P<user>[\w.@+-]+)/$', views.store, name='store'),
                  url(r'^shop/(?P<user>[\w.@+-]+)/(?P<user_id>[0-9]+)/$', views.shop, name='shop'),
                  url(r'^clothing/', views.clothing, name="clothing"),
                  url(r'^bags/', views.bags, name="bags"),
                  url(r'^edit_prof/', views.edit_prof, name="edit_prof"),
                  url(r'^hairstylist/', views.hairstylist, name="hairstylist"),
                  url(r'^beads/', views.beads, name="beads"),
                  url(r'^jewelry/', views.jewelry, name="jewelry"),
                  url(r'^makeupArtist/', views.makeupArtist, name="makeupArtist"),
                  url(r'^shoes/', views.shoes, name="shoes"),
                  url(r'^watches/', views.watches, name="watches"),
                  url(r'^weddingwears/', views.weddingwears, name="weddingwears"),
                  url(r'^search/', views.search, name="search"),
                  url(r'^MeetTeam/', views.MeetTeam, name="MeetTeam"),
                  url(r'^men_search/', views.men_search, name="men_search"),
                  url(r'^women_search/', views.women_search, name="women_search"),
                  url(r'^menacc_search/', views.menacc_search, name="menacc_search"),
                  url(r'^makeup_search/', views.makeup_search, name="makeup_search"),
                  url(r'^bead_search/', views.bead_search, name="bead_search"),
                  url(r'^artist_search/', views.artist_search, name="artist_search"),
                  url(r'^register/', views.register, name="register"),
                  url(r'^login/', views.login, name="login"),
                  url(r'^cus_store/', views.cus_store, name="cus_store"),
                  url(r'^complains/', views.complains, name="complains"),
                  url(r'^logout/', views.logout, name="logout"),
                  url(r'^dashboard/', views.dashboard, name="dashboard"),
                  url(r'^supplier_reg/', views.supplier_reg, name="supplier_reg"),
                  url(r'^subscription/', views.subscription, name="subscription"),
                  url(r'^supplier_log/', views.supplier_log, name="supplier_log"),
                  url(r'^supplier_prof/', views.supplier_prof, name="supplier_prof"),
                  url(r'^supplier_logout/', views.supplier_logout, name="supplier_logout"),
                  url(r'^Ads/', views.Ads, name="Ads"),
                  url(r'^views_ads/', views.views_ads, name="views_ads"),
                  url(r'^editads/(?P<edit_id>[0-9]+)/$', views.editads, name="editads"),
                  url(r'^t/', views.t, name="t"),
                  url(r'^contact/', views.contact, name="contact"),
                  url(r'^edit_delete/', views.edit_delete, name="edit_delete"),
                  url(r'^edit/(?P<edit_id>[0-9]+)/$', views.edit, name='edit'),
                  url(r'^prod/(?P<del_id>[0-9]+)/$', views.prod, name='prod'),
                  url(r'^forget_pass/', views.forget_pass, name="forget_pass"),
                  url(r'^change_pass/', views.change_pass, name="change_pass"),
                  url(r'^success/', views.success, name="success"),
                  url(r'^about/', views.about, name="about"),
                  url(r'^faqx/', views.faqx, name="faqx"),
                  url(r'^register/', views.register, name="register"),
                  url(r'^user_complains/', views.user_complains, name="user_complains"),
                  url(r'^attachsend/', views.attachsend, name="attachsend"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
