
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import findspark
# findspark ayuda a localizar Spark si no está en el PATH
# Si usas un entorno como Jupyter o Colab, a menudo no es necesario
# Pero es una buena práctica para scripts locales.
findspark.init()


# --- CONFIGURACIÓN DE RECURSOS PARA TU LAPTOP ---
# Nota: La configuración es para un uso seguro con 16 GB de RAM.
# Spark asignará memoria tanto para el Driver como para el Executor.

# Ruta al archivo JAR del conector JDBC de SQL Server que descargaste
JDBC_DRIVER_PATH = "/ruta/a/tu/mssql-jdbc-12.4.2.jre11.jar"  # <-- ¡ACTUALIZA ESTO!

# Parámetros de conexión a SQL Server
SQL_SERVER_HOST = "nombre_del_servidor"  # e.g., "localhost\SQLEXPRESS"
SQL_SERVER_PORT = "1433"
SQL_SERVER_DB = "nombre_de_la_base_de_datos"  # e.g., "MiBaseDeDatos"
SQL_SERVER_USER = "tu_usuario"
SQL_SERVER_PASSWORD = "tu_contraseña"
JDBC_URL = f"jdbc:sqlserver://{SQL_SERVER_HOST}:{SQL_SERVER_PORT};databaseName={SQL_SERVER_DB}"
DRIVER_CLASS = "com.microsoft.sqlserver.jdbc.SQLServerDriver"

# 1. Configuración de SparkSession
spark = SparkSession.builder \
    .appName("LocalSQLServerAnalysis") \
    .master("local[2]") \
    .config("spark.driver.memory", "8g") \
    .config("spark.executor.memory", "6g") \
    .config("spark.executor.cores", "2") \
    .config("spark.jars", JDBC_DRIVER_PATH) \
    .getOrCreate()

print("--- Configuración de PySpark Exitosa ---")
print(f"Modo de Ejecución: {spark.conf.get('spark.master')}")
print(f"Memoria del Driver: {spark.conf.get('spark.driver.memory')}")
print(f"Memoria del Executor: {spark.conf.get('spark.executor.memory')}")

# --- 2. Lectura de Datos desde SQL Server ---

# Ejemplo de lectura de una tabla grande (reemplaza 'MiTabla' por el nombre real)
df_spark = spark.read \
    .format("jdbc") \
    .option("url", JDBC_URL) \
    .option("dbtable", "MiTabla") \
    .option("user", SQL_SERVER_USER) \
    .option("password", SQL_SERVER_PASSWORD) \
    .option("driver", DRIVER_CLASS) \
    .load()

print("\n--- Lectura de Datos Exitosa ---")
print("Esquema de la tabla:")
df_spark.printSchema()
print(
    f"Número de particiones para esta lectura: {df_spark.rdd.getNumPartitions()}")

# --- 3. Ejemplo de Análisis y Procesamiento (Para tus 40 GB) ---

# Operación de transformación (Lazy Evaluation)
df_analisis = df_spark.filter(col("ColumnaImportante") > 100) \
                      .groupBy("ColumnaCategoria") \
                      .count()

print("\n--- Ejecutando Análisis (Acción) ---")
# Una acción fuerza la ejecución de las transformaciones (Lazy)
df_analisis.show(5)

# --- 4. Escritura de Datos de Vuelta a SQL Server (Ejemplo) ---

# Escritura del resultado a una nueva tabla en SQL Server
df_analisis.write \
    .format("jdbc") \
    .option("url", JDBC_URL) \
    .option("dbtable", "ResultadoAnalisisSpark")  # Nueva tabla en SQL Server
.option("user", SQL_SERVER_USER) \
    .option("password", SQL_SERVER_PASSWORD) \
    .option("driver", DRIVER_CLASS) \
    .mode("overwrite")  # Sobrescribe la tabla si existe
.save()

print("\n--- Datos Guardados en SQL Server (ResultadoAnalisisSpark) ---")

# Detener la SparkSession al finalizar
spark.stop()
print("SparkSession detenida.")
