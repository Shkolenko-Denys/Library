CREATE DATABASE librarydb;

USE librarydb;

CREATE TABLE udc
(
    udc DECIMAL(3, 3) PRIMARY KEY,
    udc_description VARCHAR(50) NOT NULL
);

CREATE TABLE publishing_houses
(
    id_publishing_house INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    publishing_house VARCHAR(50) NOT NULL
);

CREATE TABLE genres
(
    id_genre TINYINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    genre VARCHAR(40) NOT NULL
);

CREATE TABLE authors
(
    id_author INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name_author VARCHAR(30) NOT NULL,
    surname_author VARCHAR(30) NOT NULL,
    patronymic_author VARCHAR(30)
);

CREATE TABLE groups_authors
(
    id_group_authors INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    group_authors SET('')
);

CREATE TABLE book_depository
(
	id_book INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(80) NOT NULL,
    id_group_authors INT UNSIGNED NOT NULL,
    id_publishing_house INT UNSIGNED,
    year_publication YEAR NOT NULL,
    id_genre TINYINT UNSIGNED,
    udc DECIMAL(3, 3),
    isbn BIGINT UNSIGNED,
    handed_out SMALLINT UNSIGNED NOT NULL,
    available SMALLINT UNSIGNED NOT NULL,
    
    FOREIGN KEY (id_group_authors) REFERENCES groups_authors (id_group_authors) ON DELETE CASCADE,
    FOREIGN KEY (id_publishing_house) REFERENCES publishing_houses (id_publishing_house) ON DELETE SET NULL,
    FOREIGN KEY (id_genre) REFERENCES genres (id_genre) ON DELETE SET NULL,
    FOREIGN KEY (udc) REFERENCES udc (udc) ON DELETE SET NULL
);