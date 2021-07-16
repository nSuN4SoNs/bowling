from django.urls import path
from bowling.views import (
    RowListView,
    RowDetailView,
    RowCreateView,
    RowSessionListView,
    RowSessionDetailView,
    RowSessionCreateView,
    RowSessionUpdateView,
    PlayerListView,
    PlayerDetailView,
    PlayerCreateView,
    PlayerUpdateView,
    PersonalThrowListView,
    PersonalThrowDetailView,
    PersonalThrowCreateView,
    PersonalFrameListView,
    PersonalFrameDetailView,
    PersonalFrameCreateView,
)
urlpatterns = [

    path("row/", RowListView.as_view(), name="row_list" ),

    path(
        "row/<int:pk>",
        RowDetailView.as_view(),
        name="row_detail"
    ),

    path(
        "row/create",
        RowCreateView.as_view(),
        name="row_create"
    ),



    path("row_session/", RowSessionListView.as_view(), name="row_session_list" ),

    path(
        "row_session/create",
        RowSessionCreateView.as_view(),
        name="row_session_create"
    ),

    path(
        "row_session/<int:pk>/update",
        RowSessionUpdateView.as_view(),
        name="row_session_update"
    ),

    path("row_session/<int:pk>",
        RowSessionDetailView.as_view(),
        name="row_session_detail"
    ),



    path("player/", PlayerListView.as_view(), name="player_list" ),

    path("player/create",
        PlayerCreateView.as_view(),
        name="player_create"
    ),

    path("player/<int:pk>/update",
        PlayerUpdateView.as_view(),
        name="player_update"
    ),

    path(
        "player/<int:pk>",
        PlayerDetailView.as_view(),
        name="player_detail"
    ),



    path("personal_frame/", PersonalFrameListView.as_view(), name="personal_frame" ),

    path(
        "personal_frame/<int:pk>",
        PersonalFrameDetailView.as_view(),
        name="personal_frame_detail"
    ),

    path(
        "personal_frame/create",
        PersonalFrameCreateView.as_view(),
        name="personal_frame_create"
    ),



    path("personal_throw/", PersonalThrowListView.as_view(), name="personal_throw" ),

    path(
        "personal_throw/<int:pk>",
        PersonalThrowDetailView.as_view(),
        name="personal_throw_detail"
    ),

    path(
        "personal_throw/create",
        PersonalThrowCreateView.as_view(),
        name="personal_throw_create"
    ),

]
