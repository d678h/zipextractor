import zipfile

z_file = zipfile.ZipFile('your path')
z_file.extract('the name of your file (with extension)', 'your path')
z_file.close()
