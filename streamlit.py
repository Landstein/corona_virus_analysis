import streamlit as st

st.title("Covid-19 Data")
# st.header("Key Points")
# st.subheader("First, have good food.")
# st.text("Of all of the factors, quality of food displayed proved to be the most important factor.")

st.success("success")
st.info("info")
st.warning("warning")

st.write(['Corona', 'Virus'])

st.markdown('Example Mark Down Code')


employees = ['moes', 'selmas', 'pats']
for employee in employees:
    st.markdown(f'* {employee}')


names = ['fred', 'sam', 'sally']
text_input = ""
search_name = st.text_input("")
if st.button("Search"):
    search_name = search_name
if st.button("Clear"):
    search_name = ""
if search_name:
    names = [name for name in names if name.startswith(search_name)]
for name in names:
    st.markdown(f'* {name}')