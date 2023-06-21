use db_negocio_panaderia
CREATE TABLE if not exists compras(
  Id_compra INT PRIMARY KEY AUTO_INCREMENT,
  Proveedor VARCHAR(50) NOT NULL,
  Fecha_compra VARCHAR(15) NOT NULL,
  Monto_total DOUBLE NOT NULL,
  Id_insumo INT NOT NULL,
  FOREIGN KEY (Id_insumo) REFERENCES compras(Id_compra));
  
  CREATE TABLE if not exists insumos(
  Id_insumo INT primary KEY auto_increment,
  Nombre VARCHAR(50) NOT NULL,
  Unidad_Medida VARCHAR(30) NOT NULL,
  Cantidad INT NOT NULL);
  
  CREATE TABLE if not exists empleados(
  Id_empleado int primary key auto_increment,
  Nombre varchar(50) not null,
  Sueldo int not null,
  Puesto varchar(50) not null,
  DNI int not null,
  Telefono varchar(20) not null);
  
  CREATE TABLE if not exists pedidos(
  Id_pedido int primary key auto_increment,
  Monto_total double not null,
  Fecha varchar(15) not null,
  Cliente varchar(50) not null,
  Id_producto int not null,
  foreign key (Id_producto) references pedidos(Id_pedido));
  
  CREATE TABLE if not exists productos(
  Id_producto int primary key auto_increment,
  Nombre varchar(50) not null,
  Precio double not null);

CREATE TABLE if not exists produccion_diaria(
Id_produccion int primary key auto_increment,
Fecha_produccion varchar(15) not null,
Cantidad int not null,
Id_producto int not null,
foreign key (Id_producto) references produccion_diaria(Id_produccion));


CREATE TABLE if not exists recetas(
Id_receta int primary key auto_increment,
Id_producto int not null,
foreign key (Id_producto) references recetas(Id_receta),
Id_insumo int not null,
foreign key (Id_insumo) references recetas(Id_receta),
Cantidad_usada decimal (10,2) not null);

