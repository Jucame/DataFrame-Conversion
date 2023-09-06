import os
import pandas

# define carpeta "in" y "out" de conversión
in_folder = './in'
out_folder = './out'
xlsx_file_name = 'dataset Excel 20230831.xlsx'

# carga dataframe de xlsx, requiere openpyxl engine
xlsx_file = pandas.read_excel(os.path.join(in_folder, xlsx_file_name))

# Convierte todas las columnas con tipo int64 a int16
columns = ['mission_start_month', 'mission_start_year', 'mission_end_month', 'mission_end_year', 
           'appointment', 'region_2', 
           'mandate_start_month', 'mandate_start_year', 'mandate_end_month', 'mandate_end_year']

for column in columns:
    xlsx_file[column] = xlsx_file[column].astype('int16')

# Convierte todas las columnas tipo object a str
columns_2 = ['mission', 'country', 'region', 'appointment_2', 'last_name', 'name', 'gender', 'nationality']

for column in columns_2:
    xlsx_file[column] = xlsx_file[column].astype(str)

print(xlsx_file.dtypes)
print(xlsx_file['country'])

# define nombres de archivos convertidos y ruta de salida
base_file_name = 'dataset 20230831'
# DTA (stata full)
dta_file_name = base_file_name + '.dta'
dta_file_path = os.path.join(out_folder, dta_file_name)
# TAB (stata limited)
tab_file_name = base_file_name + '.tab'
tab_file_path = os.path.join(out_folder, tab_file_name)

# convierte a .dta
xlsx_file.to_stata(dta_file_path, write_index = False, version=118)
# .tab
xlsx_file.to_csv(tab_file_path, sep='\t', index=False)