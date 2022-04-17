from uuid import uuid4
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from guardian.shortcuts import assign_perm
from ddf import G
from apps.projects.models import Project
from apps.projects.models import ProjectAPIToken


class VulnmanAPITestCaseMixin(object):
    def init_mixin(self):
        self.pentester1 = self.create_user("pentester1", "changeme")
        self.pentester2 = self.create_user("pentester2", "changeme")
        self.pentester1.groups.add(Group.objects.get(name="pentester"))
        self.pentester2.groups.add(Group.objects.get(name="pentester"))
        self.project1 = self.create_project(creator=self.pentester1)
        self.project2 = self.create_project(creator=self.pentester2)

    def create_user(self, username, password, is_staff=False):
        email = "{username}@example.com".format(username=username)
        return User.objects.create_user(
            username, password=password, is_staff=is_staff, email=email)

    def get_url(self, endpoint, **kwargs):
        return reverse_lazy(endpoint, kwargs=kwargs)

    def create_instance(self, obj_class, **kwargs):
        return G(obj_class, **kwargs)

    def create_project(self, **kwargs):
        return self.create_instance(Project, uuid=uuid4(), **kwargs)

    def assign_permission(self, perm, user_or_group, obj=None):
        assign_perm(perm, user_or_group=user_or_group, obj=obj)

    def create_project_token(self, project, user):
        return self.create_instance(
            ProjectAPIToken, project=project, user=user)