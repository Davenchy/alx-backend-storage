-- count and order band origins by fans number
SELECT origin, SUM(fans) nb_fans
  FROM metal_bands
  GROUP BY origin
  ORDER BY nb_fans DESC;
