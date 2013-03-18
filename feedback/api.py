from reflection.feedback.models import Feedback
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.api import Api
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.exceptions import NotFound
from tastypie.resources import ModelResource

class DjangoAuthentication(Authentication):
    """Authenticate based upon Django session"""
    def is_authenticated(self, request, **kwargs):
        return request.user.is_authenticated()

class CommonMeta:
    authentication = DjangoAuthentication()
    authorization = Authorization()
    always_return_data = True

class FeedbackResource(ModelResource):

    class Meta(CommonMeta):
        queryset = Feedback.objects.all()
        resource_name = 'feedback'
        allowable_methods = ['post','get',]

    def obj_create(self, bundle, request=None, **kwargs):
        return super(FeedbackResource, self).obj_create(bundle, request)

    #def apply_authorization_limits(self, request, object_list):
    #    return object_list()