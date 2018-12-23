from django.conf.urls import url
from app_contacts.views import (
    ContactList,
    ContactDetail,
)

urlpatterns = [
    url(r'^$',
        ContactList.as_view(),
        name="contact-list"),
    url(r'^(?P<pk>[0-9]+)/$',
        ContactDetail.as_view(),
        name="contact-detail"),
]