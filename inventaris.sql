-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 28 Feb 2020 pada 06.01
-- Versi server: 10.1.38-MariaDB
-- Versi PHP: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inventaris`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_inventaris`
--

CREATE TABLE `data_inventaris` (
  `inventaris_no` varchar(20) NOT NULL,
  `inventaris_nama` varchar(30) NOT NULL,
  `inventaris_jenis` varchar(20) NOT NULL,
  `inventaris_tglmasuk` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `data_inventaris`
--

INSERT INTO `data_inventaris` (`inventaris_no`, `inventaris_nama`, `inventaris_jenis`, `inventaris_tglmasuk`) VALUES
('LBI.1.1', 'MEJA', 'LAMA', '12/12/2020'),
('LBI.1.2', 'KURSI', 'LAMA', '12/12/2020');

-- --------------------------------------------------------

--
-- Struktur dari tabel `habis_pakai`
--

CREATE TABLE `habis_pakai` (
  `habis_id` int(11) NOT NULL,
  `habis_nama` varchar(30) NOT NULL,
  `habis_tglmasuk` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `tetap`
--

CREATE TABLE `tetap` (
  `tetap_id` int(11) NOT NULL,
  `tetap_nama` varchar(30) NOT NULL,
  `tetap_tglmasuk` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `data_inventaris`
--
ALTER TABLE `data_inventaris`
  ADD PRIMARY KEY (`inventaris_no`);

--
-- Indeks untuk tabel `habis_pakai`
--
ALTER TABLE `habis_pakai`
  ADD PRIMARY KEY (`habis_id`);

--
-- Indeks untuk tabel `tetap`
--
ALTER TABLE `tetap`
  ADD PRIMARY KEY (`tetap_id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `habis_pakai`
--
ALTER TABLE `habis_pakai`
  MODIFY `habis_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `tetap`
--
ALTER TABLE `tetap`
  MODIFY `tetap_id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
