from zipfile import ZipFile
zipObj = ZipFile('sample.zip', 'w')
zipObj.write('Sample1.xlsx')
zipObj.write('Sample.xlsx')
zipObj.write('readme.xlsx')
zipObj.close()