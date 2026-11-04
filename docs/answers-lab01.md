# Lab 01 — Thiết lập và refactor

## Vì sao dùng `git mv`?

`git mv dvd.py aims/dvd.py` thực hiện di chuyển và đưa thay đổi vào staging
trong một bước, giảm khả năng quên thêm đường dẫn mới hoặc xóa đường dẫn cũ.
Git lưu snapshot, không lưu một thao tác đổi tên riêng. Khi so sánh hai
snapshot, Git suy luận rename từ mức tương đồng; di chuyển thủ công rồi
`git add -A` cũng có thể được nhận diện như vậy.
`git log --follow -- aims/cart.py` giúp lần ngược lịch sử qua lần di chuyển.

## `release/lab01` có phải baseline không?

Có, khi nhóm chấp nhận commit đầu nhánh đó là bản nộp Lab 01. Tuy nhiên nhánh
có thể tiến lên khi hotfix; một annotated tag `v0.1.0` giữ định danh chính xác
cho baseline ban đầu. Cần lưu SHA và kiểm soát thay đổi thay vì chỉ dựa vào tên.

## Vì sao vẫn dùng PR khi làm một mình?

PR tạo điểm kiểm tra diff, mục đích và kết quả thử nghiệm trước khi tích hợp;
đồng thời lưu dấu vết yêu cầu → thay đổi → baseline. Cấu hình làm cá nhân dùng
0 approval theo đề, nhưng vẫn yêu cầu PR. Không coi tự kiểm tra là review độc lập.
Các commit khởi tạo trước PR đầu tiên là bước bootstrap theo Lab 01.

## Cấu hình global và local khác nhau thế nào?

`--global` thường nằm trong `~/.gitconfig` và áp dụng cho mọi kho của tài khoản
máy tính. `--local` ở `.git/config` chỉ tác động kho hiện tại và được ưu tiên
hơn giá trị global tương ứng. Bài này đặt danh tính ở local để không làm đổi
cấu hình của dự án khác; dùng email noreply của tài khoản GitHub.

## Kiểm tra

- Chạy `python main.py`: tổng 63.89 USD trước và sau refactor.
- Thực hành `restore`, `restore --staged`, `commit --amend` trên thay đổi chưa push.
- `.gitignore` loại `__pycache__/`; `.gitattributes` thống nhất xuống dòng LF.
- Kết nối Git dùng HTTPS và Git Credential Manager đã xác thực, thay cho SSH
  trong ví dụ của đề. Chưa thực hiện bài kiểm tra `ssh -T`.
