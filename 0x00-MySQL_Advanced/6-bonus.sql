-- Delete bonus procedure if exists
DROP PROCEDURE IF EXISTS AddBonus;
-- Create AddBonus procedure
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
  -- get project id using its name
  DECLARE project INT;
  SET project = (SELECT id FROM projects WHERE name = project_name);
  -- check if project is not exist
  IF project IS NULL THEN
    -- insert new project with given name
    INSERT INTO projects (name) VALUES (project_name);
    -- get new project id
    SET project = LAST_INSERT_ID();
  END IF;

  -- insert new correction
  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project, score);
END
