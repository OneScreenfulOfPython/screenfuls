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

5) Create a simple website with just a front page

6) Add /users to list users

7) Add /rooms to list rooms

8) Add /bookings to list bookings

Hints:

* You can use the sqlite ".dump" command to quickly see the database contents:

  sqlite bookings.db .dump

