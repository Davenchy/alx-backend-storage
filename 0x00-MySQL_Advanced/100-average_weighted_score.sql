-- drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
-- create the procedure
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
  SET @total = (SELECT SUM(weight) FROM projects);
  SET @avg_score = (
    SELECT SUM(c.score * p.weight) / @total
    FROM corrections AS c
    JOIN projects as p ON p.id = c.project_id
    WHERE c.user_id = user_id
  );
  UPDATE users SET average_score = @avg_score WHERE id = user_id;
END
$$
DELIMITER ;
