'''
Created on 21.01.2012

@author: kamikaze
'''
import unittest
from oleinikov_tasks import numbersarr2range, ranges2numbersarr,\
    numbersarr2prefixes
from random import shuffle


class OleinikovComTest(unittest.TestCase):


    def setUp(self):
        self.maxDiff = None
        self.numbersarr2range_expected_result = (
            "1191; 1195-1196; 1199; 1201-1203; 1205-1210;"
            " 1212-1219; 1224-1225; 1228-1229; 1231; 1234;"
            " 1239-1240; 1248; 1251-1254; 1256; 1260; 1262;"  
            " 1267; 1269-1270; 1276; 1281; 1301-1305;"
            " 1307-1310; 1312-1321; 1323; 1325; 1330-1331;" 
            " 1334; 1336-1337; 1339; 1347"
        )


    def tearDown(self):
        pass


    def test_numbersarr2range_ordered(self):
        input_data = [
            1191, 1195, 1196, 1199, 1201, 1202, 1203, 1205, 1206, 1207, 1208,
            1209, 1210, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1224,
            1225, 1228, 1229, 1231, 1234, 1239, 1240, 1248, 1251, 1252, 1253,
            1254, 1256, 1260, 1262, 1267, 1269, 1270, 1276, 1281, 1301, 1302,
            1303, 1304, 1305, 1307, 1308, 1309, 1310, 1312, 1313, 1314, 1315,
            1316, 1317, 1318, 1319, 1320, 1321, 1323, 1325, 1330, 1331, 1334,
            1336, 1337, 1339, 1347
        ]

        self.assertEqual(numbersarr2range(input_data),
                         self.numbersarr2range_expected_result)


    def test_numbersarr2range_shuffled(self):
        input_data = [
            1191, 1195, 1196, 1199, 1201, 1202, 1203, 1205, 1206, 1207, 1208,
            1209, 1210, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1224,
            1225, 1228, 1229, 1231, 1234, 1239, 1240, 1248, 1251, 1252, 1253,
            1254, 1256, 1260, 1262, 1267, 1269, 1270, 1276, 1281, 1301, 1302,
            1303, 1304, 1305, 1307, 1308, 1309, 1310, 1312, 1313, 1314, 1315,
            1316, 1317, 1318, 1319, 1320, 1321, 1323, 1325, 1330, 1331, 1334,
            1336, 1337, 1339, 1347
        ]
        shuffle(input_data)
        
        self.assertEqual(numbersarr2range(input_data),
                         self.numbersarr2range_expected_result)


    def test_ranges2numbersarr(self):
        input_data = '7676;7700-7702;7705;7707;771-772;7760-7764;7777'
        expected_result = [
            7676, 7700, 7701, 7702, 7705, 7707,
            771, 772, 7760, 7761, 7762, 7763, 7764, 7777,
        ]
        
        self.assertEqual(ranges2numbersarr(input_data), expected_result)


    def test_numbersarr2prefixes(self):
        input_data = '74952200000-74952209999;74952210000-74952210099;74952211000-74952211019;74952211050-74952211132;74952211134-74952211154'
        expected_result = [
            7495220, 749522100, 7495221100, 7495221101, 7495221105, 7495221106,
            7495221107, 7495221108, 7495221109, 7495221110, 7495221111,
            7495221112, 74952211130, 74952211131, 74952211132, 74952211134,
            74952211135, 74952211136, 74952211137, 74952211138, 74952211139,
            7495221114, 74952211150, 74952211151, 74952211152, 74952211153,
            74952211154, 
        ]

        self.assertEqual(numbersarr2prefixes(input_data), expected_result)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
