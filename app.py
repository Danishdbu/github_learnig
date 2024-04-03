import streamlit as st
st.title('campusx')

col1,col2 = st.columns(2)

with col1:
    st.image('unknown.jpg')
with col1:
    st.write("""A paragraph is defined as “a group of sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles, a paragraph can be just one sentence long.""")
st.header('Courses offer')
st.subheader('Data Science')
st.subheader('Data Analysis')
st.subheader('Ai')
