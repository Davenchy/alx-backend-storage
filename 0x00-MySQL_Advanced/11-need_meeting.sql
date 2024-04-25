-- drop view if exists
DROP VIEW IF EXISTS need_meeting;
-- create view need_meeting for students that have less than 80 score and last_meeting is NULL or grater than one month
CREATE VIEW need_meeting AS
  SELECT name
  FROM students
  WHERE score < 80 AND (last_meeting IS NULL OR last_meeting < NOW() - INTERVAL 1 MONTH);
