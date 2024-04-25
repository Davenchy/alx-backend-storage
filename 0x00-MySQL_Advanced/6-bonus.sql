-- Delete bonus procedure if exists
DROP PROCEDURE IF EXISTS AddBonus;
-- Create AddBonus procedure
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
  DECLARE project VARCHAR(255);
  SET project = (SELECT id FROM projects WHERE name = project_name);
  IF project IS NOT NULL THEN
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project, score);
  END IF;
END
