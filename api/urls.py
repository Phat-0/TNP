from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'nguoidung', NguoiDungViewSet)
router.register(r'sanpham', SanPhamViewSet)
router.register(r'giohang', GioHangViewSet)
router.register(r'chitietgiohang', ChiTietGioHangViewSet)
router.register(r'donhang', DonHangViewSet)
router.register(r'chitietdonhang', ChiTietDonHangViewSet)
router.register(r'thanhtoan', ThanhToanViewSet)
router.register(r'danhgia', DanhGiaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
