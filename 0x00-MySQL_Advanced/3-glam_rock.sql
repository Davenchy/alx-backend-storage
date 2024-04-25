-- Get lifespans of bands with Glam rock style
SELECT band_name, (IFNULL(split, 2022) - formed) AS  lifespan
  FROM metal_bands
  WHERE style REGEXP 'Glam rock'
  ORDER BY lifespan DESC;
