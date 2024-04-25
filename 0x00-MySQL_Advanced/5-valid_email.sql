-- Create trigger to set user's email invalid on email update
CREATE TRIGGER update_email_trigger BEFORE UPDATE ON users FOR EACH ROW
BEGIN
IF NEW.email <> OLD.email THEN
  SET NEW.valid_email = 0;
END IF;
END
