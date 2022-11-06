import datetime
from datetime import timedelta
from rest_framework.permissions import BasePermission

class IsBookingByOwner(BasePermission):
    message = "You're not the owner of this booking to view it."

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.owner == request.user

class IsMoreThan3Days(BasePermission):
    message = "It's too early to be changed for the schedule time of departure."

    def has_object_permission(self, request, view, obj):
        today = datetime.today()
        if (obj.date - today).days >= 3 :
            return True
        else:
            return False

