#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21.01.2012

@author: kamikaze
'''

def numbersarr2range(numbers):
    n_generator = (str(n) for n in numbers)
    return ' '.join(n_generator)

def main():
    input_data = [
        1191, 1195, 1196, 1199, 1201, 1202, 1203, 1205, 1206, 1207, 1208, 1209, 1210,
        1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1224, 1225, 1228, 1229, 1231,
        1234, 1239, 1240, 1248, 1251, 1252, 1253, 1254, 1256, 1260, 1262, 1267, 1269,
        1270, 1276, 1281, 1301, 1302, 1303, 1304, 1305, 1307, 1308, 1309, 1310, 1312,
        1313, 1314, 1315, 1316, 1317, 1318, 1319, 1320, 1321, 1323, 1325, 1330, 1331,
        1334, 1336, 1337, 1339, 1347
    ]
    
    output_data = numbersarr2range(input_data)
    print(output_data)

if __name__ == '__main__':
    main()