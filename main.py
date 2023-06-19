import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Get a list of invoice Excel files
filepaths = glob.glob("invoices/*.xlsx")

# Iterate through each Excel file
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Generate pdf document for each Excel file
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Get the file name with extension
    filename = Path(filepath).stem
    # Get the invoice number and date of the invoice
    invoice_nr, date = filename.split("-")

    # Add invoice number to the page
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)

    # Add date of the invoice to the page
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date {date}", ln=1)

    pdf.output(f"PDFs/{filename}.pdf")
