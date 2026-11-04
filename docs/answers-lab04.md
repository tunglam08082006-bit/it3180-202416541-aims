# Lab 04 — Release flow và phiên bản

## Vì sao không merge release vào master?

Theo quy ước của học phần, release là dòng bảo trì một baseline đã nộp.
Merge toàn bộ có thể đưa cả metadata hoặc version dành riêng cho dòng cũ
vào master. Chỉ chuyển phần sửa lỗi cần thiết bằng cherry-pick có nguồn gốc.
Đây là chính sách của flow đang học, không phải giới hạn kỹ thuật của Git;
các quy trình khác có thể cho phép merge-back với quy tắc khác.

## So với GitFlow

Release Flow ở bài dùng master cho tích hợp liên tục, rẽ release/labXX làm
bản nộp, nhánh feature/bugfix/refactor sống ngắn. GitFlow truyền thống có thêm
develop cho tích hợp, main/master đại diện các bản production, với nhánh
release và hotfix được đưa về những nhánh dài hạn phù hợp. GitFlow có nhiều
bước phối hợp hơn, hữu ích khi nhịp phát hành và môi trường cần tách biệt.

## Vì sao 1.0.0 thay vì 0.4.0?

1.0.0 là quyết định công bố hợp đồng sử dụng ổn định đầu tiên cho phạm vi
đã chọn; không phải cứ hoàn thành Lab 04 là SemVer bắt buộc dùng 1.0.0.
Nếu hợp đồng còn thay đổi mạnh, 0.4.0 vẫn phù hợp. Trong bài, 1.0.0 đóng mốc
phát hành để các lab sau thực hành minor 1.1.0 và patch 1.0.1.

## Vì sao chuẩn bị release trên master?

Version, tài liệu và test được tích hợp qua PR trước; nhánh release chỉ rẽ
từ trạng thái đã kiểm tra. Tránh có bản sửa chuẩn bị chỉ tồn tại trên release
và bị bỏ quên ở dòng phát triển.

## Tag và nhánh release

Annotated tag chứa người tạo, thời gian và lời nhắn, định danh baseline cố
định. release/lab04 có thể tiến lên bởi PR hotfix. Vì thế sau Lab 05, tag
v1.0.0 vẫn ở commit cũ còn đầu release/lab04 chuyển sang v1.0.1.

## Ghi nhận và tái tạo

`git log A..B` liệt kê commit chỉ có ở B; `git diff A B` so snapshot.
`git describe --tags` cho tag tổ tiên gần nhất kèm khoảng cách commit.
Dùng detached HEAD/worktree để chạy lại bản cũ và `git archive` đóng gói.
CI được đưa vào từ trước khi rẽ release/lab04 để các PR hotfix cũng được test;
đây là phần mở rộng Lab 05 áp dụng sớm.
