import streamlit as st
from funciones_de_graficos import graficos_por_distrito, graficos_por_barrio
from graficos_precio_total_vivienda_barrios_en_cada_distrito import crear_grafico_precio_total_por_barrio, figuras_por_distrito

def main():
    # Título de la aplicación
    st.title('Explorando los Precios de Vivienda en Barcelona en el Año 2023')
    
    # Agregar la imagen al inicio de la página y hacerla más grande
    st.image("mapa_Barcelona_barrios_y_distritos_con_fondo_celeste.svg", width=800)

    # Botones para seleccionar grupo de gráficos
    if st.button('Graficar precio de vivienda por distrito'):
        figuras_distrito = graficos_por_distrito()
        for nombre_grafico, figura in figuras_distrito.items():
            st.subheader(nombre_grafico)
            st.plotly_chart(figura)

    if st.button('Graficar precio de vivienda por barrio'):
        figuras_barrio = graficos_por_barrio()
        for nombre_grafico, figura in figuras_barrio.items():
            st.subheader(nombre_grafico)
            st.plotly_chart(figura)
            
    # Botones para seleccionar grupo de gráficos
    if st.button('Mostrar gráficos de precios por barrio en cada distrito'):
        for nombre_grafico, figura in figuras_por_distrito.items():
            st.subheader(nombre_grafico)
            st.plotly_chart(figura)

if __name__ == "__main__":
    main()
