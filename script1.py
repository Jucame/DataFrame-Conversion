import os
import pandas

# define carpeta "in" y "out" de conversión
IN_FOLDER = './in'
OUT_FOLDER = './out'

csv_file_name = 'dataset CSV 20230831.csv'
xlsx_file_name = 'dataset CSV_to_EXCEL 20230831.xlsx'

# carga dataframe desde el CSV (manual)
csv_file = pandas.read_csv(os.path.join(IN_FOLDER, csv_file_name), encoding='iso-8859-1')

# define nombres de archivos convertidos y rutas de salida
base_name_0 = 'dataset '
base_name_1 = ' 20230831'

# CSV
csv_file_name = base_name_0 + "CSV" + base_name_1 + '.csv'
csv_file_path = os.path.join(OUT_FOLDER, csv_file_name)
# DTA (stata full)
dta_file_name = base_name_0 + "DTA" + base_name_1 + '.dta'
dta_file_path = os.path.join(OUT_FOLDER, dta_file_name)
# TAB (stata limited)
tab_file_name = base_name_0 + "TAB" + base_name_1 + '.tab'
tab_file_path = os.path.join(OUT_FOLDER, tab_file_name)

# convierte a 
# .dta
#csv_file.to_stata(dta_file_path, write_index = False)
# .tab
csv_file.to_csv(tab_file_path, sep='\t', index=False, encoding='iso-8859-1')
# .csv
#csv_file.to_csv(csv_file_path, index=False, encoding='iso-8859-1')