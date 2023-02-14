#Projeto Trader Objetivo 2023

#INÍCIO / IMPORTAÇÕES
#%%writefile app.py 
import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Trader Objetivo", page_icon="🔗",
                   layout="wide") 
st.set_option('deprecation.showPyplotGlobalUse', False)
st.markdown("""
<style>
.css-9s5bis.edgvbvh3{visibility: hidden;}
.css-164nlkn.egzxvld1{visibility: hidden;}
.css-1dp5vir.e8zbici1{visibility: hidden;}
</style>
""", unsafe_allow_html=True)


st.sidebar.image('AppTradeObjetivo_xlsx/01 Logo_TO.png')
st.title("Análise Estatística")

# Adicionando o selectbox à sidebar
st.sidebar.title("Selecione o Trade System")
opcoes = ['BB - Fechou Fora, Fechou Dentro', 'Cruzamento Di+ Di-', 'Dave Landry','Estocástico Lento 70x30', 'Gambitti', 'Gasparini', 'HiLo 7 períodos', 'IFR2 (Larry Connors)', 'IFR4 (Larry Connors)', 'InsideBar', 'Joe Biden', 
'Linha das sombras (Larry Williams)', 'Máximas e Mínimas', 'Medias 3 min/max ( Larry Williams)', 'Preço de Fechamento de Reversão', 
'Sistema MMA 9', 'Terminator (Larry Connors)', 'Tik Tok', 'Tik Tok (com filtro Solar)', 'Turtle (30 high / 20 low)' ]
opcao_selecionada = st.sidebar.selectbox("Escolha uma opção:", opcoes)

amostra = 6000
alavancagem = 1

# Incluindo o código acima no Streamlit app
st.sidebar.title("Seleção de Parâmetros")
# Barra de seleção para "Número de caixas"
num_caixas = st.sidebar.slider("Número de caixas:", 1, 5, 1)

if opcao_selecionada == "Joe Biden":
# Barra de seleção para "Alavancagem"
    alavancagem = st.sidebar.slider("Alavancagem:", 1, 15, 1)
elif opcao_selecionada == "Gasparini":
    alavancagem = st.sidebar.slider("Alavancagem:", 1, 15, 1)
elif opcao_selecionada == "Gambitti":
    alavancagem = st.sidebar.slider("Alavancagem:", 1, 15, 1)
elif opcao_selecionada == "Joe Biden":
    alavancagem = st.sidebar.slider("Alavancagem:", 1, 15, 1)
else:
    st.sidebar.write("Swing Trade sem alavancagem")

# Criar uma função para limpar a df
df = pd.DataFrame()

# Atribuir a base de dados ao sistema operacional selecionado
if st.sidebar.button("Calcular"): 
    df = pd.DataFrame()   
    if opcao_selecionada == "BB - Fechou Fora, Fechou Dentro":        
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_FFFD.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_FFFD.xlsx')
    elif opcao_selecionada == "Cruzamento Di+ Di-":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_DiDi.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_DiDi.xlsx')
    elif opcao_selecionada == "Dave Landry":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_DaveLandry.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_DaveLandry.xlsx')
    elif opcao_selecionada == "Estocástico Lento 70x30":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_EstocasticoLento70x30.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_EstocasticoLento70x30.xlsx')
    elif opcao_selecionada == "Gambitti":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_Gambit.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_Gambit.xlsx')
    elif opcao_selecionada == "Gasparini":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_gasparini.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_Gasparini.xlsx')
    elif opcao_selecionada == "HiLo 7 períodos":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_HiLo7p.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_HiLo7p.xlsx')
    elif opcao_selecionada == "IFR2 (Larry Connors)":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_IFR2.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_IFR2.xlsx')
    elif opcao_selecionada == "IFR4 (Larry Connors)":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_IFR4.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_IFR4.xlsx')
    elif opcao_selecionada == "InsideBar":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_InsideBar.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_InsideBar.xlsx')
    elif opcao_selecionada == "Joe Biden":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_JoeBiden.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_JoeBiden.xlsx')
    elif opcao_selecionada == "Linha das sombras (Larry Williams)":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_Linha_da_Sombra.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_Linha_da_Sombra.xlsx')
    elif opcao_selecionada == "Máximas e Mínimas":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_MaxMin.xlsx')
        df = pd.read_excel('APP_MC/AppTradeObjetivo_xlsx/trades_MaxMin.xlsx')
    elif opcao_selecionada == "Medias 3 min/max ( Larry Williams)":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_Média3Larry.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_Média3Larry.xlsx')
    elif opcao_selecionada == "Preço de Fechamento de Reversão":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_PFR.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_PFR.xlsx')
    elif opcao_selecionada == "Sistema MMA 9":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_SistemaMMA9.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_SistemaMMA9.xlsx')    
    elif opcao_selecionada == "Terminator (Larry Connors)":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_Terminator.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_Terminator.xlsx')
    elif opcao_selecionada == "Tik Tok":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_TikTok.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_TikTok.xlsx')
    elif opcao_selecionada == "Tik Tok (com filtro Solar)":
        backtest = pd.read_excel('AppTradeObjetivo_xlsx/bt_TikTok_FiltroSolar.xlsx')
        df = pd.read_excel('APP_MC/AppTradeObjetivo_xlsx/trades_TikTok_FiltroSolar.xlsx')
    elif opcao_selecionada == "Turtle (30 high / 20 low)":
        backtest = pd.read_excel('APP_MC/AppTradeObjetivo_xlsx/bt_Turtle.xlsx')
        df = pd.read_excel('AppTradeObjetivo_xlsx/trades_Turtle.xlsx')

    else:
        df = pd.DataFrame()   

    # Exibe o resultado na tela
    st.write("Sistema Operacional:", opcao_selecionada, "/ Número de caixas:", num_caixas, "Alavancagem:", alavancagem)
    # selecione as datas únicas
    unique_dates = df['Data de entrada'].unique()
    caixa = num_caixas

    # para cada data, selecione no máximo de linhas aleatórias respeitando número de caixas 
    random_rows = []
    for date in unique_dates:
        rows = df[df['Data de entrada'] == date]
        n_rows = min(caixa, len(rows))
        random_rows.append(rows.sample(n=n_rows, random_state=1))

    # concatene todas as linhas selecionadas em um único DataFrame
    random_df = pd.concat(random_rows)
    lista = pd.concat(random_rows)
    # se o número de linhas ainda for maior que 2.000, selecione mais linhas aleatórias
    if len(random_df) > amostra:
        random_df = random_df.sample(n=amostra, random_state=1)
    
    # Introdução da Alavancagem
    Alavancagem = alavancagem

    # redefinir o índice das linhas selecionadas
    random_df = random_df.reset_index(drop=True)
    
    # Adicione a nova coluna "Resultado" ao DataFrame
    random_df['Resultado'] = random_df['%'] * Alavancagem / caixa

    # Calcular a média dos valores de "Resultado"
    media = random_df['Resultado'].mean()

    ####### Calcular curva de capital 
    x = len(random_df)
    random_df['Lucro Acumulado'] = random_df['Resultado'].cumsum()
    random_df['Contagem'] = range(1,x+1)
    st.title("Curva de Capital")
    fig, ax = plt.subplots()
    ax.plot(random_df['Contagem'], random_df['Lucro Acumulado'])
    st.pyplot(width=1200)

    # Exibir o valor da média e Stops
    st.write("A média de Lucro por trade foi:", round(media, 2), "%")
    num_stop = (random_df['Tipo de saída'] == 'Stop Loss').sum()
    st.write("Número de Stop Loss: ", num_stop, " = ", round(num_stop*100/amostra, 2), "%")

    ###### Criar o gráfico de curva de Gauss
    st.title("Curva de Distribuição de Resultados")
    data = random_df["Resultado"]
    lower_bound = np.percentile(data, 10)
    upper_bound = np.percentile(data, 90)
    
    sns.distplot(random_df['Resultado'], kde=True, color='blue', hist_kws={'edgecolor':'black'})
    st.pyplot()
    st.write("O intervalo que corresponde a 80% dos resultados é", round(lower_bound, 2), "%", "e", round(upper_bound,2), "%")
          
    # Exibir o gráfico       
    chart = plt.figure(figsize=(20, 8))

    # Plotar a coluna "Resultado" no eixo y e o índice das linhas selecionadas no eixo x
    plt.plot(random_df.index, random_df['Resultado'])

    # Adicionar a linha da média ao gráfico
    plt.axhline(media, color='red', linestyle='dashed', linewidth=2)

    ##### Gráfico resultados trade a trade
    st.title("Gráfico de Resultado (trade a trade)")
    #plt.title('Gráfico de Resultados')

    # Adicionar legenda ao eixo y
    plt.ylabel('Resultado')

    # Adicionar legenda ao eixo x
    plt.xlabel('Número de amostra')

    # Exibir o gráfico na tela
    st.write(chart)

    # Criar coluna "Mês" a partir da coluna "Data"
    random_df['Mês'] = random_df['Data de entrada'].dt.strftime('%m')
    random_df['Ano'] = random_df['Data de entrada'].dt.strftime('%Y')
    random_df['Resultado'] = random_df['%'] * Alavancagem / caixa
    tabela = random_df.pivot_table(index='Ano', columns='Mês', values='Resultado', aggfunc='sum')
    tabela = tabela.fillna(0)
    
    ###### Gráfico resultados mensais
    st.title("Resultados mensais")
    plt.figure(figsize=(20,8))
    sns.heatmap(tabela, cmap='Greens', annot=True)
    st.pyplot()

    # Adicionar colunas com o mês e o ano de cada transação
    random_df['Month'] = pd.DatetimeIndex(random_df['Data de entrada']).month
    random_df['Year'] = pd.DatetimeIndex(random_df['Data de entrada']).year
    random_df['Day'] = pd.DatetimeIndex(random_df['Data de entrada']).day

    # Agrupar os resultados por mês e ano
    monthly_yearly_results = random_df.groupby(['Month', 'Year'])['Resultado'].sum()

    # Encontre o mês e ano com o melhor resultado
    max_month_year = monthly_yearly_results.idxmax()
    max_result = monthly_yearly_results.max()
   
    # Encontre o mês e ano com o pior resultado
    min_month_year = monthly_yearly_results.idxmin()
    min_result = monthly_yearly_results.min()
    
    # Calcular a média dos resultados mensais e anuais
    mean_monthly_yearly_results = monthly_yearly_results.mean()

    # Adicionar resultados ao Streamlit
    st.write("Melhor resultado mensal:", round(max_result, 2), "%")
    st.write("Pior resultado mensal:", round(min_result, 2), "%")
    st.write("Média dos resultados mensais:", round(mean_monthly_yearly_results, 2), "%")
    
    # Calcular o pior resultado diário
    worst_day_result = random_df.groupby('Data de entrada')['Resultado'].sum().min()
    st.write("O pior resultado diário foi:", round(worst_day_result, 2), "%")       

    ##### Teste Monte Carlo
    mc_df = pd.concat(random_rows)
    st.title("Teste de Monte Carlo")    
    if amostra > len(mc_df):
        amostra = len(mc_df)    
    simulations = []
    for i in range(100):  
        mc_df = df.sample(amostra)      
        mc_df['Lucro Acumulado'] = mc_df['%'].cumsum()
        mc_df['Contagem'] = range(1,x+1)
        simulations.append(mc_df)
    fig, ax = plt.subplots()
    for sim in simulations:
        ax.plot(sim['Contagem'], sim['Lucro Acumulado'], alpha=0.7)
    st.pyplot(width=1200)
           
    # Exibir Backtest   
    bt = backtest 
    bt.reset_index(drop=True, inplace=True)
    bt.index = bt.index + 1
    # Excluir colunas e alterar campos
    bt.drop(["Trades com lucro", "Saldo máximo", "Saldo mínimo", "Max Drawdown", "Expec. matemática"], axis=1, inplace=True)
    bt.rename(columns={"Expec. mat. lucratividade": "Exp. Mat."}, inplace=True)
    bt.rename(columns={"%": "Lucro Total (%)"}, inplace=True)
    st.title("Backtest por ativos do Ibov:")   
    # Permitir copiar dados
    st.write(bt) 

        
