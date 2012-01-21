'''
Created on 21.01.2012

@author: kamikaze
'''
import unittest
from oleinikov_tests import numbersarr2range
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
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
