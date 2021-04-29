-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	SET @weighted_average = (
		SELECT SUM(score * weight) / SUM(weight)
		FROM corrections
		JOIN projects
		ON corrections.project_id = projects.id
		WHERE corrections.user_id = user_id);

	UPDATE users
	SET average_score = @weighted_average
	WHERE id = user_id;

END$$

DELIMITER ;

