# Chạy lại và giải thích bài thực hành

## 1. Chạy bản cuối

```console
git clone https://github.com/tunglam08082006-bit/it3180-202416541-aims.git
cd it3180-202416541-aims
python main.py
python -m unittest discover -s tests -v
```

Kỳ vọng banner 1.1.0, tổng 63.89 USD và 9 test thành công.

## 2. Xem lịch sử

```console
git log --oneline --graph --all
git log --oneline --follow -- aims/cart.py
git show a508f4f
git show f03e786
git show 07a23eb
git show b08ef37
```

Lần lượt quan sát lịch sử rename, test bắt lỗi đĩa 21, bản sửa,
merge giải quyết conflict và commit revert.

## 3. So sánh bản trước/sau hotfix

```console
git worktree add ../aims-1.0.0 v1.0.0
git worktree add ../aims-1.0.1 v1.0.1
```

Trong từng thư mục, chạy:

```console
python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; print([d.title for d in search_by_title([D('The Lion King')], 'lion')])"
```

v1.0.0 trả `[]`; v1.0.1 trả `['The Lion King']`. Sau khi kiểm tra, quay lại
kho chính và dùng `git worktree remove ../aims-1.0.0` / `../aims-1.0.1`.

## 4. Kiểm tra cấu hình phát hành

```console
git tag -n
git diff --stat v1.0.0 v1.0.1
git log --all --oneline --grep="cherry picked from commit 959624edec1c4e8f17b0ab3940ba03c9fe3aaab8"
git tag --contains 959624edec1c4e8f17b0ab3940ba03c9fe3aaab8
git cherry -v origin/master origin/release/lab04
git cherry -v origin/release/lab05 origin/release/lab04
```

Tag chứa commit gốc chỉ là v1.0.1. Với cherry-pick, cần kiểm tra patch tương
đương hoặc hành vi; không yêu cầu v1.1.0 chứa đúng SHA gốc.

## 5. Câu hỏi phân tích

- Vì sao test giới hạn phải fail trước fix?
- Vì sao PR #8 có base feature/discount?
- Hai cha của merge commit mang ý nghĩa gì? `revert -m 1` giữ đường nào?
- Tại sao không chuyển commit tăng version 1.0.1 lên master 1.1.0?
- Vì sao tag không đổi nhưng nhánh release có thể tiến lên?
- CI phát hiện điều gì ở PR #24 và bảo vệ master bằng cách nào?
