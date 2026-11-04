# Lab 03 — Bugfix, conflict và hoàn tác

## Merge base là gì?

Merge base là tổ tiên chung tốt nhất của hai commit: không có một tổ tiên
chung khác là hậu duệ của nó. Git dùng baseline này để thực hiện three-way
merge: so sánh từng phía với tổ tiên rồi kết hợp. Lịch sử criss-cross phức tạp
có thể có nhiều merge base, nên 'luôn đúng một commit gần nhất' là chưa đầy đủ.
Xem bằng `git merge-base <nhánh-A> <nhánh-B>`.

## Vì sao master và release cần revert?

Các nhánh này đã được chia sẻ và có baseline/tag phụ thuộc. Reset hoặc rebase
làm đổi lịch sử người khác đang sử dụng. Revert thêm commit đảo ngược nhưng
giữ dấu vết thay đổi và lý do hoàn tác. Revert merge dùng `-m 1` để chọn cha
thứ nhất (master trước merge) làm đường chính; phải kiểm tra các cha trước.

## Bằng chứng thực hành

- Issue giới hạn giỏ: #6.
- Commit test thất bại: `a508f4fe50c1e084710be4afb33957fc5bc03ddc` (đĩa 21 trả True).
- Commit sửa sau test: `f03e7869b7ad61fe481232e96a8d0f051daf8000` (đĩa 21 trả False).
- Bugfix discount mở PR vào `feature/discount` trước khi feature vào master.
- Hai nhánh sửa cùng dòng thông báo đã tạo conflict thật khi merge master.
  Commit giải quyết: `07a23eb840dfc84e1f80c4d72923d3443ac3b0a6`; kết hợp tiếng Việt và tên DVD.
- Merge bị hoàn tác: `0a75c3a82da2bb4c79a4e6ee27a023787ff74c1b`; commit revert: `b08ef37f6f3d4bc31a4578c768c614736df5a7d7`.
  Sau revert, thông báo chỉ còn tiếng Việt, vẫn giữ chức năng thêm DVD.
- Đã chạy reset soft/mixed/hard trên nhánh nháp chưa push, với tệp dùng riêng
  cho bài thử. `reflog`/`git show` truy lại commit `00879a8fb53f1e3087bedd4a158349bf8f287b2e`.
- Bộ 4 unittest thành công sau sửa lỗi, sau giải quyết conflict và sau revert.

Reset soft giữ thay đổi ở staging; mixed đưa về working tree; hard loại bỏ
thay đổi trong các tệp được theo dõi. Reflog là nhật ký local, có thời hạn lưu,
không phải bản sao lưu và không được push lên GitHub.
