from re import sub
import openpyxl as xl
from openpyxl import descriptors
from openpyxl.chart import Barchart, Reference
from openpyxl.xml.constants import MAX_COLUMN, MAX_ROW, MIN_COLUMN, MIN MAX_ROW

wb = xl.load_workbook('ventas.xlsx')
sheet = wb['sheet']
cell = sheet['a1']

for row in range(2, sheet.max_row + 1):
    orderid = sheet.cell(row,1)
    productid = sheet.cell(row,2)
    qty = sheet.cell(row,3)
    price = sheet.cell(row,4)
    discount = sheet.cell(row,5)
    total = sheet.cell(row,6)


#Calculos

subtotal = qty.value * price.value
calculo = subtotal - (subtotal * discount.value / 100)

total.value =calculo

values= Reference (
    sheet,
    min_row=2,
    max_row=sheet.max_row,
    min_col=6,
    max_col=6

)