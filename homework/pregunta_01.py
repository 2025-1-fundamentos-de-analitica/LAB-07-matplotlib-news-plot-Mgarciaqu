"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import os
    import matplotlib.pyplot as plt
    import pandas as pd

    # Cargar los datos desde el archivo CSV
    df = pd.read_csv('files/input/news.csv', index_col=0)

    # Inicializar la figura para el gráfico
    plt.figure()

    # Especificar los colores para cada medio
    colors = {
        "Television": "dimgray",
        "Newspaper": "grey", 
        "Internet": "tab:blue",
        "Radio": "lightgrey",
    }

    # Asignar el orden z para las diferentes líneas
    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }

    # Determinar el grosor de las líneas
    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 4,
        'Radio': 2,
    }

    # Ajustar el título y la visibilidad de los ejes
    plt.title("How people get their news", fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    # Dibujar líneas y puntos para cada fuente de información
    for col in df.columns:
        first_year = df.index[0]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col],
        )

        # Trazar la línea correspondiente
        plt.plot(
            df.index,
            df[col],
            color=colors[col],
            linewidth=linewidths[col],
            zorder=zorder[col],
        )

        # Agregar el punto final de cada línea
        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
        )

        # Colocar etiquetas en los extremos de cada línea
        plt.text(
            first_year - 0.2,
            df[col][first_year],
            f"{col} {df[col][first_year]}%",
            ha='right',
            va='center',
            color=colors[col]
        )

        plt.text(
            last_year + 0.2,
            df[col][last_year],
            f"{df[col][last_year]}%",
            ha='left',
            va='center',
            color=colors[col]
        )

    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha='center'
    )

    plt.tight_layout()

    # Crear la carpeta de salida si no existe
    os.makedirs('files/plots', exist_ok=True)

    # Guardar el gráfico generado
    plt.savefig('files/plots/news.png', dpi=300, bbox_inches='tight')
    plt.show()
