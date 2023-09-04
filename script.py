import os
import pandas

# define carpeta "in" y "out" de conversión
in_folder = './in'
out_folder = './out'
xlsx_file_name = 'dataset Excel 20230831.xlsx'

# carga dataframe de xlsx, requiere openpyxl engine
xlsx_file = pandas.read_excel(os.path.join(in_folder, xlsx_file_name))

# define nombres de archivos convertidos
base_file_name = 'dataset 20230831'
dta_file_name = base_file_name + '.dta'
rda_file_name = base_file_name + '.rda'
tab_file_name = base_file_name + '.tab'

# convierte a .dta, .rda y .tab en "out"

