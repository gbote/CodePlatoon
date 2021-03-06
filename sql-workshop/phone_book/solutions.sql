-- 1.1 Find phone number for Lauri Abshire.
select phone from contacts where name='Lauri Abshire';

-- 1.2 Find who has the phone number 363-350-4983.
select name from contacts where phone='363-350-4983';

-- 2.1 Find phone number for the last name of Hermann.
select name, phone
from contacts
where name like '%Hermann';

-- 3.1 Change John Smith's phone number to 212-987-2342
update contacts
set phone='212-987-2342'
where name='John Smith';
