

from pyspark.sql import SparkSession

# =========================
# CONFIGURACIÓN GENERAL
# =========================

APP_NAME = "pyspark_local_sqlserver"

# Ajustes según tu hardware:
# - 2 núcleos → local[2]
# - 16 GB RAM → no asignar todo a Spark (dejar RAM al SO)
#   Driver: 6 GB
#   Executor: 6 GB

spark = (
    SparkSession.builder
    .appName(APP_NAME)
    .master("local[2]")

    # Memoria
    .config("spark.driver.memory", "6g")
    .config("spark.executor.memory", "6g")

    # Paralelismo y shuffles
    .config("spark.executor.cores", "2")
    .config("spark.sql.shuffle.partitions", "4")

    # Uso eficiente de memoria y disco
    .config("spark.memory.fraction", "0.6")
    .config("spark.memory.storageFraction", "0.3")

    # Arrow (opcional, útil si conviertes a pandas en datasets pequeños)
    .config("spark.sql.execution.arrow.pyspark.enabled", "true")

    # Driver JDBC de SQL Server (asegúrate de tener el .jar)
    .config(
        "spark.jars",
        "/ruta/al/sqljdbc42.jar"
    )

    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

print("Spark configurado correctamente en modo local")

# =========================
# CONEXIÓN A SQL SERVER
# =========================

JDBC_URL = (
    "jdbc:sqlserver://HOST:1433;"
    "databaseName=BASE_DATOS;"
    "encrypt=true;"
    "trustServerCertificate=true"
)

connection_properties = {
    "user": "USUARIO",
    "password": "PASSWORD",
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

# Lectura simple (tabla completa)
df = spark.read.jdbc(
    url=JDBC_URL,
    table="dbo.mi_tabla",
    properties=connection_properties
)

df.printSchema()
df.show(5)

df = spark.read.jdbc(
    url=JDBC_URL,
    table="dbo.mi_tabla",
    column="id",            # columna numérica indexada
    lowerBound=1,
    upperBound=10_000_000,  # ajusta según tu tabla
    numPartitions=2,        # igual a núcleos
    properties=connection_properties
)
df.write \
  .mode("append") \
  .option("batchsize", 10000) \
  .jdbc(
      url=JDBC_URL,
      table="dbo.tabla_destino",
      properties=connection_properties
  )
