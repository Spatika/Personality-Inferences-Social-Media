from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

      # ex: /pi/5/
    url(r'^(?P<instance_id>[0-9]+)/$', views.instance, name='instance'),
    # ex: /pi/5/results/
    url(r'^(?P<instance_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /pi/5/runmodel/
    url(r'^(?P<instance_id>[0-9]+)/runmodel/$', views.runmodel, name='runmodel'),

    url(r'^inputfeature/new/$', views.inputfeature_new, name='inputfeature_new'),

    url(r'^instancelist/$', views.instancelist, name='instancelist'),

    url(r'^about/$', views.about, name='about'),

]

#url() argument is a regex
