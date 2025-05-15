from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, month, year, explode, split

# Iniciar Spark
spark = SparkSession.builder.appName("AtividadeSpark").getOrCreate()

#  Leitura dos dados
produtos = spark.read.csv("../dados/produtos.csv", header=True, inferSchema=True)
vendas = spark.read.csv("../dados/vendas.csv", header=True, inferSchema=True)

#  Juntar os dados
df = vendas.join(produtos, "produto_id")

#  1. Produtos mais vendidos por categoria
print("\n1. Produtos mais vendidos por categoria:\n")
df.groupBy("categoria", "nome") \
  .agg(sum("quantidade").alias("total_vendido")) \
  .orderBy("categoria", "total_vendido", ascending=False) \
  .show()

 #2. Ticket médio por mês
df = df.withColumn("ano", year("data")).withColumn("mes", month("data"))
print("\n2. Ticket médio por mês:\n")
df.groupBy("ano", "mes") \
  .agg(avg("valor").alias("ticket_medio")) \
  .orderBy("ano", "mes") \
  .show()

#  3. Tags mais associadas a produtos premium
print("\n3. Tags mais associadas a produtos premium:\n")
tags_premium = df.filter(col("produto_premium") == True) \
    .withColumn("tag", explode(split("tags", ",")))

tags_premium.groupBy("tag").count().orderBy("count", ascending=False).show()

 #4. Evolução das vendas (gráfico)
print("\n4. Evolução das vendas ao longo dos meses (gráfico):\n")
import pandas as pd
import matplotlib.pyplot as plt

evolucao = df.groupBy("ano", "mes") \
    .agg(sum("valor").alias("total_vendido")) \
    .orderBy("ano", "mes") \
    .toPandas()

evolucao["data"] = pd.to_datetime(evolucao["ano"].astype(str) + "-" + evolucao["mes"].astype(str))

plt.plot(evolucao["data"], evolucao["total_vendido"])
plt.title("Evolução das Vendas")
plt.xlabel("Data")
plt.ylabel("Total Vendido")
plt.grid(True)
plt.tight_layout()
plt.show()

#5. Função de recomendação por tags
print("\n5. Recomendação de produtos com base em tags:\n")

def recomendar(produto_nome, df):
    target_tags = df.filter(col("nome") == produto_nome).select("tags").first()[0]
    target_set = set(target_tags.split(","))

    def score(tags_str):
        if not tags_str:
            return 0
        return len(target_set.intersection(tags_str.split(",")))

    from pyspark.sql.functions import udf
    from pyspark.sql.types import IntegerType

    score_udf = udf(score, IntegerType())
    recomendados = df.withColumn("score", score_udf(col("tags")))

    recomendados.filter(col("nome") != produto_nome) \
        .select("nome", "score") \
        .distinct() \
        .orderBy("score", ascending=False) \
        .show()

# Exemplo de uso:
recomendar("Camiseta Estilosa", df)
