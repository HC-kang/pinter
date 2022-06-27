from typing import Optional, Type
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project


# Create your views here.
class ProjectCreateView(CreateView):
    model: Optional[Type[Project]] = Project
    form_class: Optional[Type[ProjectCreationForm]] = ProjectCreationForm
    template_name: str = 'projectapp/create.html'
    
    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView):
    model: Optional[Type[Project]] = Project
    context_object_name: Optional[str] = 'target_project'
    template_name: str = 'projectapp/detail.html'


class ProjectListView(ListView):
    model: Optional[Type[Project]] = Project
    context_object_name: Optional[str] = 'project_list'
    template_name: str = 'projectapp/list.html'
    paginate_by: int = 25