from django.conf.urls import url
from Apps.Usuarios.views import Registrousuario

urlpatterns =[
    url(r'^usuario/registrar', Registrousuario.as_view(), name="registrar")
]