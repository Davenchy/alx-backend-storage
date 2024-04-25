-- Create index for the first letter of the name using b-tree
CREATE INDEX idx_name_first USING BTREE ON names(name(1));
