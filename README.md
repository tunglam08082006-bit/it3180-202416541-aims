# AIMS-mini — IT3180

**Sinh viên:** Hoàng Tùng Lâm  
**MSSV:** 202416541

Ứng dụng dòng lệnh quản lý giỏ DVD, dùng để thực hành quản lý cấu hình
phần mềm với Git và GitHub qua 5 lab.

```console
python main.py
```

Kết quả kiểm tra nhanh: `Total cost: 63.89 $`.

Bài được triển khai độc lập theo đề IT3180. Các lỗi mẫu ban đầu được giữ
để thực hành test tái hiện, sửa lỗi và phát hành bản vá ở đúng lab.

Yêu cầu: Python 3.10 trở lên; chỉ sử dụng thư viện chuẩn.

## Chạy và kiểm thử

```console
python main.py
python -m unittest discover -s tests -v
```

## Các bản nộp

| Lab | Nhánh | Mốc ban đầu / bản vá | Nội dung |
|---|---|---|---|
| 01 | `release/lab01` | `v0.1.0` | Thiết lập và refactor |
| 02 | `release/lab02` | `v0.2.0` | Feature/topic, ba cách merge |
| 03 | `release/lab03` | `v0.3.0` | Bugfix, conflict, revert |
| 04 | `release/lab04` | `v1.0.0` / `v1.0.1` | Phát hành và dòng bảo trì 1.0.x |
| 05 | `release/lab05` | `v1.1.0` | Tính năng mới và lan truyền hotfix |

Tag mới chỉ xuất hiện sau khi hoàn thành bước phát hành tương ứng.
Các bản cũ giữ lỗi mẫu theo tiến trình học; dùng v1.1.0 hoặc master cho mã đã sửa.

## Tài liệu

- [Lab 01](docs/answers-lab01.md), [Lab 02](docs/answers-lab02.md),
  [Lab 03](docs/answers-lab03.md), [Lab 04](docs/answers-lab04.md).
- Câu trả lời Lab 05 được thêm khi hoàn tất hotfix trong `docs/answers-lab05.md`.
- [Use case](docs/use-case.md) và [CHANGELOG](CHANGELOG.md).

## Quy trình

Mọi thay đổi sau bootstrap đi qua PR. Master yêu cầu CI `test` thành công,
release/* yêu cầu PR và cấm force push/xóa. Làm cá nhân với 0 approval theo đề;
không có review độc lập bằng tài khoản bạn học. Dùng HTTPS/Git Credential
Manager thay cho SSH trong hướng dẫn.

Kho tham khảo chỉ được đọc để hiểu cách tổ chức; mã nguồn, test và phần giải
thích được xây dựng riêng. Có hỗ trợ của Codex trong quá trình thực hiện;
sinh viên cần đọc, chạy lại và hiểu lịch sử trước khi nộp.
