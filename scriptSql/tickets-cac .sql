CREATE DATABASE IF NOT EXISTS myapp_python;
USE myapp_python;

CREATE TABLE IF NOT EXISTS `familias` (
  `id_familia` int AUTO_INCREMENT PRIMARY KEY,
  `familia` varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int AUTO_INCREMENT PRIMARY KEY,
  `id_familia` int,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  FOREIGN KEY (`id_familia`) REFERENCES `familias`(`id_familia`)
);

CREATE TABLE IF NOT EXISTS `artistas` (
  `id_artista` int AUTO_INCREMENT PRIMARY KEY,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `nacionalidad` varchar(255) NOT NULL,
  `genero` varchar(255) NOT NULL,
  `edad` int NOT NULL
);

CREATE TABLE IF NOT EXISTS `tickets` (
  `id_ticket` int AUTO_INCREMENT PRIMARY KEY,
  `id_usuario` int,
  `id_artista` int,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `cantidad` int NOT NULL,
  `categoria` varchar(255) NOT NULL,
  `files` LONGBLOB,
  FOREIGN KEY (`id_usuario`) REFERENCES `usuarios`(`id_usuario`),
  FOREIGN KEY (`id_artista`) REFERENCES `artistas`(`id_artista`)
);

/* ----------------------------------------------------------------------- */
USE myapp_python;

-- Insertar en la tabla familias
INSERT INTO familias (familia) VALUES ('admin');
INSERT INTO familias (familia) VALUES ('usuario');

-- Insertar en la tabla usuarios
INSERT INTO usuarios (id_familia, username, password, mail, nombre, apellido) VALUES 
(1, 'admin1', 'adminpass1', 'admin1@mail.com', 'AdminA', 'UnoA'),
(1, 'admin2', 'adminpass2', 'admin2@mail.com', 'AdminB', 'DosB'),
(2, 'usuario1', 'userpass1', 'usuario1@mail.com', 'Usuario1A', 'Uno'),
(2, 'usuario2', 'userpass2', 'usuario2@mail.com', 'Usuario2B', 'Dos');

-- Insertar en la tabla artistas
INSERT INTO artistas (nombre, apellido, nacionalidad, genero, edad) VALUES 
('Bruno', 'Mars', 'Estadounidense', 'Pop', 36),
('Dua', 'Lipa', 'Británica', 'Pop', 26),
('Michael', 'Jackson', 'Estadounidense', 'Pop', 50),
('Taylor', 'Swift', 'Estadounidense', 'Pop', 32),
('Billie', 'Eilish', 'Estadounidense', 'Indie Pop', 20),
('The', 'Weeknd', 'Canadiense', 'R&B', 32);

-- Insertar en la tabla tickets (dejar files NULL)
INSERT INTO tickets (id_usuario, id_artista, nombre, apellido, mail, cantidad, categoria, files) VALUES 
(3, 1, 'Usuario', 'Uno', 'usuario1@mail.com', 2, 'VIP', NULL),
(4, 2, 'Usuario', 'Dos', 'usuario2@mail.com', 3, 'General', NULL);

