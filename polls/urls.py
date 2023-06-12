from django.urls import path

from . import views

urlpatterns = [
    #左から
    #URLパターン
    #URLパターンにマッチしたときに実行されるPython関数(viewsモジュールの中のindex関数)
    #URLパターンに名前を付けるためのオプション
    path("", views.index, name="index"),

    path("home/", views.home),
    path("photo/", views.photos),
    path("portfolio/", views.portfolio),
    path("portfolio/<int:portfolio_id>/", views.portfolio_details, name='portfolio_details'),

]