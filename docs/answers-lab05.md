# Lab 05 — Hotfix và bảo trì nhiều phiên bản

## Upstream first và release first

Upstream first sửa master trước rồi chuyển về dòng cũ: phiên bản tương lai
chắc chắn có fix, phù hợp khi master được giữ ổn định bằng CI. Đổi lại master
có thể khác nhiều bản đang chạy, nên backport cần điều chỉnh và kiểm thử.

Release first bắt đầu đúng baseline gặp lỗi: phạm vi nhỏ, có thể kiểm tra và
phát hành bản vá khẩn nhanh. Rủi ro là quên đưa fix về master hoặc dòng release
khác. Cần một checklist lan truyền và kiểm toán hành vi ở từng dòng.

## Nếu quên sửa release/lab05 thì lệnh nào phát hiện?

Vòng lặp kiểm tra hành vi trên `v1.0.1`, `v1.1.0`, `master` trong Phần F phát
hiện trực tiếp: dòng nào còn lỗi sẽ in 0 thay vì 1.

`git tag --contains FIX_SHA` chỉ xét quan hệ tổ tiên của đúng commit gốc.
Cherry-pick tạo SHA mới; vì vậy v1.1.0 không nhất thiết xuất hiện dù đã nhận fix.
Không được suy luận thiếu bản sửa chỉ từ việc tag không chứa SHA gốc.
`git cherry -v origin/release/lab05 origin/release/lab04` bổ sung kiểm tra
patch tương đương: dấu `-` cho fix nghĩa là đã có patch tương đương ở lab05.
Lệnh so với master trong ví dụ của đề chỉ kiểm tra master, không kiểm tra lab05.

## Vì sao tách commit sửa lỗi và tăng version?

Chỉ cherry-pick phần mã/test. Nếu chuyển cả commit 1.0.1 lên master đang 1.1.0,
version sẽ bị hạ hoặc xung đột. CHANGELOG cập nhật riêng theo dòng phát hành.

## Vì sao chưa tag v1.1.0 ngay lúc tạo release/lab05?

Nhánh còn cần nhận hotfix và kiểm thử. Tag chỉ được đặt khi baseline sẵn sàng.
Nếu v1.1.0 đã công bố thì phải phát hành v1.1.1, không di chuyển tag cũ.

## Truy vết

- Issue lỗi tìm kiếm: #19.
- FIX_SHA gốc: `959624edec1c4e8f17b0ab3940ba03c9fe3aaab8`.
- Cherry-pick về master: `7fddd7a888d9902360a105292d8405edcfd342a9`.
- Cherry-pick về lab05: `03e4f868c235cac2455371c08b292afd48f7b2a0`.
- Cả hai commit dùng `cherry-pick -x`, giữ dòng nguồn gốc trong message.
- Dòng 1.0.x chỉ sửa tìm kiếm, không nhận sort/category từ master.
