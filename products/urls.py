from django.urls import path,include
from .views import ProductList, ProductDetail, BrandList, BrandDetail,CategoryList, product_list
from .api import ProductListApi,ProductDetailApi,CategoryListApi,CategoryDetailApi,CategoryDetailApi, BrandListApi,BrandDetailApi,ProductViewSet

app_name = 'products'


from rest_framework import routers


router = routers.DefaultRouter()
router.register('myproducts',ProductViewSet)



urlpatterns = [
    path('testing/', product_list),
    
    path('', ProductList.as_view(), name='product_list'),
    path('brands/<int:pk>', BrandDetail.as_view(),name='brand_detail'),
    path('brands/', BrandList.as_view(), name='brand_list'),
    
    path('<int:pk>', ProductDetail.as_view(),name='product_detail'),
    path('category/', CategoryList.as_view(), name='category_list'),




    # path('api/list', product_list_api),
    # path('api/list/<int:id>', product_detail),



    path('api/list/cbv/', ProductListApi.as_view()),
    path('api/list/cbv/<int:pk>', ProductDetailApi.as_view()),

    path('api/category', CategoryListApi.as_view()),
    path('api/category/<int:pk>', CategoryDetailApi.as_view()),


    path('api/brand', BrandListApi.as_view()),
    path('api/brand/<int:pk>', BrandDetailApi.as_view()),




    path('myapi/', include(router.urls))


    

    
    
]

