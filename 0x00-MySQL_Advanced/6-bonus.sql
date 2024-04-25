-- Delete bonus procedure if exists
DROP PROCEDURE IF EXISTS AddBonus;
-- Create AddBonus procedure
CREATE PROCEDURE AddBonus (
  IN user_id INT,
  IN project_name VARCHAR(255),
  IN score FLOAT)
BEGIN
  -- insert project if not exists
  IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0 THEN
    INSERT INTO projects (name) VALUES (project_name);
  END IF;

  -- get project id
  SET @project_id = (SELECT id FROM projects WHERE name = project_name);
  -- insert new correction
  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @project_id, score);
END
