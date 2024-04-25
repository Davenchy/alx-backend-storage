-- drop presedure if exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
-- create procedure
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id int)
BEGIN
  SET @avg_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id);
  UPDATE users SET average_score = @avg_score WHERE id = user_id;
END;
$$
DELIMITER ;
