from django.urls import path
from author.views import AuthorViewSet


author_list = AuthorViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

author_detail = AuthorViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("author/", author_list, name="author_list"),
    path("author/<int:pk>/", author_detail, name="author_detail"),
]


app_name = "author"
