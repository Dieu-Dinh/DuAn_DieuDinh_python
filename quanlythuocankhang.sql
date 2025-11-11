-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 04, 2025 lúc 02:49 AM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `quanlythuocankhang`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `danhmuc`
--

CREATE TABLE `danhmuc` (
  `id` int(11) NOT NULL,
  `ten_danhmuc` varchar(100) NOT NULL,
  `mo_ta` text DEFAULT NULL,
  `trang_thai` tinyint(4) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `danhmuc`
--

INSERT INTO `danhmuc` (`id`, `ten_danhmuc`, `mo_ta`, `trang_thai`, `created_at`) VALUES
(1, 'Hot Sale', NULL, 1, '2025-11-04 00:32:53'),
(2, 'Thuốc', NULL, 1, '2025-11-04 00:32:53'),
(3, 'My pham ', 'An toan va hieu qua ', 1, '2025-11-04 00:32:53'),
(4, 'Thiết bị, dụng cụ y tế', 'Bao gom tat ca cac thiet bi y te chuyen dung', 1, '2025-11-04 00:32:53'),
(5, 'Dược mỹ phẩm', NULL, 1, '2025-11-04 00:32:53'),
(6, 'Chăm sóc cá nhân', NULL, 1, '2025-11-04 00:32:53'),
(7, 'Chăm sóc trẻ em', 'Bao gom tat ca thuoc ve tre em', 1, '2025-11-04 00:32:53'),
(11, 'Hỗ trợ chức năng', 'Giúp hỗ trợ tăng cường sức khỏe', 1, '2025-11-04 01:44:45');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sanpham`
--

CREATE TABLE `sanpham` (
  `id` int(11) NOT NULL,
  `ten_sanpham` varchar(255) NOT NULL,
  `hinh_anh` varchar(255) DEFAULT NULL,
  `gia_goc` decimal(10,2) NOT NULL,
  `gia_ban` decimal(10,2) NOT NULL,
  `giam_gia` int(11) DEFAULT 0,
  `mo_ta` text DEFAULT NULL,
  `dung_tich_hoac_khoi_luong` varchar(50) DEFAULT NULL,
  `don_vi` varchar(50) DEFAULT NULL,
  `danhmuc_id` int(11) DEFAULT NULL,
  `trang_thai` tinyint(4) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `sanpham`
--

INSERT INTO `sanpham` (`id`, `ten_sanpham`, `hinh_anh`, `gia_goc`, `gia_ban`, `giam_gia`, `mo_ta`, `dung_tich_hoac_khoi_luong`, `don_vi`, `danhmuc_id`, `trang_thai`, `created_at`) VALUES
(1, 'Nước muối Vietrue sát khuẩn, súc miệng', 'vietrue.jpg', 7000.00, 4900.00, 30, NULL, '500ml', 'chai', 2, 1, '2025-11-04 00:32:55'),
(2, 'Thực phẩm dinh dưỡng Y Học Ensure Gold', 'ensure.jpg', 932000.00, 845000.00, 9, NULL, '800g', 'lon', 3, 1, '2025-11-04 00:32:55'),
(3, 'Sữa bột Anlene Gold hương Vani', 'anlene.jpg', 555000.00, 480000.00, 13, NULL, '800g', 'lon', 3, 1, '2025-11-04 00:32:55'),
(4, 'Costar Omega 3', 'omega3.jpg', 972000.00, 729000.00, 25, NULL, '365 viên', 'lọ', 3, 1, '2025-11-04 00:32:55'),
(5, 'Sắc Ngọc Khang', 'sacngockhang.jpg', 666000.00, 532800.00, 20, NULL, '180 viên', 'hộp', 2, 1, '2025-11-04 00:32:55');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`id`),
  ADD KEY `danhmuc_id` (`danhmuc_id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD CONSTRAINT `sanpham_ibfk_1` FOREIGN KEY (`danhmuc_id`) REFERENCES `danhmuc` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
