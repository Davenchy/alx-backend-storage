-- Add a trigger to update stock on order
-- drop trigger if exists
DROP TRIGGER IF EXISTS update_stock_trigger;
-- create trigger
CREATE TRIGGER update_stock_trigger AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
