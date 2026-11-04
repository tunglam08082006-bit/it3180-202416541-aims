# Lab 02 — Feature, topic và Pull Request

## Vì sao đồng bộ với master trước PR?

Nhánh được tạo từ commit cũ có thể thiếu thay đổi vừa được tích hợp. Fetch và
merge master vào nhánh giúp chạy thử đúng tổ hợp mã sắp được nộp, xử lý conflict
sớm và giảm khả năng một PR riêng lẻ đúng nhưng khi tích hợp lại sai.
Không nhất thiết rebase mọi PR; trong bài dùng merge để giữ lịch sử đã chia sẻ.

## Khi nào không được rebase?

Không rebase master, release hoặc nhánh mà người khác đang dựa vào. Rebase
tạo commit có SHA mới; người cộng tác vẫn giữ lịch sử cũ sẽ phải xử lý phân kỳ.
Đề giới hạn viết lại lịch sử ở commit chưa chia sẻ. Nhánh nháp chưa push có
thể rebase hoặc amend; commit chung cần sửa bằng commit mới/revert.

## Feature khác topic thế nào?

Đây là quy ước nhóm, không phải hai loại đối tượng khác nhau trong Git.
`feature/cart-print` thêm hành vi sản phẩm; `topic/pr-template` hoặc
`topic/use-case-diagram` phục vụ tài liệu/cấu hình. Mỗi nhánh có một mục đích.

## Ba cách merge

| Cách | Lịch sử | Hoàn tác |
|---|---|---|
| Merge commit | Giữ commit nhánh và một commit hai cha | Revert merge với `-m 1` |
| Squash | Một commit tổng hợp mới trên nhánh đích | Revert commit đó |
| Rebase and merge | Các commit tuyến tính với SHA được GitHub tạo lại | Có thể phải revert nhiều commit |

## Làm cá nhân

Bài thực hành dùng chế độ cá nhân với 0 approval. Khi kiểm tra PR in giỏ,
phát hiện thiếu thông báo giỏ rỗng và bổ sung commit sửa trên cùng nhánh.
Phần kiểm tra được thực hiện bởi tác giả, chưa có review độc lập.
