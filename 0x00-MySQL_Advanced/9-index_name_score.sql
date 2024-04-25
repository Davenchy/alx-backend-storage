-- Create index for the first letter of the name and the score using b-tree
CREATE INDEX idx_name_first_score USING BTREE ON names(name(1), score);
