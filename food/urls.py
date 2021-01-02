from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='index'),
    path('itom/',views.itom,name='itom'),
    path('page1/',views.page1,name='page1'),
    path('<int:item_id>/',views.detail,name='detail'),
    path('add',views.add_item,name='add_item'),
    path('update/<int:id_item>/',views.edit_item,name='edit_item'),
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
    path('delete_temp',views.delete_base,name='delete_temp'),
]


urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
