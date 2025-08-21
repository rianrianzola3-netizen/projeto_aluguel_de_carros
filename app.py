import streamlit as st


st.sidebar.title('rianzola aluguel de carros')

carros = ['BMW','ferrari','skyline','mustang']
modelo = st.sidebar.selectbox('escolha o carro',carros)

st.title('rianzola aluguel de carros')
st.write(f'voce escolheu {modelo}')
st.image(f'{modelo}.png')



