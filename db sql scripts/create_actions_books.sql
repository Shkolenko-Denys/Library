USE librarydb;

CREATE TABLE id_of_book
(
    inventory_number INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_book INT UNSIGNED,
    place VARCHAR(30) NOT NULL,
    
    FOREIGN KEY (id_book) REFERENCES book_depository (id_book) ON DELETE SET NULL
);

CREATE TABLE books_out
(
    order_number INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_reader INT UNSIGNED,
    inventory_number INT UNSIGNED,
    status_if_returned BOOLEAN,
    date_out DATE,
    return_date DATE,
    
    FOREIGN KEY (inventory_number) REFERENCES id_of_book (inventory_number) ON DELETE SET NULL,
    FOREIGN KEY (id_reader) REFERENCES readers (id_reader) ON DELETE SET NULL
);

CREATE TABLE replenishment
(
    id_replenishment INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_book INT UNSIGNED,
    quantity INT UNSIGNED,

    FOREIGN KEY (id_book) REFERENCES id_of_book (id_book) ON DELETE SET NULL
);

CREATE TABLE write_off
(
    id_write_off INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    inventory_number INT UNSIGNED,
    date_write_off DATE,

    FOREIGN KEY (inventory_number) REFERENCES id_of_book (inventory_number) ON DELETE SET NULL
);