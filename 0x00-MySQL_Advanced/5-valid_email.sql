-- Create trigger to set user's email invalid on email update
-- drop trigger if exists
DROP TRIGGER IF EXISTS update_email_trigger;
-- create trigger
CREATE TRIGGER update_email_trigger BEFORE UPDATE ON users FOR EACH ROW
BEGIN
IF NEW.email <> OLD.email THEN
  SET NEW.valid_email = 0;
END IF;
END
