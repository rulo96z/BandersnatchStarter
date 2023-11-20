from altair import Chart


def chart(df, x, y, target) -> Chart:
    """
    Create an Altair chart based on the provided DataFrame and encoding parameters.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - x (str): The column to be encoded on the x-axis.
    - y (str): The column to be encoded on the y-axis.
    - target (str): The column to be used for color encoding.

    Returns:
    - Chart: Altair chart object.
    """

    graph = Chart(df).mark_circle(size=70).encode(
        x = x,
        y = y,
        color = target,
        tooltip = df.columns.to_list()
    ).properties(
        title = f"{y} by {x} for {target}",
        height = 475,
        width = 450,
        padding = 40,
        background='#252525'
    ).configure_title(
        fontSize=25,
        color='#aaaaaa',
        offset=28
    ).configure_axis(
        labelColor='#aaaaaa',  
        titleColor='#aaaaaa',
        gridOpacity=0.1,
        titlePadding=20,
        domainColor='#aaaaaa'
    ).configure_legend(
        labelColor='#aaaaaa',
        titleColor='#aaaaaa'
    ).configure_view(
        stroke='transparent'
    )
    return graph
