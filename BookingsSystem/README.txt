Build a booking system (ostensibly for Rooms but could be for anything: gym equipment, library books etc.).

Meta-Requirement:

* Only use built-in modules but suggest alternatives

Requirements:

* People have names & email addresses

* Rooms have names and locations

* Bookings are made by one person for one room between Time A and Time B

* There should be a usable interface to book rooms / view room bookings

Steps -- each intended to be a screenful

1) Create the empty database

2) Populate with some sample data: users, rooms, bookings

3) Create simple functions for accessing users & rooms

4) Create simple functions for accessing bookings via users & rooms

5) Refactor the database queries to use common functionality

6) Create a simple website with just a front page

7) Add /users to list users & /rooms to list rooms

8) Refactor the HTML pages to use common functionality

9) Add /bookings to list bookings for a user or a room

10) Add a user

11) Add a room

12) Add a booking (of a room by a user)

13) Add a booking (by a user of a room)

Hints:

* You can use the sqlite ".dump" command to quickly see the database contents:

  sqlite bookings.db .dump

