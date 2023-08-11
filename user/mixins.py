from django.shortcuts import render, redirect
from .models import User
from django.core.exceptions import PermissionDenied

class TodoOwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.id != kwargs['user_id']:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


class ProfileMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.id != kwargs['user_id']:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)