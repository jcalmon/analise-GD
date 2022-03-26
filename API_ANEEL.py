import pandas as pd
import streamlit as st
from IPython.display import Image
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config( layout = 'wide')

@st.cache
def get_data():
    data = pd.read_csv('GD.csv', sep=',')
    data = pd.DataFrame(data)
    data = data.drop('Unnamed: 0', axis=1)
    data['DthAtualizaCadastralEmpreend']= pd.to_datetime(data['DthAtualizaCadastralEmpreend']).dt.date
    data['MdaPotenciaInstaladaKW'] = data['MdaPotenciaInstaladaKW'].astype(float)
    data = data.sort_values(by='DthAtualizaCadastralEmpreend')
    return data

@st.cache(allow_output_mutation=True)
def bar(hue,xvalue,yvalue):
    plt.subplots(figsize=(4,4), facecolor=(.90, .90, .90))
    sns.barplot(x=xvalue,y = yvalue, data=data ,palette='magma',ci = None, hue=hue)
    return 0

#get data
data = get_data()
data_estatic = data.copy()


#estruturação sidebar
cp1, cc1 = st.sidebar.columns((1,1))
cgd1,cmuni1 = st.sidebar.columns((1,1))

#estruturação pagina
titulo, figura= st.columns((3,1))
titulo .title('Geração Distribuida no Brasil')
# imagem = Image.open('energia-renovavel.png')
# figura.image(imagem)
c1,test1,test2,test3,ctest= st.columns((1,1,1,1.2,3))
filt, mark= st.columns((3,1))
c, ctest2 = st.columns((3,1))
c2, c3, c4= st.columns((2,1,1))
c5, c6, c7= st.columns((2,1,1))
gf1, gf2=st.columns((1,2))
gf3, gf4 = st.columns((1,1))



#inicio e fim das data
lista_data = data['DthAtualizaCadastralEmpreend'].to_list()
start = pd.to_datetime(lista_data[0])
end = pd.to_datetime(lista_data[-1])

#filtro de data
start_date, end_date = mark.date_input('Escolha um intervalo de tempo: ', [start,end])
filtro_data = (data['DthAtualizaCadastralEmpreend']>= start_date) & (data['DthAtualizaCadastralEmpreend']<= end_date)
data = data.loc[filtro_data]


#filtros
agente = c.multiselect('Agentes', data['NomAgente'].unique())
consumo = c5.multiselect('Classe de consumo', data['DscClasseConsumo'].unique())
grupo_tarif = c6.multiselect('Grupo tarifário', data['DscSubGrupoTarifario'].unique())
estados = c4.multiselect('Estados', data['SigUF'].unique())
regiao = c3.multiselect('Região', data['NomRegiao'].unique())
modalidade = c2.multiselect('Modalidade', data['DscModalidadeHabilitado'].unique())
geracao = c7.multiselect('Tipo de geração', data['SigTipoGeracao'].unique())
Porte = ctest2.multiselect('Porte', data['DscPorte'].unique())

start_potencia, end_potencia = filt.select_slider(
                                                        'Potência instalada em KW',
                                                        data['MdaPotenciaInstaladaKW'].sort_values().unique(),
                                                        [data['MdaPotenciaInstaladaKW'].max(), data['MdaPotenciaInstaladaKW'].min()],
                                                        )
data = data[(data['MdaPotenciaInstaladaKW']>=start_potencia) & (data['MdaPotenciaInstaladaKW']<=end_potencia)]

#Lógica dos filtros
if (agente == []):
    data = data
else:
    data = data[data['NomAgente'].isin(agente)]

if (consumo == []):
    data = data
else:
    data = data[data['DscClasseConsumo'].isin(consumo)]

if (grupo_tarif == []):
    data = data
else:
    data = data[data['DscSubGrupoTarifario'].isin(grupo_tarif)]

if (estados == []):
    data = data
else:
    data = data[data['SigUF'].isin(estados)]

if (regiao == []):
    data = data
else:
    data = data[data['NomRegiao'].isin(regiao)]

if (modalidade == []):
    data = data
else:
    data = data[data['DscModalidadeHabilitado'].isin(modalidade)]

if (geracao == []):
    data = data
else:
    data = data[data['SigTipoGeracao'].isin(geracao)]

if (Porte == []):
    data = data
else:
    data = data[data['DscPorte'].isin(Porte)]


c1.markdown("")
test1.markdown("")
test2.markdown("")
test3.markdown("")
c1.markdown("")
test1.markdown("")
test2.markdown("")
test3.markdown("")
c1.markdown("")
test1.markdown("")
test2.markdown("")
test3.markdown("")
c1.markdown("")
test1.markdown("")
test2.markdown("")
test3.markdown("")
c1.markdown("")
test1.markdown("")
test2.markdown("")
test3.markdown("")
c1.markdown("")
test1.markdown("")
test2.markdown("")
test3.markdown("")
c1.markdown("")
test1.markdown("")
test2.markdown("")
test3.markdown("")
c1.markdown("")
test1.markdown("")
test2.markdown("")
test3.markdown("")
c1.markdown("")
test1.markdown("")
test2.markdown("")
test3.markdown("")
c1.markdown("")
test1.markdown("")
test2.markdown("")
test3.markdown("")



## Métricas de cálculo
potencia_total = data['MdaPotenciaInstaladaKW'].sum()
c1.write('Pot inst (kW)')
c1.markdown("---")
c1.write(f'{potencia_total:,.2f}')

credito_total = data['QtdUCRecebeCredito'].sum()
test1.write('UC crédito')
test1.markdown("---")
test1.write(f'{credito_total}')

num_gds = len(data)
test2.write('Qnt de GDs')
test2.markdown("---")
test2.write(f'{num_gds}')

num_municipios = len(data['NomMunicipio-UF'].unique())
test3.write('Municípios com GD')
test3.markdown("---")
test3.write(f'{num_municipios}')

c1.markdown("")
test1.markdown("")
test2.markdown("")
test3.markdown("")
c1.markdown("")
test1.markdown("")
test2.markdown("")
test3.markdown("")
c1.markdown("")
test1.markdown("")
test2.markdown("")
test3.markdown("")
c1.header('Filtros')


check_graf = gf1.checkbox('Gráfico de Barras')

if check_graf:
    color1 = gf1.color_picker('cor do gráfico1')
    color2 = gf2.color_picker('cor do gráfico2')


    with gf1.container():
        #grafico side bar
        group_bar = data.groupby('SigTipoGeracao').sum()[['MdaPotenciaInstaladaKW']].sort_values(by='MdaPotenciaInstaladaKW')
        fig_bar = px.bar(group_bar,
                         x='MdaPotenciaInstaladaKW',
                         y=group_bar.index,
                         width=500,
                         height=550,
                         labels={'SigTipoGeracao':''},
                         text_auto='.2s',
                         color_discrete_sequence=[color1]
        )

        fig_bar.update_layout(
                                plot_bgcolor='rgba(0,0,0,0)',
                                xaxis=(dict(showgrid=False))
        )
        st.plotly_chart(fig_bar)

    with gf2.container():
        #Grafico de Potencia por
        group_bar2 = data.groupby('SigUF').sum()[['MdaPotenciaInstaladaKW']].sort_values(by='MdaPotenciaInstaladaKW')
        fig_bar2 = px.bar(group_bar2,
                          y='MdaPotenciaInstaladaKW',
                          x=group_bar2.index,
                          width=800,
                          height=600,
                          labels={'SigUF':''},
                          text_auto='.2s',
                          color_discrete_sequence=[color2]

        )


        fig_bar2.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=(dict(showgrid=False))
        )
        st.plotly_chart(fig_bar2)


    with gf3.container():
        select_agrup = st.selectbox('Selecione um agrupamento',['NomAgente','DscClasseConsumo','DscSubGrupoTarifario','SigUF','NomRegiao','DscModalidadeHabilitado','SigTipoGeracao','DscPorte'])

        group_bar3 = data.groupby(select_agrup).sum()[['MdaPotenciaInstaladaKW']].sort_values(by='MdaPotenciaInstaladaKW')
        fig_bar3 = px.bar(group_bar3,
                         y='MdaPotenciaInstaladaKW',
                         x=group_bar3.index,
                         width=500,
                         height=500,
                         labels={'SigUF':''},
                         text_auto='.2s'
        )

        fig_bar3.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=(dict(showgrid=False))
        )
        st.plotly_chart(fig_bar3)

with ctest.container():
    percent = float((data['MdaPotenciaInstaladaKW'].sum() / data_estatic['MdaPotenciaInstaladaKW'].sum()))
    fig = go.Figure(go.Indicator(
        gauge = {'axis': {'range': [0.0, 1]}},
        mode = "gauge+number",
        value = percent,
        title = {'text': "Market Share","font":{"size":30}},
        number={"font":{"size":30}, 'valueformat':'.2%'})
        )
    st.plotly_chart(fig,use_container_width=True)

