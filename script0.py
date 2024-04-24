import os
import pandas

# define carpeta "in" y "out" de conversión
in_folder = './in'
out_folder = './out'

original_file_name = 'dataset CSV 20230831.csv'

# carga dataframe desde el CSV
csv_file = pandas.read_csv(os.path.join(in_folder, original_file_name), encoding='iso-8859-1')

"""
# Convierte todas las columnas con tipo int64 a int16
columns = ['mission_start_month', 'mission_start_year', 'mission_end_month', 'mission_end_year', 
           'appointment', 'region_2', 
           'mandate_start_month', 'mandate_start_year', 'mandate_end_month', 'mandate_end_year']

for column in columns:
    csv_file[column] = csv_file[column].astype('int16')

# Convierte todas las columnas tipo object a str
columns_2 = ['mission', 'country', 'region', 'appointment_2', 'last_name', 'name', 'gender', 'nationality']

for column in columns_2:
    xlsx_file[column] = xlsx_file[column].astype(str)
 """
print(csv_file.head)
print(csv_file['name'])

# define nombres de archivos convertidos y ruta de salida
base_file_name = 'dataset 20230831'
# CSV
csv_file_name = base_file_name + '.csv'
csv_file_path = os.path.join(out_folder, csv_file_name)
# DTA (stata full)
dta_file_name = base_file_name + '.dta'
dta_file_path = os.path.join(out_folder, dta_file_name)
# TAB (stata limited)
tab_file_name = base_file_name + '.tab'
tab_file_path = os.path.join(out_folder, tab_file_name)

# convierte a .dta
csv_file.to_stata(dta_file_path, write_index = False)
# .tab
csv_file.to_csv(tab_file_path, sep='\t', index=False)
# .csv
csv_file.to_csv(csv_file_path, index=False, encoding='iso-8859-1')