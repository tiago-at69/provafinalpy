
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel ("dados-educacao.xlsx")
df_mestrado = df[df["escolaridade"] == "Mestrado"]
contagem_genero = df_mestrado["genero"].value_counts()
print(contagem_genero)

# 1. titulo do painel
st.title("Pessoas com Mestrado por Gênero")

# 2. leitura e filtragem dos dados
df = pd.read_excel("dados-educacao.xlsx", engine="calamine")

df_mestrado = df[df["escolaridade"] == "Mestrado"]
contagem = (
    df_mestrado.groupby("genero")
    .size()
    .reset_index(name="Quantidade")
)

# 3. barra lateral
opcao = st.sidebar.radio(
    "Selecione a visualização:",
    ["Tabela", "Gráfico"]
)

if opcao == "Tabela":
    st.header("Tabela: Número de pessoas com mestrado por gênero")
    st.dataframe(contagem, use_container_width=True)

elif opcao == "Gráfico":
    st.header("Gráfico: Número de pessoas com mestrado por gênero")
    fig = px.bar(
        contagem,
        x="genero",
        y="Quantidade",
        color="genero",
        labels={"genero": "Gênero", "Quantidade": "Número de Pessoas"},
        title="Pessoas com Mestrado (Masculino vs. Feminino)"
    )
    st.plotly_chart(fig, use_container_width=True)