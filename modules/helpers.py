from IPython.display import display_html
import pandas as pd

def sample_df(upperleft, lowerright, prefix="", suffix=""):
    """
    Generate a Pandas DataFrame with values filled in based on the specified cell range.

    Parameters:
    upperleft (str): The upper-left cell of the DataFrame, in the format 'A1', 'B2', etc.
    lowerright (str): The lower-right cell of the DataFrame, in the format 'A1', 'B2', etc.
    prefix (str, optional): The prefix to be added to each value within the DataFrame. Defaults to an empty string.
    suffix (str, optional): The suffix to be added to each value within the DataFrame. Defaults to an empty string.

    Returns:
    pandas.DataFrame: A DataFrame with values filled in based on the specified cell range, prefixed and suffixed as specified.

    Example:
    >>> sample_df('A1', 'C3', prefix='X', suffix='_end')
          A       B       C
    1  XA1_end  XB1_end  XC1_end
    2  XA2_end  XB2_end  XC2_end
    3  XA3_end  XB3_end  XC3_end
    """
    col_start = ord(upperleft[0])
    col_end = ord(lowerright[0])

    row_start = int(upperleft[1:])
    row_end = int(lowerright[1:])

    if col_end < col_start: (col_start, col_end) = (col_end, col_start)
    if row_end < row_start: (row_start, row_end) = (row_end, row_start)

    cols = [chr(col) for col in range(col_start, col_end + 1)]
    rows = list(range(row_start, row_end + 1))

    values = [[f'{prefix}{col}{row}{suffix}' for col in cols] for row in rows]
    
    return pd.DataFrame(values, index=rows, columns=cols)

def hdisplay(dataframes, titles=None, space=50):
    """
    Display multiple Pandas DataFrames horizontally with customized titles and spacing.

    Parameters:
    dataframes (list): A list of Pandas DataFrames to be displayed horizontally.
    titles (list, optional): A list of titles for each DataFrame. If not provided, default titles will be used.
    space (int, optional): The spacing (in pixels) between the displayed DataFrames. Defaults to 50.

    Example:
    >>> df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    >>> df2 = pd.DataFrame({'X': [7, 8, 9], 'Y': [10, 11, 12]})
    >>> hdisplay([df1, df2], titles=['First DataFrame', 'Second DataFrame'], space=30)
    """

    html = ""

    if titles is None: titles = [f"DataFrame {n}" for n in range(len(dataframes))]

    styles = [
        dict(selector="th", props=[("text-align", "left"), ("vertical-align", "top")])
    ]

    for df, title in zip(dataframes, titles):
        html += (df.style.set_table_attributes(f"style='display:inline; margin-right: {space}px;'")
                 .set_caption(title)
                 .set_table_styles(styles)
                 ._repr_html_())

    display_html(html, raw=True)

def nowrap_display(dataframe):
    """
    Display the DataFrame without text wrapping.

    This function applies custom styling to the DataFrame, preventing text wrapping and ensuring that the text is displayed in a single line.

    Parameters:
    dataframe (pandas.DataFrame): The DataFrame to be displayed without text wrapping.

    Returns:
    None
    """

    html = (dataframe.style.set_properties(**{'font-size': '12pt', 'text-align': 'left', 'white-space': 'nowrap'})
             .set_table_styles([{'selector': 'th', 'props': [('text-align', 'left')]}]))._repr_html_()

    display_html(html, raw=True)