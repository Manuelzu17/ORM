CREATE TABLE ordenes (
  id INT PRIMARY KEY,
  fecha_creacion DATE,
  fecha_envio DATE,
  estado VARCHAR(255),
  usuario VARCHAR(255),
);
SELECT * FROM ordenes WHERE usuario;
