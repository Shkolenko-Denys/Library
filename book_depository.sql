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

CREATE TABLE id_of_book
(
	inventory_number INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    id_book INT UNSIGNED,
    place VARCHAR(30) NOT NULL,
    
    FOREIGN KEY (id_book) REFERENCES book_depository (id_book) ON DELETE SET NULL
);

CREATE TABLE books_out
(
	order_number INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    id_reader INT UNSIGNED,
    inventory_number INT UNSIGNED,
    status_if_returned BOOLEAN,
    date_out DATE,
    return_date DATE,

    FOREIGN KEY (inventory_number) REFERENCES id_of_book (inventory_number) ON DELETE SET NULL,
    FOREIGN KEY (id_reader) REFERENCES readers (id_reader) ON DELETE SET NULL
);

CREATE TABLE readers
(
    id_reader INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    surname_author VARCHAR(30) NOT NULL,
    name_author VARCHAR(30) NOT NULL,
    patronymic_author VARCHAR(30),
    date_birth DATE,
    phone_num VARCHAR(15) NOT NULL,
    email NVARCHAR(255),
    address_of_residence varchar(1024),
    passport_num VARCHAR(9) NOT NULL,
    returned_books SMALLINT UNSIGNED NOT NULL,
    published_books SMALLINT UNSIGNED NOT NULL
);