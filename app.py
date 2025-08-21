import streamlit as st


st.sidebar.title('rianzola aluguel de carros')

carros = ['BMW','ferrari','skyline','mustang']
modelo = st.sidebar.selectbox('escolha o carro',carros)

st.title('rianzola aluguel de carros')
st.write(f'voce escolheu {modelo}')
st.image(f'{modelo}.png')

st.title('car future - aluguel de carros')

st.markdown(f'## voce escolheu um carro:{modelo}')
st.image(f'{modelo}.png')

if modelo== 'BMW' :
    diaria =500

elif modelo== 'mustang' :
    diaria =600

elif modelo == 'skyline' :
    diaria =700

elif modelo == 'ferrari' :
    diaria =1000

dias = st.text_input(f'por quantos dias voce alugou o {modelo}?')
km = st.text_input(f'quantos km voce rodou?')

if st.button('calcular') :
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km= km * 0.15
    aluguel = total_dias + total_km

    st. warning(f'voce alugou o {modelo} por {dias} e rodou {km}km. o valor do aluguel será r${aluguel}')

