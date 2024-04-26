-- drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
-- create the procedure
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  SET @total = (SELECT SUM(weight) FROM projects);
  UPDATE users as U, (
    SELECT U.id as id, SUM(C.score * P.weight) / @A as average_score
    FROM users as U
    JOIN corrections as C ON C.user_id = U.id
    JOIN projects as P ON P.id = C.project_id
    GROUP BY U.id
  ) as AW
  SET U.average_score = AW.average_score
  WHERE U.id = AW.id;
END
$$
DELIMITER ;
