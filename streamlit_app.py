import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

st.set_option('deprecation.showPyplotGlobalUse', False)
# Loading dataset 
# Montar Google Drive
#drive.mount('/content/drive')

# Ruta del archivo en Google Drive
#file_path = '/content/drive/MyDrive/COLABORATORY/Pycaret/dataset03'

# Leer el archivo CSV
#df = pd.read_csv(file_path, header=None, names=['FONDO', 'CONCURSO', 'CONVOCATORIA', 'ANIO', 'MONTO_FINANCIAMIENTO', 'MONEDA'])
#-----------------
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

#st.title('Análisis exploratorio monto financiero de convocatoria')
#st.header('Esta aplicación permite explorar el conjunto de datos de monto financiero de convocatoria mediante diversos gráficos.')

#st.subheader("DataFrame")
#st.dataframe(df)
#selected_column = st.sidebar.selectbox('Select a column to visualize', df.columns)

#st.write("Histogram Plots")
#sns.histplot(df[selected_column])
#st.pyplot()

#st.write("Scatter plot")
#x_axis = st.sidebar.selectbox('Select the x-axis', df.columns)
#y_axis = st.sidebar.selectbox('Select the y-axis', df.columns)

#fig = px.scatter(df, x=x_axis, y=y_axis)
#st.plotly_chart(fig)

#st.write("Pair Plot")
#sns.pairplot(df, hue='class')
#st.pyplot()
#st.write("Description of the data")
#st.table(df.describe())

#st.header('Correlation Matrix')

#corr = df.corr()
#sns.heatmap(corr, annot=True)
#st.pyplot()

#st.header('Boxplot')

#fig = px.box(df, y=selected_column)
#st.plotly_chart(fig)

#selected_class = st.sidebar.selectbox('Select a class to visualize', df['class'].unique())

#if st.sidebar.button('Show Violin Plot'):
    #fig = px.violin(df[df['class'] == selected_class], y=selected_column)
    #st.plotly_chart(fig)






