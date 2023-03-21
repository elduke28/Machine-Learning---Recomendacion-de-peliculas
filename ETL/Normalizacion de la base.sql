-- Tansformaciones de las tablas

-- Generar campo id con la primer letra del nombre de la plataforma seguido del show_id
ALTER TABLE amazon ADD id VARCHAR(10) AFTER show_id;
UPDATE amazon SET id = concat('a',show_id);
ALTER TABLE amazon DROP show_id;
ALTER TABLE amazon ADD COLUMN plataform VARCHAR(10) NULL AFTER id;
UPDATE amazon SET plataform = 'amazon';


ALTER TABLE disney ADD id VARCHAR(10) AFTER show_id;
UPDATE disney SET id = concat('d',show_id);
ALTER TABLE disney DROP show_id;
ALTER TABLE disney ADD COLUMN plataform VARCHAR(10) NULL AFTER id;
UPDATE disney SET plataform = 'disney';

ALTER TABLE hulu ADD id VARCHAR(10) AFTER show_id;
UPDATE hulu SET id = concat('h',show_id);
ALTER TABLE hulu DROP show_id;
ALTER TABLE hulu ADD COLUMN plataform VARCHAR(10) NULL AFTER id;
UPDATE hulu SET plataform = 'hulu';

ALTER TABLE netflix ADD id VARCHAR(10) AFTER show_id;
UPDATE netflix SET id = concat('n',show_id);
ALTER TABLE netflix DROP show_id;
ALTER TABLE netflix ADD COLUMN plataform VARCHAR(10) NULL AFTER id;
UPDATE netflix SET plataform = 'netflix';

-- Creamos la tabla plataforma, que es la union de todas las plataformas
DROP TABLE IF EXISTS plataforma;
CREATE TABLE IF NOT EXISTS plataforma
select * from amazon
union all
select * from disney
union all
select * from hulu
union all
select * from netflix;

-- Imputar Valores Faltantes
UPDATE plataforma SET rating = 'G' WHERE rating = '';

-- Realizamos algunas modificaciones de tipos de datos
UPDATE plataforma SET duration = rating WHERE rating like '%Season%' or rating like '%min%';

-- UPDATE plataforma SET rating = 'Sin_datos' WHERE rating LIKE "%season%" or rating LIKE "%min%";


-- Actualizamos de las fechas
UPDATE plataforma SET date_added = 'Sin_dato' WHERE date_added = '';
UPDATE plataforma SET date_added = date_format(str_to_date(date_added, '%M %d, %Y'), '%Y-%m-%d') WHERE date_added != 'Sin_dato';


-- Pasamos los campos texto a minuscula
UPDATE plataforma SET type = TRIM(LOWER(type));
UPDATE plataforma SET title = TRIM(LOWER(title));
UPDATE plataforma SET director = TRIM(LOWER(director));
UPDATE plataforma SET cast = TRIM(LOWER(cast));
UPDATE plataforma SET country = TRIM(LOWER(country));
UPDATE plataforma SET rating = TRIM(LOWER(rating));
UPDATE plataforma SET duration = TRIM(LOWER(duration));
UPDATE plataforma SET listed_in = TRIM(LOWER(listed_in));
UPDATE plataforma SET description = TRIM(LOWER(description));

-- Normalizacion del campo duration
ALTER TABLE plataforma ADD duration_int integer AFTER duration;
ALTER TABLE plataforma ADD duration_type varchar(10) AFTER duration_int;
UPDATE plataforma SET duration_int = REGEXP_SUBSTR(duration,"[0-9]+");
UPDATE plataforma SET duration_type = REGEXP_SUBSTR(duration,"[a-z]+");
UPDATE plataforma SET duration_type = 'season' WHERE duration_type = 'seasons';
-- ALTER TABLE plataforma DROP duration;

-- Valores faltantes 
UPDATE plataforma SET cast = 'Sin_dato' where cast = '';
UPDATE plataforma SET director = 'Sin_dato' where director = '';
