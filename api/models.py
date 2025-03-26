from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# NguoiDung model (equivalent to User in the sample)
class NguoiDung(models.Model):
    LOAI_NGUOI_DUNG = [
        ('KhachHang', 'Khách Hàng'),
        ('QuanTriVien', 'Quản Trị Viên'),
    ]
    mand = models.AutoField(primary_key=True)
    hoten = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True)
    matkhau = models.CharField(max_length=255, null=False)
    sdt = models.CharField(max_length=15, blank=True, null=True)
    loainguoidung = models.CharField(max_length=20, choices=LOAI_NGUOI_DUNG, default='KhachHang')
    ngaytao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "nguoidung"
        ordering = ['-ngaytao']

    def __str__(self):
        return self.hoten

# SanPham model (equivalent to Product in the sample)
class SanPham(models.Model):
    masp = models.AutoField(primary_key=True)
    tensp = models.CharField(max_length=255, null=False)
    mota = models.TextField(blank=True, null=True)
    gia = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    soluongtonkho = models.PositiveIntegerField(default=0)
    hinhanh = models.ImageField(upload_to='sanpham/', blank=True, null=True)  # Changed to ImageField
    danhmuc = models.CharField(max_length=100, blank=True, null=True)
    ngaytao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sanpham"
        ordering = ['-ngaytao']

    def __str__(self):
        return self.tensp

    @property
    def in_stock(self):
        return self.soluongtonkho > 0

# GioHang model (equivalent to a Cart, not explicitly in the sample but implied)
class GioHang(models.Model):
    magh = models.AutoField(primary_key=True)
    nguoidung = models.ForeignKey(
        NguoiDung,
        on_delete=models.CASCADE,
        related_name='giohangs'
    )

    class Meta:
        db_table = 'giohang'

    def __str__(self):
        return f"Giỏ hàng của {self.nguoidung.hoten}"

# ChiTietGioHang model (equivalent to OrderItem in the sample, but for a cart)
class ChiTietGioHang(models.Model):
    id = models.AutoField(primary_key=True)
    giohang = models.ForeignKey(
        GioHang,
        on_delete=models.CASCADE,
        related_name="chitiet"
    )
    sanpham = models.ForeignKey(
        SanPham,
        on_delete=models.CASCADE,
        related_name="chitiet_giohang"
    )
    soluong = models.PositiveIntegerField()

    class Meta:
        db_table = "chitietgiohang"
        unique_together = ('giohang', 'sanpham')

    def __str__(self):
        return f"{self.soluong} x {self.sanpham.tensp} trong giỏ hàng {self.giohang.id}"

    @property
    def item_subtotal(self):
        return self.sanpham.gia * self.soluong

# DonHang model (equivalent to Order in the sample)
class DonHang(models.Model):
    TRANG_THAI_CHOICES = [
        ('ChoXacNhan', 'Chờ Xác Nhận'),
        ('DangGiao', 'Đang Giao'),
        ('HoanThanh', 'Hoàn Thành'),
        ('DaHuy', 'Đã Hủy'),
    ]
    madh = models.AutoField(primary_key=True)
    nguoidung = models.ForeignKey(
        NguoiDung,
        on_delete=models.CASCADE,
        related_name="donhangs"
    )
    ngaydathang = models.DateTimeField(auto_now_add=True)
    tongtien = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    trangthai = models.CharField(max_length=20, choices=TRANG_THAI_CHOICES, default='ChoXacNhan')

    class Meta:
        db_table = "donhang"
        ordering = ['-ngaydathang']

    def __str__(self):
        return f"Đơn hàng {self.madh} - {self.nguoidung.hoten}"

# ChiTietDonHang model (equivalent to OrderItem in the sample)
class ChiTietDonHang(models.Model):
    id = models.AutoField(primary_key=True)
    donhang = models.ForeignKey(
        DonHang,
        on_delete=models.CASCADE,
        related_name="chitiet"
    )
    sanpham = models.ForeignKey(
        SanPham,
        on_delete=models.CASCADE,
        related_name="chitiet_donhang"
    )
    soluong = models.PositiveIntegerField()
    gia = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    class Meta:
        db_table = "chitietdonhang"
        unique_together = ('donhang', 'sanpham')

    def __str__(self):
        return f"{self.soluong} x {self.sanpham.tensp} trong đơn hàng {self.donhang.madh}"

    @property
    def item_subtotal(self):
        return self.gia * self.soluong

# ThanhToan model (not in the sample, but fine to keep)
class ThanhToan(models.Model):
    PHUONG_THUC_THANH_TOAN = [
        ('TienMat', 'Tiền Mặt'),
        ('ChuyenKhoan', 'Chuyển Khoản'),
        ('TheTinDung', 'Thẻ Tín Dụng'),
    ]
    TRANG_THAI_THANH_TOAN = [
        ('ChuaThanhToan', 'Chưa Thanh Toán'),
        ('DaThanhToan', 'Đã Thanh Toán'),
    ]
    matt = models.AutoField(primary_key=True)
    donhang = models.OneToOneField(
        DonHang,
        on_delete=models.CASCADE,
        related_name="thanhtoan"
    )
    sotien = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    phuongthucthanhtoan = models.CharField(max_length=20, choices=PHUONG_THUC_THANH_TOAN, null=False)
    trangthaithanhtoan = models.CharField(max_length=20, choices=TRANG_THAI_THANH_TOAN, default='ChuaThanhToan')
    ngaythanhtoan = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "thanhtoan"

    def __str__(self):
        return f"Thanh toán {self.matt} - Đơn hàng {self.donhang.madh}"

# DanhGia model (not in the sample, but fine to keep)
class DanhGia(models.Model):
    madg = models.AutoField(primary_key=True)
    nguoidung = models.ForeignKey(
        NguoiDung,
        on_delete=models.CASCADE,
        related_name="danhgias"
    )
    sanpham = models.ForeignKey(
        SanPham,
        on_delete=models.CASCADE,
        related_name="danhgias"
    )
    sosao = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    binhluan = models.TextField(blank=True, null=True)
    ngaydanhgia = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "danhgia"
        ordering = ['-ngaydanhgia']

    def __str__(self):
        return f"{self.nguoidung.hoten} - {self.sanpham.tensp} ({self.sosao} sao)"