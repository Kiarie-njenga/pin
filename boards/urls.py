







from django.urls import path

from . import views

app_name = 'boards'

urlpatterns = [
    path('create/', views.CreateBoardView.as_view(), name='create_board'),
    path('<int:pk>/', views.board_detail, name='board_detail'),
    path('boards/<int:id>/', views.edit_board, name='edit_board'),
    path('save/<int:id>', views.save_to_board, name='save_to_board'),
    path('boards/<str:title>/', views.board_tag_search, name='boards'),
    path('remove/<int:pin_id>/<int:board_id>/', views.remove_from_board, name='remove_from_board'),
]