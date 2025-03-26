from rest_framework import serializers
from .models import *

# Serializer cho người dùng
class NguoiDungSerializer(serializers.ModelSerializer):
    class Meta:
        model = NguoiDung
        fields = '__all__'

# Serializer cho sản phẩm
class SanPhamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanPham
        fields = '__all__'

# Serializer cho giỏ hàng
class GioHangSerializer(serializers.ModelSerializer):
    class Meta:
        model = GioHang
        fields = '__all__'

# Serializer cho chi tiết giỏ hàng
class ChiTietGioHangSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChiTietGioHang
        fields = '__all__'

# Serializer cho đơn hàng
class DonHangSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonHang
        fields = '__all__'

# Serializer cho chi tiết đơn hàng
class ChiTietDonHangSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChiTietDonHang
        fields = '__all__'

# Serializer cho thanh toán
class ThanhToanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThanhToan
        fields = '__all__'

# Serializer cho đánh giá
class DanhGiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanhGia
        fields = '__all__'
