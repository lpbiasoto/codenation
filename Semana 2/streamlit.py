import streamlit as st
import pandas as pd

def main():
	st.title("Hello World")
	#st.header("This is a header")
	#st.subheader("This is a subheader")
	#st.text("This is a text")
	st.markdown("Botão")
	botao = st.button("Botão")
	if botao:
		st.markdown("Clicado")
	check = st.checkbox("Checkbox")
	if check:
		st.markdown("Clicado")

	st.markdown("Radio")
	radio = st.radio("Escolha as opções", ("Opt 1", "Opt 2"))

	if radio == "Opt 1":
		st.markdown("Opt 1")
	if radio == "Opt 2":
		st.markdown("Opt 2")
	st.markdown("Selectbox")

	select = st.selectbox("Choose opt", ("Opt 1", "Opt 2"))

	if select == "Opt 1":
		st.markdown("Opt 1")
	if select == "Opt 2":
		st.markdown("Opt 2")

	multi = st.multiselect ("Choose 1", ("Opt 1", "Opt 2"))
	if multi == "Opt 1":
		st.markdown("Opt 1")
	if multi == "Opt 2":
		st.markdown("Opt 2")

	file = st.file_uploader("Choose your file", type="csv")
	if file is not None:
		slider = st.slider("Valores", 1,100)
		df = pd.read_csv(file)
		st.dataframe(df.head(slider))
		st.dataframe(df.tail(slider))
		st.write(df.columns)


if __name__ == '__main__':
	main()