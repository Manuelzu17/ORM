CREATE TABLE categorias (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  producto_id INT,
  FOREIGN KEY (producto_id) REFERENCES productos(id));

SELECT productos.* FROM productos
JOIN categorias ON categorias.producto_id = productos.id
WHERE productos.nombre LIKE '%search_term%';
