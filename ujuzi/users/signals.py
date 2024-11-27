from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
        from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


User = get_user_model()

@receiver(post_save, sender=User)
def assign_user_permissions(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            """Add the superuser to the admin group"""
            admin_group, created = Group.objects.get_or_create(name="Admin")
            instance.groups.add(admin_group)
            """ Assign admin permissions"""
            admin_permissions = Permission.objects.filter(
                codename__in=[
                    "view_portal",
                    "manage_users",
                    "view_statistics",
                    "edit_system_settings",
                    "manage_assessments",
                    "manage_resources",
                    "manage_trainers",
                    "manage_teachers",
                ]
            )
            instance.user_permissions.set(admin_permissions)
        elif instance.role == "teacher":
            """Assign teacher group and permissions"""
            teacher_group, created = Group.objects.get_or_create(name="Teacher")
            instance.groups.add(teacher_group)
            teacher_permissions = Permission.objects.filter(
                codename__in=[
                    "view_assessments",
                    "do_assessments",
                    "view_resources",
                ]
            )
            instance.user_permissions.set(teacher_permissions)
        elif instance.role == "trainer":
            """Assign trainer group and permissions"""
            trainer_group, created = Group.objects.get_or_create(name="Trainer")
            instance.groups.add(trainer_group)
            trainer_permissions = Permission.objects.filter(
                codename__in=[
                    "view_assessments",
                    "create_assessments",
                    "edit_assessments",
                    "view_resources",
                    "view_statistics",
                ]
            )
            instance.user_permissions.set(trainer_permissions)
        elif instance.role == "kicd_official":
            """Assign KICD official group and permissions"""
            kicd_group, created = Group.objects.get_or_create(name="KICD Official")
            instance.groups.add(kicd_group)
            kicd_permissions = Permission.objects.filter(
                codename__in=[
                    "view_assessments",
                    "allocate_teachers_to_trainers",
                    "view_progress",
                ]
            )
            instance.user_permissions.set(kicd_permissions)
        else:
            """Default user with read-only access"""
            default_group, created = Group.objects.get_or_create(name="Default User")
            instance.groups.add(default_group)
            default_permissions = Permission.objects.filter(codename="view_portal")
            instance.user_permissions.set(default_permissions)
        
        instance.save()
        # from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class IsAuthenticatedAndHasPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.has_perm("view_portal")

class HasTeacherPermissions(BasePermission):
    """
    Custom permission for teachers.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == "teacher":
            teacher_permissions = [
                "view_assessments",
                "do_assessments",
                "view_resources",
            ]
            return all(request.user.has_perm(perm) for perm in teacher_permissions)
        return False

class HasTrainerPermissions(BasePermission):
    """
    Custom permission for trainers.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == "trainer":
            trainer_permissions = [
                "view_assessments",
                "create_assessments",
                "edit_assessments",
                "view_resources",
                "view_statistics",
            ]
            return all(request.user.has_perm(perm) for perm in trainer_permissions)
        return False

class HasAdminPermissions(BasePermission):
    """
    Custom permission for admin users with full access.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == "admin":
            admin_permissions = [
                "view_portal",
                "manage_users",
                "view_statistics",
                "edit_system_settings",
                "manage_assessments",
                "manage_resources",
                "manage_trainers",
                "manage_teachers",
            ]
            return all(request.user.has_perm(perm) for perm in admin_permissions)
        return False

class HasKICDOfficialPermissions(BasePermission):
    """
    Custom permission for KICD officials.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == "kicd_official":
            kicd_permissions = [
                "view_assessments",
                "allocate_teachers",
                "view_progress",
            ]
            return all(request.user.has_perm(perm) for perm in kicd_permissions)
        return False

class ReadOnlyAccess(BasePermission):
    """
    Custom permission to allow read-only access for authenticated users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.method in SAFE_METHODS