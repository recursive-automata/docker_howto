from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

conf = SparkConf().setAppName('count_connections').setMaster('local[*]')
sc = SparkContext(conf=conf)
spark = SparkSession(sc)

x = spark.range(1000)
x_1 = x.select(col('id').alias('id_1'))
x_2 = x.select(col('id').alias('id_2'))

y = (
    x_1.crossJoin(x_2)
    .filter(col('id_1') < col('id_2'))
    .sample(False, 0.01)
)

connections = y
connections.cache()
connections.show(20)
connections.createOrReplaceTempView('connections')


connection_counts = spark.sql('''

SELECT id,
       COUNT(*) AS n_connections

FROM (
    SELECT id_1 AS id
    FROM connections
    UNION ALL
    SELECT id_2 AS id
    FROM connections
    )

GROUP BY 1
ORDER BY 2 DESC

''')


connection_counts.show(20)
connection_counts.createOrReplaceTempView('connection_counts')


avg_connections = spark.sql(

    'SELECT COUNT(*), AVG(n_connections) FROM connection_counts'

).collect()[0]


msg = '''
{0} ids in the dataset,
with an average connection count of {1}.
'''.format(*avg_connections)

print(msg)

spark.stop()

