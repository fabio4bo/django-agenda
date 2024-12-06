from contact import views
from django.urls import path

app_name = 'contact'

urlpatterns = [
    # path('<int:contact_id>/', views.contact, name='contact'),
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),  # logged in and owner
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),  # logged in and owner
    path('contact/create/', views.create, name='create'),  # logged in
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    # contact CRUD
    # path('contact/<int:contact_id>/update/', views.contact, name='contact'),
    # path('contact/<int:contact_id>/delete/', views.contact, name='contact'),
    # user
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),  # logged in
    path('user/update/', views.user_update, name='user_update'),  # logged in
]
