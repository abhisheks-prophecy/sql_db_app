WITH all_type_non_partitioned AS (

  SELECT * 
  
  FROM {{ source('spark_catalog.qa_database', 'all_type_non_partitioned') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM all_type_non_partitioned AS in0

)

SELECT *

FROM Reformat_1
