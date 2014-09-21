CREATE TABLE
    users
(
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(200) NOT NULL,
    email_address VARCHAR(200) NULL
)
;

CREATE TABLE
    rooms
(
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(200) NOT NULL,
    location VARCHAR(1024) NULL
)
;

CREATE TABLE
    bookings
(
    user_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    booked_on DATE NOT NULL,
    booked_from TIME NULL,
    booked_to TIME NULL
)
;