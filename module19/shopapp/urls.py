from rest_framework.routers import SimpleRouter
from .views import ItemsPage, ItemEdit
from django.urls import path

router = SimpleRouter()
router.register('api/items', ItemsPage)

urlpatterns = [
    path('api/edit-items/', ItemEdit.as_view())
]
urlpatterns += router.urls
