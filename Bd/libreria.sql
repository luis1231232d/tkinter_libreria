-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-03-2021 a las 03:34:07
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 7.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `libreria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `Documento` int(12) NOT NULL,
  `Nombre` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `Apellido` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `Direccion` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `Ciudad` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `Codigo_Postal` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`Documento`, `Nombre`, `Apellido`, `Direccion`, `Ciudad`, `Codigo_Postal`) VALUES
(1005712070, 'Luis Miguel', 'Garcia Aranzalez', 'Smpz3 Mz6 Csa1 Las Americas', 'Ibague', 72);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `Id_libro` int(3) NOT NULL,
  `Titulo` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `Nom_Autor` varchar(35) COLLATE utf8_spanish_ci NOT NULL,
  `Categoria` varchar(35) COLLATE utf8_spanish_ci NOT NULL,
  `Precio` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`Id_libro`, `Titulo`, `Nom_Autor`, `Categoria`, `Precio`) VALUES
(1, 'Luces de bohemia', 'Ramón del Valle-Inclán', 'Teatro', 9000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ordenes`
--

CREATE TABLE `ordenes` (
  `Id_orden` int(11) NOT NULL,
  `Documento` int(12) NOT NULL,
  `Id_libro` int(3) NOT NULL,
  `Fecha_orden` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `ordenes`
--

INSERT INTO `ordenes` (`Id_orden`, `Documento`, `Id_libro`, `Fecha_orden`) VALUES
(3, 1005712070, 1, '2021-03-03 00:26:48');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`Documento`);

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`Id_libro`);

--
-- Indices de la tabla `ordenes`
--
ALTER TABLE `ordenes`
  ADD PRIMARY KEY (`Id_orden`),
  ADD KEY `Documento` (`Documento`),
  ADD KEY `Id_libro` (`Id_libro`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ordenes`
--
ALTER TABLE `ordenes`
  MODIFY `Id_orden` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ordenes`
--
ALTER TABLE `ordenes`
  ADD CONSTRAINT `ordenes_ibfk_3` FOREIGN KEY (`Documento`) REFERENCES `clientes` (`Documento`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ordenes_ibfk_4` FOREIGN KEY (`Id_libro`) REFERENCES `libros` (`Id_libro`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
