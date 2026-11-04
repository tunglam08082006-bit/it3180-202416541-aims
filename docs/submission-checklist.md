# Đối chiếu bài nộp — 05/11/2026

## Luồng và minh chứng trên GitHub

| Phần | Đã thực hiện | Minh chứng |
|---|---|---|
| Lab 01 | git mv, sửa import, restore/staged/amend, bỏ qua cache, baseline | [PR #1](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pull/1), release/lab01 |
| Lab 02 | PR template, 2 clone, tính năng song song, đồng bộ master | [PR #2–5](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pulls?q=is%3Apr+is%3Amerged) |
| Ba kiểu merge | Merge commit (#3), squash (#4), rebase (#5) | Lịch sử master và từng PR |
| Lab 03 | Issue → test fail → fix pass → PR → Issue đóng | [Issue #6](https://github.com/tunglam08082006-bit/it3180-202416541-aims/issues/6), [PR #7](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pull/7) |
| Bugfix từ feature | PR có base feature/discount rồi mới vào master | [PR #8](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pull/8), [PR #9](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pull/9) |
| Conflict | Hai nhánh cùng dòng, merge phát sinh conflict, kết hợp ý định | [PR #10](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pull/10), [PR #11](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pull/11) |
| Hoàn tác | Revert merge qua PR; reset/reflog trên nhánh nháp local | [PR #12](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pull/12), [câu trả lời Lab 03](answers-lab03.md) |
| Lab 04 | Version, CHANGELOG, annotated tag, GitHub Release, worktree/archive | [PR #15](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pull/15), [v1.0.0](https://github.com/tunglam08082006-bit/it3180-202416541-aims/releases/tag/v1.0.0) |
| Phát triển tiếp | Sort chỉ ở master/1.1.x, không ở dòng 1.0.x | [PR #16](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pull/16), [PR #17](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pull/17) |
| Lab 05 | Hotfix từ release/lab04, tách mã và version, phát hành patch | [Issue #19](https://github.com/tunglam08082006-bit/it3180-202416541-aims/issues/19), [PR #20](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pull/20) |
| Lan truyền | 2 cherry-pick -x, kiểm tra patch tương đương và hành vi | [PR #21](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pull/21), [PR #23](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pull/23) |
| CI | Test mọi PR vào master/release, yêu cầu test trên master | [Workflow](../.github/workflows/ci.yml) |
| CI chặn lỗi | Cố ý sai tổng, test fail, mergeable_state=blocked; đóng không merge | [PR #24](https://github.com/tunglam08082006-bit/it3180-202416541-aims/pull/24), [run thất bại](https://github.com/tunglam08082006-bit/it3180-202416541-aims/actions/runs/41874208716) |

## Kiểm toán đã chạy

Đã checkout và chạy demo trên từng tag cùng master. Các baseline có bộ test
đều chạy thành công: v0.3.0 có 4 test; v1.0.0 có 5; v1.0.1 có 6;
v1.1.0 và master có 9. Lab 01–02 chưa có unittest theo tiến trình của đề.

| Ref tại lần kiểm toán | Commit | Demo |
|---|---|---|
| `v0.1.0` | `9cb265392c3f` | 63.89 USD |
| `v0.2.0` | `a9a5156ae8e3` | 63.89 USD |
| `v0.3.0` | `10966622a5ff` | 63.89 USD |
| `v1.0.0` | `2a888d1d9e87` | 63.89 USD |
| `v1.0.1` | `67fd206bd993` | 63.89 USD |
| `v1.1.0` | `885ffe2ba642` | 63.89 USD |
| `master` | `babf38bbc58e` | 63.89 USD |

SHA master trong bảng là thời điểm kiểm toán mã; PR tài liệu sau đó không
thay đổi mã nguồn hoặc test. Không di chuyển các tag đã công bố.

- `git cat-file -t <tag>` trả `tag` cho cả 6 tag.
- v1.0.1 trùng đầu release/lab04; v1.1.0 trùng đầu release/lab05.
- `git diff --name-only v1.0.0 v1.0.1`: đúng 4 tệp.
- Tìm `lion` trên v1.0.1, v1.1.0, master đều cho 1 kết quả.
- `git cherry` xác nhận patch của FIX_SHA đã có trên cả master và lab05.
- Đúng 2 commit có dòng `(cherry picked from commit ...)` trỏ FIX_SHA.
- Không có __pycache__, .pyc hoặc log trong cây Git của các baseline.
- Push thử vào master bị GH006; push thử release/lab04 bị GH013.
  Hai commit thăm dò chỉ chứa tệp nháp và không được đưa vào các nhánh nộp.

## Phạm vi và phần cần sinh viên lưu ý

1. Dùng chế độ cá nhân, 0 approval theo trang 13/29 của đề. Chưa có review
   độc lập của bạn học; không giả mạo reviewer. Nếu lớp yêu cầu làm cặp đôi,
   cần một bạn học thật thực hiện phần review.
2. Git đã xác thực và push bằng HTTPS/Git Credential Manager. Chưa cấu hình
   SSH key hay chạy `ssh -T`; đây là khác biệt với bước SSH ở Lab 01.
3. Phần CI của Lab 05 được áp dụng trước lúc tạo release/lab04 để hotfix
   cũng có workflow. Không bỏ qua CI để merge lỗi; PR cố ý lỗi đã đóng.
4. Thư mục dữ liệu ban đầu chỉ có Android Affirmations, nên AIMS-mini được
   xây dựng mới theo đặc tả Python của PDF. Không lấy mã từ kho tham khảo.
5. Đã đưa bài lên GitHub. Việc dán link lên LMS vẫn do sinh viên thực hiện.
