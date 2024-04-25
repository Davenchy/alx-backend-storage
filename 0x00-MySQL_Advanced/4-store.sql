-- Add a trigger to update stock on order

-- drop trigger if exists
DROP TRIGGER IF EXISTS update_stock_on_order;

-- create trigger
CREATE TRIGGER update_stock_on_order
  AFTER INSERT ON orders
  FOR EACH ROW
  BEGIN
    UPDATE items SET quantity = quantity - NEW.number
      WHERE name = NEW.item_name;
  END;
