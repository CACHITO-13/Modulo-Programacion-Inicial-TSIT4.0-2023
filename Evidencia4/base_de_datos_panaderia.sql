create database db_negocio_panaderia;
use db_negocio_panaderia;
create table PRODUCTOS (Id_producto int, Precio int, Proveedor varchar(40));
create table INSUMOS (Id_insumo int, Nombre_insumo varchar(45)); 
create table COMPRAS (Id_compra int, Proveedor varchar(40), Id_pedido int);
create table PEDIDOS (Id_pedido int, Id_empleado int, Id_producto int, Total int);
create table EMPLEADOS (Id_empleado int, DNI int, Nombre varchar(30), Salario int);
create table PRODUCCION_DIARIA (Id_produccion int, Fecha_produccion varchar(15),Id_producto int,Cantidad_Producida int);
create table RECETAS (Id_receta int, Id_producto int, Id_insumo int, Cantidad_usada int);
use db_negocio_panaderia;
insert INTO db_negocio_panaderia.PRODUCTOS(Id_producto,Precio ,Proveedor)
VALUES 
	(1,60,"Medialunas Don Juan"),
	(2,40,"Pastelitos S.A."),
    (3,55,"Facturas Chocolatosas S.R.L"),
    (4,20,"Chipas lo de carlitos"),
    (5,500,"Tortas sabrosas S.A.");

insert INTO db_negocio_panaderia.INSUMOS(Id_insumo,Nombre_insumo)
VALUES
	(1,"Harina"),
    (2,"Leche"),
    (3,"Huevos"),
    (4,"Azucar"),
    (5,"Levadura");
insert INTO db_negocio_panaderia.COMPRAS(Id_compra,Proveedor,Id_pedido)
VALUES
	(1,"Manfrey",1),
    (2,"Pureza",2),
    (3,"Gallinero Roberto",3),
    (4,"Don Pedro",4),
    (5,"Calsa",5);
insert INTO db_negocio_panaderia.PEDIDOS(Id_pedido, Id_empleado, Id_producto,Total) 
VALUES
	(1,1,4,1000),
    (2,4,3,550),
    (3,5,5,5000),
    (4,3,2,2000),
    (5,2,1,600);
insert INTO db_negocio_panaderia.EMPLEADOS(Id_empleado, DNI,Nombre, Salario) 
VALUES
	(1,35564329,"Irina",80000),
    (2,17524500,"Matheo",100000),
    (3,42086301,"Elias",120000),
    (4,15340588,"Ezequiel",65000),
    (5,21081308,"Marcos",70000);
insert INTO db_negocio_panaderia.PRODUCCION_DIARIA(Id_produccion,Fecha_produccion,Id_producto,Cantidad_Producida) 
VALUES
(1,"11/6/2023",1,20),
(2,"12/6/2023",2,2),
(3,"13/6/2023",3,50),
(4,"14/6/2023",4,5),
(5,"15/6/2023",5,4);
insert INTO db_negocio_panaderia.RECETAS (Id_receta,Id_producto,Id_insumo ,Cantidad_usada)
VALUES
	(1,1,1,3),
    (2,2,2,6),
    (3,3,3,50),
    (4,4,4,8),
    (5,5,5,42);
    
