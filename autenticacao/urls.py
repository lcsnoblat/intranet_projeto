from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, name="home"),
    url(r'^logout$', views.logout_user, name="logout"),
    url(r'^logar$',views.login_user, name='logar'),
    url(r'^esqueci$', views.change_password, name="esqueci_senha"),
    url(r'^alterar$', views.change_password_to_old, name="alterar_senha"),
    url(r'^email$', views.change_email, name="esqueci_email")

]
