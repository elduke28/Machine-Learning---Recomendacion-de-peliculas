show variables like "secure_file_priv";  
show variables like "local_infile";
set global local_infile = 1;
SET @@global.sql_mode= '';

-- Creamos la tabla de la plataforma amazon e ingestamos los datos
DROP TABLE IF EXISTS `amazon`;
CREATE TABLE IF NOT EXISTS `amazon` (
  `show_id` varchar(10),
  `type` varchar(10),
  `title` varchar(200),
  `director` text,
  `cast` text,
  `country` varchar(200),
  `date_added` text,
  `release_year` int DEFAULT NULL,
  `rating` varchar(10),
  `duration` varchar(20),
  `listed_in` varchar(100),
  `description` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\MLOpsReviews\\amazon_prime_titles.csv"
INTO TABLE `amazon` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

-- Creamos la tabla de la plataforma disney e ingestamos los datos
DROP TABLE IF EXISTS `disney`;
CREATE TABLE IF NOT EXISTS `disney` (
  `show_id` varchar(10),
  `type` varchar(10),
  `title` varchar(100),
  `director` varchar(100),
  `cast` varchar(200),
  `country` varchar(200),
  `date_added` text,
  `release_year` int DEFAULT NULL,
  `rating` varchar(10),
  `duration` varchar(20),
  `listed_in` varchar(100),
  `description` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\MLOpsReviews\\disney_plus_titles.csv"
INTO TABLE `disney` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

-- Creamos la tabla de la plataforma hulu e ingestamos los datos
DROP TABLE IF EXISTS `hulu`;
CREATE TABLE IF NOT EXISTS `hulu` (
  `show_id` varchar(10),
  `type` varchar(10),
  `title` varchar(100),
  `director` text,
  `cast` varchar(200),
  `country` varchar(200),
  `date_added` text,
  `release_year` int DEFAULT NULL,
  `rating` varchar(10),
  `duration` varchar(20),
  `listed_in` varchar(100),
  `description` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\MLOpsReviews\\hulu_titles.csv"
INTO TABLE `hulu` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

-- Creamos la tabla de la plataforma netflix e ingestamos los datos
DROP TABLE IF EXISTS `netflix`;
CREATE TABLE IF NOT EXISTS `netflix` (
  `show_id` varchar(10),
  `type` varchar(10),
  `title` varchar(150),
  `director` varchar(250),
  `cast` text,
  `country` varchar(200),
  `date_added` text,
  `release_year` int DEFAULT NULL,
  `rating` varchar(10),
  `duration` varchar(20),
  `listed_in` varchar(100),
  `description` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\MLOpsReviews\\netflix_titles.csv"
INTO TABLE `netflix` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

-- Creamos la tabla de los rating de los usuarios e ingestamos los datos
DROP TABLE IF EXISTS `score_movies`;
CREATE TABLE IF NOT EXISTS `score_movies` (
  `userid` int,
  `rating` decimal(1,1),
  `timestamp` int,
  `movieid` varchar(10)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\MLOpsReviews\\ratings\\1.csv"
INTO TABLE `rating` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\MLOpsReviews\\ratings\\2.csv"
INTO TABLE `rating` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\MLOpsReviews\\ratings\\3.csv"
INTO TABLE `rating` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\MLOpsReviews\\ratings\\4.csv"
INTO TABLE `rating` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\MLOpsReviews\\ratings\\5.csv"
INTO TABLE `rating` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\MLOpsReviews\\ratings\\6.csv"
INTO TABLE `rating` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\MLOpsReviews\\ratings\\7.csv"
INTO TABLE `rating` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\MLOpsReviews\\ratings\\8.csv"
INTO TABLE `rating` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\r\n' IGNORE 1 LINES;

-- Creamos una nueva tabla, con los promedio de los score y los movieid
CREATE TABLE score_prom_movies AS
SELECT movieid, AVG(score)*100 AS score
FROM score_movies
GROUP BY movieid;