create database db_negocio_panaderia;
use db_negocio_panaderia;
create table PRODUCTOS (Id_producto int, Precio int, Proveedor varchar(40));
create table INSUMOS (Id_insumo int, Nombre_insumo varchar(45)); 
create table COMPRAS (Id_compra int, Proveedor varchar(40), Id_pedido int);
create table PEDIDOS (Id_pedido int, Id_empleado int, Id_producto int, Total int);
create table EMPLEADOS (Id_empleado int, DNI int, Nombre varchar(30), Salario int);
create table PRODUCCION_DIARIA (Id_produccion int, Fecha_produccion varchar(15),Id_producto int,Cantidad_Producida int);
create table RECETAS (Id_receta int, Id_producto int, Id_insumo int, Cantidad_usada int);

