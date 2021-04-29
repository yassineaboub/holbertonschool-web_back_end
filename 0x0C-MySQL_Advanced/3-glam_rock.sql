-- SQL script that lists all bands with Glam rock as their main style
SELECT band_name, (if(split, split, 2020) - formed) as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan  DESC;
