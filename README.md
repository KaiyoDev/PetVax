# 🐾 PetVax - Hệ Thống Quản Lý Tiêm Chủng Thú Cưng

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-lightgrey)
![Status](https://img.shields.io/badge/Status-Development-yellow)

## Bắt Đầu Nhanh

### Yêu Cầu Hệ Thống
- Python 3.10+
- Git
- Rect JS

### ⚙️ Cài Đặt
```bash
# 1. Clone dự án
git clone https://github.com/KaiyoDev/PetVax.git
cd PetVax

# 2. Cài đặt môi trường ảo
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Cài đặt dependencies
pip install -r requirements.txt

# 4. Chạy ứng dụng
flask run
```

---

## 📂 Cấu Trúc Dự Án

```
PetVax/
├── server/
│   ├── app/              # Core application
│   │   ├── __init__.py
│   │   ├── routes/       # API endpoints
│   │   ├── models/       # Database models
│   │   └── utils/        # Helper functions
│   ├── config.py         # Configuration
│   └── requirements.txt
├── client/               # Frontend (sẽ thêm sau)
└── docs/                 # Tài liệu
```

I. Tổng quan dự án:

🐾 1. Bối cảnh

Ngày nay, với số lượng thú cưng (đặc biệt là chó và mèo) ngày càng tăng, việc đảm bảo sức khỏe và tiêm chủng cho chúng là điều vô cùng cần thiết. Tuy nhiên, nhiều chủ nuôi gặp khó khăn trong việc theo dõi lịch tiêm chủng, tình trạng sức khỏe và các dịch vụ chăm sóc liên quan. Điều này dẫn đến nguy cơ thú cưng khôngContext </summary>
```plantuml
@startuml
@context
title Biểu đồ ngữ cảnh hệ thống PVMS

entity "Khách Hàng" as KH
entity "Nhân Viên" as NV
entity "Quản Trị Viên" as QTV
entity "Bác Sĩ" as BS
entity "Cổng thanh toán" as Payment
entity "Thông báo" as Notify

system "Hệ thống PVMS" as PVMS

KH --> PVMS : Gửi yêu cầu / Đặt lịch
KH --> PVMS : Gửi yêu cầu hỗ trợ\nnhận lịch hẹn
PVMS --> KH : Thông báo hệ thống
PVMS --> KH : Thông báo lịch tiêm

NV --> PVMS : Hỗ trợ khách hàng
NV --> PVMS : Quản lý lịch hẹn
NV --> PVMS : Quản lý khách hàng

QTV --> PVMS : Quản lý website
QTV --> PVMS : Tạo báo cáo

PVMS --> Payment : Yêu cầu thanh toán
Payment --> PVMS : Xác nhận giao dịch

PVMS --> BS : Trả kết quả
PVMS --> BS : Nhận lịch tiêm

PVMS --> Notify : Gửi thông báo
@enduml
```
---
<details>
<summary> Code PlantUML USE </summary>
```plantuml
@startuml
title ERD - Hệ thống PVMS

entity NhanVien
entity TaiKhoan
entity KhachHang
entity BacSi
entity ThuCung
entity LichTiem
entity Vaccine
entity ThanhToan
entity HoSo

NhanVien -- TaiKhoan : quản lý
KhachHang -- ThuCung : sở hữu
ThuCung -- LichTiem : được lập
Vaccine -- LichTiem : được sử dụng
LichTiem -- ThanhToan : có
BacSi -- HoSo : ghi nhận
LichTiem -- HoSo : lưu trữ

@enduml
```
---
<details>
<summary> Code PlantUML USE </summary>

```plantuml
@startuml
left to right direction
actor "Người dùng" as User
actor "Bác Sĩ" as BS
actor "<<Hệ Thống>>\nThông báo" as Notify

rectangle "Hệ thống PVMS" {
    usecase "Đặt Lịch Tiêm" as UC1
    usecase "Xem lịch" as UC2
    usecase "Thanh toán" as UC3
    usecase "Thanh Toán Online" as UC4
    usecase "Gửi hóa đơn" as UC5
    usecase "Thực hiện Tiêm" as UC6
}

' Liên kết actor
User --> UC1
BS --> UC6
Notify --> UC5

' Include / Extend
UC1 .> UC2 : <<include>>
UC1 .> UC6 : <<include>>
UC1 .> UC3 : <<include>>
UC3 <|-- UC4 : generalization
UC4 .> UC5 : <<include>>
@enduml
```
---
<details>


