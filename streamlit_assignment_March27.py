import streamlit as st
import altair as alt
import pandas as pd
import altair as alt


st.header('Streamlit Assignment March 27th')

st.markdown(
"Impact of climate change on Mortality rate and relation to GDP")


source = pd.read_csv("Streamlit_App_Temp_Climatechange.csv")
st.write(source)

brush = alt.selection_interval()

c = alt.Chart(source).mark_circle().encode(
    alt.X('years_2080_2099', scale=alt.Scale(zero=False)),
    alt.Y('Temperature', scale=alt.Scale(zero=False, padding=1)),
    color=alt.condition(brush, 'Country', alt.value('grey')),
    size='GDP',
    tooltip = ['Country', 'Temperature', 'years_2080_2099']
).add_selection(brush)


st.altair_chart(c, use_container_width=True)
