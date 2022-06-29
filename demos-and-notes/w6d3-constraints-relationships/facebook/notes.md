# Facebook Database Schema

## Relationships

### One-to-One
    - user_account <-> user_profile
        - a user account can only be connected to one user profile and vice versa.

### One-to-Many
- user_accounts -> comments
    - user account has multiple comments
    - comment has just one user account
- posts -> comments
    - post has multiple comments
    - comment has just one post

### Many-to-Many
- user_accounts <-> groups
    - user account can be associated with multiple groups, a group can be associated with multiple users.
        - this is implemented with the user_group join table