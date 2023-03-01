CREATE TABLE comentarios (
  id INT PRIMARY KEY,
  texto VARCHAR(255),
  fecha_creacion DATE,
  producto VARCHAR(255),
);
SELECT * FROM comentarios WHERE producto = 'product';
