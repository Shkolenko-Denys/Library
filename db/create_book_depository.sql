CREATE DATABASE librarydb;

USE librarydb;

CREATE TABLE udc
(
    udc DECIMAL(6, 3) PRIMARY KEY,
    udc_description VARCHAR(50) NOT NULL
);

CREATE TABLE publishing_houses
(
    id_publishing_house INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    publishing_house VARCHAR(50) NOT NULL
);

CREATE TABLE genres
(
    id_genre TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    genre VARCHAR(40) NOT NULL
);

CREATE TABLE authors
(
    id_authors INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    surnames_initials VARCHAR(50) NOT NULL
);

CREATE TABLE book_depository
(
    id_book INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(80) NOT NULL,
    id_authors INT UNSIGNED NOT NULL,
    id_publishing_house INT UNSIGNED,
    year_publication YEAR NOT NULL,
    id_genre TINYINT UNSIGNED,
    udc DECIMAL(6, 3),
    isbn BIGINT UNSIGNED,
    handed_out SMALLINT UNSIGNED NOT NULL,
    available SMALLINT UNSIGNED NOT NULL,
    
    FOREIGN KEY (id_authors) REFERENCES authors (id_authors) ON DELETE CASCADE,
    FOREIGN KEY (id_publishing_house) REFERENCES publishing_houses (id_publishing_house) ON DELETE SET NULL,
    FOREIGN KEY (id_genre) REFERENCES genres (id_genre) ON DELETE SET NULL,
    FOREIGN KEY (udc) REFERENCES udc (udc) ON DELETE SET NULL
);