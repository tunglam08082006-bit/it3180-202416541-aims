# Changelog

Các thay đổi đáng chú ý được nhóm theo Added/Changed/Fixed; phiên bản dùng
Semantic Versioning. Tag đã công bố không được di chuyển.

## [Unreleased]

## [1.1.0] - 2026-11-04

### Added
- Tìm DVD theo thể loại, không phân biệt hoa thường.
- Sắp xếp giỏ theo tiêu đề hoặc giá, kèm unittest.

## [1.0.0] - 2026-11-04

### Added
- Mô hình DVD và Cart; demo tổng 63.89 USD.
- In giỏ hàng, thông báo giỏ rỗng và tìm theo tiêu đề.
- Tính tổng sau giảm giá, kiểm tra tỷ lệ trong khoảng 0–100.
- Bộ unittest và CI cho PR vào master/release.

### Changed
- Đưa mã vào package aims và dùng thông báo thêm DVD bằng tiếng Việt.

### Fixed
- Từ chối DVD thứ 21, giữ đúng giới hạn 20 (#6).
- Công thức giảm giá trả số tiền cần trả thay vì tiền được giảm.

## [0.3.0] - 2026-11-04
### Added
- Bugfix flow, kiểm thử hồi quy, conflict và revert qua PR.

## [0.2.0] - 2026-11-04
### Added
- In giỏ, tìm kiếm tiêu đề, use case và mẫu Pull Request.

## [0.1.0] - 2026-11-04
### Added
- DVD, Cart và demo; tổ chức package qua refactor flow.
