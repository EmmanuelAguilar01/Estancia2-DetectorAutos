create database Deteccion;
drop database Deteccion;
use Deteccion;
CREATE TABLE `deteccion`.`usuario` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(30) NOT NULL,
  `Apellido` VARCHAR(25) NULL,
  `Contra` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`idUsuario`));
CREATE TABLE `deteccion`.`imagen` (
  `idImagen` INT NOT NULL AUTO_INCREMENT,
  `idUsuario` INT NOT NULL,
  `Fecha` DATE NULL,
  `Hora` DATETIME NULL,
  PRIMARY KEY (`idImagen`),
  CONSTRAINT `idUsuario`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `deteccion`.`usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
    ALTER TABLE `deteccion`.`imagen` 
CHANGE COLUMN `Hora` `Hora` TIME NULL DEFAULT NULL ;

CREATE TABLE `deteccion`.`resultado` (
  `idResultado` INT NOT NULL AUTO_INCREMENT,
  `idImagen` INT NOT NULL,
  `Resul` VARCHAR(15) NOT NULL,
  `Elemento` VARCHAR(15) NOT NULL,
  `Color` VARCHAR(15) NULL,
  PRIMARY KEY (`idResultado`),
  CONSTRAINT `idImagen`
    FOREIGN KEY (`idImagen`)
    REFERENCES `deteccion`.`imagen` (`idImagen`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
INSERT INTO `deteccion`.`usuario` (`Nombre`, `Apellido`, `Contra`) VALUES ('Abner', 'Moreno', 'Moreno456');
INSERT INTO `deteccion`.`usuario` (`Nombre`, `Apellido`, `Contra`) VALUES ('Maria', 'Lorenzo', 'Lorenzo789');
INSERT INTO `deteccion`.`usuario` (`Nombre`, `Apellido`, `Contra`) VALUES ('Sadra', 'Diaz', 'Dias159');
INSERT INTO `deteccion`.`usuario` (`Nombre`, `Apellido`, `Contra`) VALUES ('Joaquin', 'Lopez', 'Lopez753');

INSERT INTO `deteccion`.`imagen` (`idUsuario`, `Fecha`, `Hora`) VALUES ('1', '2022-10-24', '15:00:00');
INSERT INTO `deteccion`.`imagen` (`idUsuario`, `Fecha`, `Hora`) VALUES ('4', '2022-10-23', '12:00:35');
INSERT INTO `deteccion`.`imagen` (`idUsuario`, `Fecha`, `Hora`) VALUES ('2', '2022-10-15', '13:35:55');
INSERT INTO `deteccion`.`imagen` (`idUsuario`, `Fecha`, `Hora`) VALUES ('5', '2022-10-10', '14:00:02');
INSERT INTO `deteccion`.`imagen` (`idUsuario`, `Fecha`, `Hora`) VALUES ('1', '2022-10-20', '16:15:50');

INSERT INTO `deteccion`.`resultado` (`idImagen`, `Resul`, `Elemento`, `Color`) VALUES ('3', 'NO', 'Desconocido', 'No');
INSERT INTO `deteccion`.`resultado` (`idImagen`, `Resul`, `Elemento`, `Color`) VALUES ('6', 'SI', 'Automovil', 'Azul');
INSERT INTO `deteccion`.`resultado` (`idImagen`, `Resul`, `Elemento`, `Color`) VALUES ('5', 'SI', 'Automovil', 'Rojo');
INSERT INTO `deteccion`.`resultado` (`idImagen`, `Resul`, `Elemento`, `Color`) VALUES ('7', 'SI', 'Automovil', 'Amarillo');
