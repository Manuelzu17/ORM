CREATE TABLE productos (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  descripcion VARCHAR(255),
  precio DECIMAL(10, 2)
);
SELECT * FROM productos WHERE nombre LIKE '%search_term%';
