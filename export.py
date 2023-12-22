```python
# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from io import BytesIO
import base64

def export_visualization(export_data):
    """
    This function takes the visualization data and export format as input and exports the visualization 
    in the specified format. It supports exporting to PDF, PNG, and interactive web-based reports.
    """

    # Extract the data and format from the export_data
    df = pd.DataFrame(export_data['data'])
    export_format = export_data['format']

    # Export to PDF
    if export_format == 'pdf':
        pdf_export(df)

    # Export to PNG
    elif export_format == 'png':
        png_export(df)

    # Export to interactive web-based report
    elif export_format == 'web':
        web_export(df)

    # If the export format is not supported, return an error message
    else:
        return 'Error: The export format is not supported.'

    return 'Success: The visualization has been exported.'

def pdf_export(df):
    """
    This function takes a DataFrame as input and exports the visualization to a PDF file.
    """

    # Create a BytesIO object
    buf = BytesIO()

    # Save the figure to the BytesIO object
    plt.savefig(buf, format='pdf')

    # Get the PDF data from the BytesIO object
    pdf_data = buf.getvalue()

    # Close the BytesIO object
    buf.close()

    # Write the PDF data to a file
    with open('visualization.pdf', 'wb') as f:
        f.write(pdf_data)

def png_export(df):
    """
    This function takes a DataFrame as input and exports the visualization to a PNG file.
    """

    # Save the figure to a PNG file
    plt.savefig('visualization.png')

def web_export(df):
    """
    This function takes a DataFrame as input and exports the visualization to an interactive web-based report.
    """

    # Convert the DataFrame to HTML
    html = df.to_html()

    # Write the HTML to a file
    with open('visualization.html', 'w') as f:
        f.write(html)
```
