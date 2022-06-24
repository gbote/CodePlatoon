
--customers table
-- 1.
ALTER TABLE customers 
RENAME COLUMN first TO first_name;

ALTER TABLE customers 
RENAME COLUMN last TO last_name;

-- 2.
ALTER TABLE customers 
  ALTER COLUMN first_name TYPE varchar(255),
  ALTER COLUMN last_name TYPE varchar(255);

-- 3.
ALTER TABLE customers 
  ALTER COLUMN social TYPE varchar(9);

-- 4.
ALTER TABLE customers 
  ALTER COLUMN account_number TYPE varchar(14);

-- 5.
ALTER TABLE customers ADD line_2 varchar(255);

-- 6.
ALTER TABLE customers 
  ALTER COLUMN zip TYPE varchar(9);

-- 7.
ALTER TABLE customers 
DROP COLUMN current_balance_cents;


--statements table
-- 1.
ALTER TABLE statements 
ALTER COLUMN customer_id SET NOT NULL;

-- 2.
ALTER TABLE statements 
ALTER gallons_used TYPE numeric(10, 2);

-- 3.
ALTER table statements 
ALTER status SET DEFAULT 'payment due';

--final steps observation 
-- in customers, line 2 is the last column so address out of sequence; does not appear to be a way to change the order