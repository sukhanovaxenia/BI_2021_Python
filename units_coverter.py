
#This scripts will convert absorbing radiation units:

print('Absorbing radiation converter is launched!')

unit = int(input('Print your unit in Gy format: ', ))
<<<<<<< HEAD
out_format = input('Print to which format do you want to convert (mGy, mcrGy, rad=cGy): ', )
=======
out_format = input('Print to which format do you want to convert (mGy, mcrGy, rad): ', )
>>>>>>> 46f367f89d9d811059260a1c862ae369d599aa9b

absorb = {
        'mGy' : lambda unit: unit / 1000,
        'mcrGy' : lambda unit: unit / 1000000,
<<<<<<< HEAD
        'rad=cGy' : lambda unit: unit / 10000,
=======
        'rad' : lambda unit: unit / 10000,
>>>>>>> 46f367f89d9d811059260a1c862ae369d599aa9b
        }

print(f'In {out_format} your radiation is:', absorb[out_format](unit))
