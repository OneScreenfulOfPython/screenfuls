Add a user via an HTML form on the /users page.

This required adding a general-purpose execute function for SQL,
an add_user_to_database function which creates a user from a name
and (optional) email address, and trapping the /add-user URL.
