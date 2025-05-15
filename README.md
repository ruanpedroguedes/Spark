# 📊 Atividade Aula 10 - Apache Spark


## 🧠 Descrição

Esta atividade tem como objetivo praticar o uso do Apache Spark para análise de dados e construção de pipelines de processamento distribuído. Foram realizadas análises exploratórias, cálculos estatísticos e criação de visualizações para extração de insights a partir de dados de vendas de produtos.

---

## ✅ Objetivos da Atividade

1. **Produtos mais vendidos por categoria:**
   Encontrar os produtos com maior quantidade de vendas em cada categoria.

2. **Ticket médio por mês:**
   Calcular o valor médio das vendas mensais.

3. **Tags associadas a produtos premium:**
   Identificar as tags mais comuns em produtos classificados como premium.

4. **Visualização da evolução das vendas:**
   Criar um gráfico que mostra o comportamento das vendas ao longo dos meses.

5. **Recomendação baseada em tags:**
   Implementar uma função que recomenda produtos com base em similaridade de tags.

---

## ⚙️ Tecnologias Utilizadas

* Apache Spark (PySpark)
* Python 3.x
* Pandas (para apoio nas visualizações, se necessário)
* Matplotlib / Seaborn (para gráficos)
* Jupyter Notebook ou script `.py`

---

## 📁 Estrutura do Projeto

```
atividade-aula10-spark/
├── data/
│   └── vendas.csv
├── main.py
├── README.md
```

---

## 📌 Como Executar

1. Instale os pacotes necessários:

```bash
pip install pyspark pandas matplotlib seaborn
```

2. Execute o script principal:

```bash
python main.py
```

---

## 📈 Funcionalidades Implementadas

### 1. Produtos Mais Vendidos por Categoria

Utilizando `groupBy` e `agg`, o Spark calcula os produtos com maior soma de quantidade vendida em cada categoria.

### 2. Ticket Médio por Mês

Conversão de datas e agregação mensal do valor médio de vendas (faturamento dividido por número de vendas).

### 3. Tags Associadas a Produtos Premium

Filtragem por produtos premium e extração das tags mais frequentes via transformação com `explode`.

### 4. Visualização de Evolução das Vendas

Uso de Pandas + Matplotlib para plotar o total de vendas ao longo do tempo.

### 5. Sistema de Recomendação por Tags

Função que identifica produtos com maior número de tags em comum com um produto de entrada.
