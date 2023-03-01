import io
import streamlit as st
import csv

st.set_page_config(layout="centered", page_title="Construtor de Regex e Links para Produtos Auchan")

st.title(" Construtor de Regex e Links para Produtos da Auchan 😎 ")

st.header("Faz upload de um ficheiro csv, onde a primeira coluna lista todas as referências desejadas")
uploaded_file = st.file_uploader('Upload de Ficheiro',type=['csv'])


st.markdown(
 """
<style>

@import url('https://fonts.googleapis.com/css2?family=Roboto');

    html, body, [class*="css"]  {
    font-family: 'Roboto', sans-serif;
    }


h1 {
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    width: auto;
}

h2 {
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    width: auto;
    font-size: 20px;
}
""",
unsafe_allow_html=True
    
)

st.header("Ou faz copiar/colar diretamente da lista que esteja em Sheets/Excel")

user_list=st.text_input("Por favor insere a tua lista de referências aqui. Clica Enter para aplicar.")

if uploaded_file is not None:
    # create a file-like object from the uploaded file
    file_contents = uploaded_file.getvalue()
    file_io = io.StringIO(file_contents.decode('utf-8'))
    
    # read the CSV contents using the csv.reader() function
    reader = csv.reader(file_io)
    next(reader)  # skip header
    rows = [row[0] for row in reader if row[0].strip()]  # extract non-empty rows
    
    # concatenate rows and add '^' and '$' to the beginning and end, respectively
    concatenated_string = "|".join(rows)
    # concatenated_string = "$|^".join(rows)
    prod_link='https://www.auchan.pt/pt/produtos/?prefn1=id&prefv1='+concatenated_string

    if rows:
        concatenated_string = f"^({concatenated_string}"
        concatenated_string += ")$"
    
    # display the concatenated string
    st.header('Código Regex para usar em análise')
    st.code(concatenated_string, language='regex')

    st.header('Link de produto para ser acedido em auchan.pt')
    st.text('Nota: o website só permite ter até cerca de 100-200 referências por link')
    st.code(prod_link, language='uri')


elif user_list is not None:
    
    list_split=user_list.split()
    # # concatenate rows and add '^' and '$' to the beginning and end, respectively
    concatenated_string = "|".join(list_split)

    prod_link='https://www.auchan.pt/pt/produtos/?prefn1=id&prefv1='+concatenated_string


    concatenated_string = f"^({concatenated_string}"
    concatenated_string += ")$"
    
    # # display the concatenated string
    st.header('Código Regex para usar em análise')
    st.code(concatenated_string, language='regex')

    st.header('Link de produto para ser usado em auchan.pt')
    st.text('Nota: o website só permite ter até cerca de 100-200 referências por link')
    st.code(prod_link, language='uri')


