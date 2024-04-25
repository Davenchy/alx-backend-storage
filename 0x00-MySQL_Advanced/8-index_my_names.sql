-- Drop index if it exists
DROP INDEX idx_name_first IF EXISTS ON names;
-- Create index for the first letter of the name using b-tree
CREATE INDEX idx_name_first USING BTREE ON names(name(1));
