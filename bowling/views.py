from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from bowling.models import Row, RowSession, Player, PersonalFrame, PersonalThrow
from bowling.forms import RowSessionCreateForm, PlayerForm

#####################################################################################################################################################################################################
#####################################################################################################################################################################################################
#####################################################################################################################################################################################################

# Create your views here.

class RowListView(ListView):

    template_name = "row_list.html"

    model = Row
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title":"List of row",
            })
        print(dict(context))
        return context


class RowDetailView(DetailView):

    template_name = "row_detail.html"
    model = Row

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class RowCreateView(CreateView):

    template_name = "row_create.html"

    model = RowSession
    form_class = RowSessionCreateForm


    def get(self, request, *args, **kwargs):
        data = request.GET
        user = User.objects.get(pk=request.session["_auth_user_id"])
        if data:
            row = Row.objects.get(pk = int(data.get("row")))
            self.initial = {"row": row, "user":user}
        return super().get(request, *args, **kwargs)

#####################################################################################################################################################################################################
#####################################################################################################################################################################################################
#####################################################################################################################################################################################################

class RowSessionListView(ListView):

    template_name = "row_session_list.html"

    model = Row
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title":"List of row sessions",
            })
        print(dict(context))
        return context

class RowSessionDetailView(DetailView):

    template_name = "row_session_detail.html"

    model = RowSession

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class RowSessionUpdateView(UpdateView):

    template_name = "row_session_update.html"
    model = RowSession
    form_class = RowSessionCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = context["object"]
        players = object.players.all()
        if object.players.all():
            list_of_entry = [[entry, PlayerForm(instance=entry)] for entry in players]
            context.update({"list_of_entry": list_of_entry})
        context.update({"player_form": PlayerForm})
        print(context)
        return context


class RowSessionCreateView(CreateView):

    template_name = "row_session_create.html"

    model = RowSession
    form_class = RowSessionCreateForm


    def get(self, request, *args, **kwargs):
        data = request.GET
        user = User.objects.get(pk=request.session["_auth_user_id"])
        if data:
            row = Row.objects.get(pk = int(data.get("row")))
            self.initial = {"row": row, "user":user}
        return super().get(request, *args, **kwargs)

#####################################################################################################################################################################################################
#####################################################################################################################################################################################################
#####################################################################################################################################################################################################

class PlayerListView(ListView):

    template_name = "player_list.html"

    model = Row
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title":"List of players",
            })
        print(dict(context))
        return context

class PlayerDetailView(DetailView):

    template_name = "player_detail.html"
    model = Row

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class PlayerUpdateView(UpdateView):

    template_name = "row_session_update.html"
    model = Player
    form_class = PlayerForm

class PlayerCreateView(CreateView):

    template_name = "player_create.html"

    model = Player
    form_class = PlayerForm

#####################################################################################################################################################################################################
#####################################################################################################################################################################################################
#####################################################################################################################################################################################################

class PersonalFrameListView(ListView):

    template_name = "personal_frame_list.html"

    model = Row
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title":"List of personal frames",
            })
        print(dict(context))
        return context

class PersonalFrameDetailView(DetailView):

    template_name = "personal_frame_detail.html"
    model = Row

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class PersonalFrameCreateView(CreateView):

    template_name = "personal_frame_create.html"

    model = RowSession
    form_class = RowSessionCreateForm


    def get(self, request, *args, **kwargs):
        data = request.GET
        user = User.objects.get(pk=request.session["_auth_user_id"])
        if data:
            row = Row.objects.get(pk = int(data.get("row")))
            self.initial = {"row": row, "user":user}
        return super().get(request, *args, **kwargs)

#####################################################################################################################################################################################################
#####################################################################################################################################################################################################
#####################################################################################################################################################################################################

class PersonalThrowListView(ListView):

    template_name = "personal_throw_list.html"

    model = Row
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title":"List of personal throws",
            })
        print(dict(context))
        return context

class PersonalThrowDetailView(DetailView):

    template_name = "personal_throw_detail.html"
    model = Row

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class PersonalThrowCreateView(CreateView):

    template_name = "personal_throw_create.html"

    model = RowSession
    form_class = RowSessionCreateForm


    def get(self, request, *args, **kwargs):
        data = request.GET
        user = User.objects.get(pk=request.session["_auth_user_id"])
        if data:
            row = Row.objects.get(pk = int(data.get("row")))
            self.initial = {"row": row, "user":user}
        return super().get(request, *args, **kwargs)