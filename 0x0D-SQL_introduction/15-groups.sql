-- list repeated score
SELECT score, COUNT(score) 'number' FROM second_table GROUP BY score;
