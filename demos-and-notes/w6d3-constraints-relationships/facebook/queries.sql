-- Examples of a join query using a join table
-- How we can very flexibly get data from our many-to-many relationships.


-- Get user ids of all users who joined a particular group, 
-- and also get the name of the group. 
SELECT user_accounts.id AS user_account_id, group.name,
FROM user_accounts                                                                                          
JOIN user_group ON user_accounts.id = user_group.user_id                                                    
JOIN groups ON groups.id = user_group.group_id                                                              
WHERE groups.id = 2;

-- Get group ids of all groups a particular user has joined,
-- and also get the name of each group and the user id.
SELECT groups.id AS group_id, group.name as group_name, user_accounts.id AS user_id,
FROM user_accounts                                                                                          
JOIN user_group ON user_accounts.id = user_group.user_id                                                    
JOIN groups ON groups.id = user_group.group_id                                                              
WHERE user_accounts.id = 1;