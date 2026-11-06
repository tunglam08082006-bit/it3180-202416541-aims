# AIMS-mini — IT3180

[![CI](https://github.com/tunglam08082006-bit/it3180-202416541-aims/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/tunglam08082006-bit/it3180-202416541-aims/actions/workflows/ci.yml)

**Hoàng Tùng Lâm · MSSV 202416541**  
Thực hành quản lý cấu hình phần mềm bằng Git và GitHub, Lab 01–05.

AIMS-mini quản lý giỏ DVD trong bộ nhớ: thêm/xóa, in giỏ, tính tổng và giảm
giá, tìm theo tiêu đề/thể loại, sắp xếp theo tiêu đề/giá. 



```console
git clone https://github.com/tunglam08082006-bit/it3180-202416541-aims.git
cd it3180-202416541-aims
python main.py
python -m unittest discover -s tests -v
```
## Bản nộp theo từng lab

| Lab | Nhánh nộp | Tag | Trọng tâm |
|---|---|---|---|
| 01 | [release/lab01](https://github.com/tunglam08082006-bit/it3180-202416541-aims/tree/release/lab01) | [v0.1.0](https://github.com/tunglam08082006-bit/it3180-202416541-aims/tree/v0.1.0) | Thiết lập, restore/amend, refactor |
| 02 | [release/lab02](https://github.com/tunglam08082006-bit/it3180-202416541-aims/tree/release/lab02) | [v0.2.0](https://github.com/tunglam08082006-bit/it3180-202416541-aims/tree/v0.2.0) | Feature/topic, đồng bộ và 3 kiểu merge |
| 03 | [release/lab03](https://github.com/tunglam08082006-bit/it3180-202416541-aims/tree/release/lab03) | [v0.3.0](https://github.com/tunglam08082006-bit/it3180-202416541-aims/tree/v0.3.0) | Test trước fix, conflict, reset/revert |
| 04 | [release/lab04](https://github.com/tunglam08082006-bit/it3180-202416541-aims/tree/release/lab04) | [v1.0.0](https://github.com/tunglam08082006-bit/it3180-202416541-aims/releases/tag/v1.0.0) → [v1.0.1](https://github.com/tunglam08082006-bit/it3180-202416541-aims/releases/tag/v1.0.1) | Phát hành và bảo trì dòng 1.0.x |
| 05 | [release/lab05](https://github.com/tunglam08082006-bit/it3180-202416541-aims/tree/release/lab05) | [v1.1.0](https://github.com/tunglam08082006-bit/it3180-202416541-aims/releases/tag/v1.1.0) | Tính năng mới và lan truyền hotfix |

Các tag đều là **annotated tag**. `v1.0.0` giữ nguyên baseline gốc; đầu
`release/lab04` đã tiến lên `v1.0.1` qua PR hotfix. Các bản trước hotfix giữ
lỗi mẫu để thể hiện quá trình học; dùng master hoặc v1.1.0 để chạy mã đã sửa.

## Tài liệu và bằng chứng

- Câu trả lời: [Lab 01](docs/answers-lab01.md), [Lab 02](docs/answers-lab02.md),
  [Lab 03](docs/answers-lab03.md), [Lab 04](docs/answers-lab04.md),
  [Lab 05](docs/answers-lab05.md).
- [Bảng đối chiếu bài nộp và kiểm toán](docs/submission-checklist.md).
- [Cách chạy lại các bài thực hành](docs/reproduce.md).
- [Use case](docs/use-case.md), [CHANGELOG](CHANGELOG.md),
  [Pull Requests](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pulls?q=is%3Apr) và [Releases](https://github.com/tunglam08082006-bit/it3180-202416541-aims/releases).

## Quy trình thực hiện

Sau bootstrap Lab 01, mọi thay đổi vào master/release đi qua PR. Master yêu
cầu CI `test` thành công và nhánh cập nhật; release/* cấm force push và xóa.
Đã kiểm tra push thẳng bị chặn ở cả master và release/lab04.

Thực hiện theo chế độ cá nhân với **0 approval**, được đề cho phép. Chưa có
review độc lập `Changes requested → Approved` từ bạn học. Kết nối Git dùng
**HTTPS + Git Credential Manager**, chưa thực hiện bước SSH key/`ssh -T`.
Hai điểm khác với kịch bản cặp đôi/SSH được ghi rõ trong bảng đối chiếu.

Mã và câu trả lời được xây dựng riêng theo đề, có hỗ trợ Codex; kho tham khảo
chỉ dùng để hiểu cách trình bày, không sao chép mã nguồn. Sinh viên cần đọc,
chạy lại và hiểu lịch sử trước khi nộp link kho lên LMS.
