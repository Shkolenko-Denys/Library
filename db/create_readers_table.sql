USE librarydb;

CREATE TABLE readers
(
    id_reader INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    surname_author VARCHAR(30) NOT NULL,
    name_author VARCHAR(30) NOT NULL,
    patronymic_author VARCHAR(30),
    date_birth DATE,
    phone_num VARCHAR(15) NOT NULL,
    email VARCHAR(255),
    address_of_residence VARCHAR(1024),
    passport_num VARCHAR(9) NOT NULL,
    returned_books SMALLINT UNSIGNED NOT NULL,
    published_books SMALLINT UNSIGNED NOT NULL
);