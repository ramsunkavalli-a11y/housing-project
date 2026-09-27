-- division; inspected 2026-09-27
SELECT id,names,subtype,sources,bbox,hex(ST_AsWKB(geometry)) as geometry_hex FROM read_parquet('s3://overturemaps-us-west-2/release/2026-09-23.1/theme=divisions/type=division/*',hive_partitioning=true)
    WHERE country='US' AND subtype IN ('neighborhood','macrohood','microhood') AND (
       (bbox.xmin BETWEEN -118.6 AND -118.0 AND bbox.ymin BETWEEN 34.0 AND 34.3 AND (names.primary ILIKE '%Los Feliz%' OR names.primary ILIKE '%Sherman Oaks%' OR names.primary ILIKE '%Bungalow%'))
       OR (bbox.xmin BETWEEN -87.8 AND -87.5 AND bbox.ymin BETWEEN 41.8 AND 42.1 AND names.primary ILIKE '%Lincoln Square%')
       OR (bbox.xmin BETWEEN -93.71 AND -93.55 AND bbox.ymin BETWEEN 41.97 AND 42.08));

-- division_area; inspected 2026-09-27
SELECT id,names,subtype,sources,bbox,hex(ST_AsWKB(geometry)) as geometry_hex FROM read_parquet('s3://overturemaps-us-west-2/release/2026-09-23.1/theme=divisions/type=division_area/*',hive_partitioning=true)
    WHERE country='US' AND subtype IN ('neighborhood','macrohood','microhood') AND (
       (bbox.xmin BETWEEN -118.6 AND -118.0 AND bbox.ymin BETWEEN 34.0 AND 34.3 AND (names.primary ILIKE '%Los Feliz%' OR names.primary ILIKE '%Sherman Oaks%' OR names.primary ILIKE '%Bungalow%'))
       OR (bbox.xmin BETWEEN -87.8 AND -87.5 AND bbox.ymin BETWEEN 41.8 AND 42.1 AND names.primary ILIKE '%Lincoln Square%')
       OR (bbox.xmin BETWEEN -93.71 AND -93.55 AND bbox.ymin BETWEEN 41.97 AND 42.08));
