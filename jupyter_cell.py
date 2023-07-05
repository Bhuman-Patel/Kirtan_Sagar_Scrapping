# All methods are used for manipulating cell in jupyter notebook
# here the value = Int(some no.) can also be set and in that case cell it auto-adopt the size
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_colwidth', None)

# Increasing the width of juypter cell to max
from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))