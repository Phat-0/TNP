from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *

class NguoiDungViewSet(viewsets.ModelViewSet):
    queryset = NguoiDung.objects.all()
    serializer_class = NguoiDungSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SanPhamViewSet(viewsets.ModelViewSet):
    queryset = SanPham.objects.all()
    serializer_class = SanPhamSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GioHangViewSet(viewsets.ModelViewSet):
    queryset = GioHang.objects.all()
    serializer_class = GioHangSerializer


class ChiTietGioHangViewSet(viewsets.ModelViewSet):
    queryset = ChiTietGioHang.objects.all()
    serializer_class = ChiTietGioHangSerializer


class DonHangViewSet(viewsets.ModelViewSet):
    queryset = DonHang.objects.all()
    serializer_class = DonHangSerializer


class ChiTietDonHangViewSet(viewsets.ModelViewSet):
    queryset = ChiTietDonHang.objects.all()
    serializer_class = ChiTietDonHangSerializer


class ThanhToanViewSet(viewsets.ModelViewSet):
    queryset = ThanhToan.objects.all()
    serializer_class = ThanhToanSerializer


class DanhGiaViewSet(viewsets.ModelViewSet):
    queryset = DanhGia.objects.all()
    serializer_class = DanhGiaSerializer
