import ast

def combine_sets(input_list):
    # Initialize an empty set to store all unique elements
    combined_set = set()

    # Process each input string and update the combined set
    for input_str in input_list:
        # Convert the string to an actual set using ast.literal_eval
        input_str = input_str.replace('\\', '\\\\')
        current_set = ast.literal_eval(input_str)
        print(len(list(current_set)))
        
        # Update the combined set with elements from the current set
        combined_set.update(current_set)

    # Return the combined set
    return combined_set


if __name__ == "__main__": 
    input_list = [
        "{'Dataset\\241.warc.wet.gz', 'Dataset\\118.warc.wet.gz', 'Dataset\\220.warc.wet.gz', 'Dataset\\135.warc.wet.gz', 'Dataset\\29.warc.wet.gz', 'Dataset\\202.warc.wet.gz', 'Dataset\\7.warc.wet.gz'}", 
        "{'Dataset\\389.warc.wet.gz', 'Dataset\\598.warc.wet.gz', 'Dataset\\447.warc.wet.gz', 'Dataset\\508.warc.wet.gz', 'Dataset\\550.warc.wet.gz', 'Dataset\\442.warc.wet.gz', 'Dataset\\348.warc.wet.gz', 'Dataset\\327.warc.wet.gz', 'Dataset\\490.warc.wet.gz', 'Dataset\\315.warc.wet.gz', 'Dataset\\388.warc.wet.gz', 'Dataset\\463.warc.wet.gz', 'Dataset\\592.warc.wet.gz', 'Dataset\\340.warc.wet.gz', 'Dataset\\487.warc.wet.gz', 'Dataset\\473.warc.wet.gz', 'Dataset\\514.warc.wet.gz', 'Dataset\\346.warc.wet.gz', 'Dataset\\594.warc.wet.gz', 'Dataset\\494.warc.wet.gz', 'Dataset\\534.warc.wet.gz', 'Dataset\\429.warc.wet.gz', 'Dataset\\587.warc.wet.gz', 'Dataset\\488.warc.wet.gz', 'Dataset\\486.warc.wet.gz', 'Dataset\\383.warc.wet.gz', 'Dataset\\318.warc.wet.gz', 'Dataset\\321.warc.wet.gz', 'Dataset\\391.warc.wet.gz', 'Dataset\\392.warc.wet.gz', 'Dataset\\491.warc.wet.gz', 'Dataset\\505.warc.wet.gz', 'Dataset\\597.warc.wet.gz', 'Dataset\\433.warc.wet.gz', 'Dataset\\541.warc.wet.gz', 'Dataset\\451.warc.wet.gz', 'Dataset\\456.warc.wet.gz', 'Dataset\\394.warc.wet.gz', 'Dataset\\476.warc.wet.gz', 'Dataset\\375.warc.wet.gz', 'Dataset\\582.warc.wet.gz', 'Dataset\\530.warc.wet.gz', 'Dataset\\589.warc.wet.gz'}",
        "{'Dataset\\818.warc.wet.gz', 'Dataset\\741.warc.wet.gz', 'Dataset\\871.warc.wet.gz', 'Dataset\\896.warc.wet.gz', 'Dataset\\858.warc.wet.gz', 'Dataset\\839.warc.wet.gz', 'Dataset\\862.warc.wet.gz', 'Dataset\\782.warc.wet.gz', 'Dataset\\882.warc.wet.gz', 'Dataset\\899.warc.wet.gz', 'Dataset\\717.warc.wet.gz', 'Dataset\\807.warc.wet.gz', 'Dataset\\806.warc.wet.gz', 'Dataset\\886.warc.wet.gz', 'Dataset\\712.warc.wet.gz', 'Dataset\\820.warc.wet.gz', 'Dataset\\894.warc.wet.gz', 'Dataset\\861.warc.wet.gz', 'Dataset\\692.warc.wet.gz', 'Dataset\\624.warc.wet.gz', 'Dataset\\811.warc.wet.gz', 'Dataset\\719.warc.wet.gz', 'Dataset\\608.warc.wet.gz', 'Dataset\\865.warc.wet.gz', 'Dataset\\887.warc.wet.gz', 'Dataset\\843.warc.wet.gz', 'Dataset\\859.warc.wet.gz', 'Dataset\\794.warc.wet.gz', 'Dataset\\810.warc.wet.gz', 'Dataset\\872.warc.wet.gz', 'Dataset\\860.warc.wet.gz', 'Dataset\\813.warc.wet.gz', 'Dataset\\866.warc.wet.gz', 'Dataset\\898.warc.wet.gz', 'Dataset\\869.warc.wet.gz', 'Dataset\\788.warc.wet.gz', 'Dataset\\851.warc.wet.gz', 'Dataset\\881.warc.wet.gz', 'Dataset\\847.warc.wet.gz', 'Dataset\\622.warc.wet.gz', 'Dataset\\884.warc.wet.gz', 'Dataset\\790.warc.wet.gz', 'Dataset\\897.warc.wet.gz', 'Dataset\\781.warc.wet.gz', 'Dataset\\789.warc.wet.gz', 'Dataset\\809.warc.wet.gz', 'Dataset\\891.warc.wet.gz', 'Dataset\\892.warc.wet.gz', 'Dataset\\841.warc.wet.gz', 'Dataset\\817.warc.wet.gz', 'Dataset\\885.warc.wet.gz', 'Dataset\\889.warc.wet.gz', 'Dataset\\853.warc.wet.gz', 'Dataset\\780.warc.wet.gz', 'Dataset\\824.warc.wet.gz', 'Dataset\\770.warc.wet.gz', 'Dataset\\699.warc.wet.gz', 'Dataset\\846.warc.wet.gz', 'Dataset\\867.warc.wet.gz', 'Dataset\\705.warc.wet.gz', 'Dataset\\877.warc.wet.gz', 'Dataset\\875.warc.wet.gz', 'Dataset\\830.warc.wet.gz', 'Dataset\\649.warc.wet.gz', 'Dataset\\796.warc.wet.gz', 'Dataset\\828.warc.wet.gz', 'Dataset\\834.warc.wet.gz', 'Dataset\\836.warc.wet.gz', 'Dataset\\713.warc.wet.gz', 'Dataset\\679.warc.wet.gz', 'Dataset\\627.warc.wet.gz', 'Dataset\\603.warc.wet.gz', 'Dataset\\670.warc.wet.gz', 'Dataset\\854.warc.wet.gz', 'Dataset\\876.warc.wet.gz', 'Dataset\\890.warc.wet.gz', 'Dataset\\880.warc.wet.gz', 'Dataset\\821.warc.wet.gz', 'Dataset\\888.warc.wet.gz', 'Dataset\\822.warc.wet.gz', 'Dataset\\864.warc.wet.gz', 'Dataset\\787.warc.wet.gz', 'Dataset\\791.warc.wet.gz', 'Dataset\\675.warc.wet.gz', 'Dataset\\863.warc.wet.gz', 'Dataset\\879.warc.wet.gz', 'Dataset\\883.warc.wet.gz', 'Dataset\\815.warc.wet.gz', 'Dataset\\654.warc.wet.gz', 'Dataset\\672.warc.wet.gz', 'Dataset\\621.warc.wet.gz', 'Dataset\\668.warc.wet.gz', 'Dataset\\874.warc.wet.gz', 'Dataset\\802.warc.wet.gz', 'Dataset\\617.warc.wet.gz', 'Dataset\\751.warc.wet.gz', 'Dataset\\677.warc.wet.gz', 'Dataset\\833.warc.wet.gz', 'Dataset\\739.warc.wet.gz', 'Dataset\\900.warc.wet.gz', 'Dataset\\798.warc.wet.gz', 'Dataset\\827.warc.wet.gz', 'Dataset\\857.warc.wet.gz', 'Dataset\\779.warc.wet.gz', 'Dataset\\629.warc.wet.gz', 'Dataset\\868.warc.wet.gz', 'Dataset\\850.warc.wet.gz'}",
        "{'Dataset\\1107.warc.wet.gz', 'Dataset\\1080.warc.wet.gz', 'Dataset\\1135.warc.wet.gz', 'Dataset\\1047.warc.wet.gz', 'Dataset\\1081.warc.wet.gz', 'Dataset\\1200.warc.wet.gz', 'Dataset\\927.warc.wet.gz', 'Dataset\\1172.warc.wet.gz', 'Dataset\\957.warc.wet.gz', 'Dataset\\967.warc.wet.gz', 'Dataset\\1199.warc.wet.gz', 'Dataset\\980.warc.wet.gz', 'Dataset\\1108.warc.wet.gz', 'Dataset\\974.warc.wet.gz', 'Dataset\\901.warc.wet.gz', 'Dataset\\1008.warc.wet.gz', 'Dataset\\992.warc.wet.gz', 'Dataset\\1179.warc.wet.gz', 'Dataset\\921.warc.wet.gz', 'Dataset\\1100.warc.wet.gz', 'Dataset\\1145.warc.wet.gz', 'Dataset\\1178.warc.wet.gz', 'Dataset\\1098.warc.wet.gz', 'Dataset\\1181.warc.wet.gz', 'Dataset\\1109.warc.wet.gz', 'Dataset\\1194.warc.wet.gz', 'Dataset\\1183.warc.wet.gz', 'Dataset\\1000.warc.wet.gz', 'Dataset\\979.warc.wet.gz', 'Dataset\\1064.warc.wet.gz', 'Dataset\\919.warc.wet.gz', 'Dataset\\1105.warc.wet.gz', 'Dataset\\962.warc.wet.gz', 'Dataset\\1180.warc.wet.gz', 'Dataset\\906.warc.wet.gz', 'Dataset\\933.warc.wet.gz', 'Dataset\\908.warc.wet.gz', 'Dataset\\1129.warc.wet.gz', 'Dataset\\1058.warc.wet.gz', 'Dataset\\917.warc.wet.gz', 'Dataset\\1113.warc.wet.gz', 'Dataset\\1176.warc.wet.gz', 'Dataset\\1055.warc.wet.gz', 'Dataset\\1056.warc.wet.gz', 'Dataset\\1174.warc.wet.gz', 'Dataset\\965.warc.wet.gz', 'Dataset\\1039.warc.wet.gz', 'Dataset\\1031.warc.wet.gz', 'Dataset\\951.warc.wet.gz', 'Dataset\\970.warc.wet.gz', 'Dataset\\1083.warc.wet.gz', 'Dataset\\1159.warc.wet.gz', 'Dataset\\960.warc.wet.gz', 'Dataset\\981.warc.wet.gz', 'Dataset\\1095.warc.wet.gz', 'Dataset\\1168.warc.wet.gz', 'Dataset\\1052.warc.wet.gz', 'Dataset\\1138.warc.wet.gz', 'Dataset\\1089.warc.wet.gz', 'Dataset\\1018.warc.wet.gz', 'Dataset\\1040.warc.wet.gz', 'Dataset\\923.warc.wet.gz', 'Dataset\\942.warc.wet.gz', 'Dataset\\1011.warc.wet.gz', 'Dataset\\1101.warc.wet.gz', 'Dataset\\1141.warc.wet.gz', 'Dataset\\1048.warc.wet.gz', 'Dataset\\1088.warc.wet.gz', 'Dataset\\924.warc.wet.gz', 'Dataset\\1175.warc.wet.gz', 'Dataset\\1111.warc.wet.gz', 'Dataset\\1087.warc.wet.gz', 'Dataset\\1140.warc.wet.gz', 'Dataset\\940.warc.wet.gz', 'Dataset\\1103.warc.wet.gz', 'Dataset\\1177.warc.wet.gz', 'Dataset\\1125.warc.wet.gz', 'Dataset\\1104.warc.wet.gz', 'Dataset\\938.warc.wet.gz', 'Dataset\\968.warc.wet.gz', 'Dataset\\1119.warc.wet.gz', 'Dataset\\1171.warc.wet.gz', 'Dataset\\973.warc.wet.gz', 'Dataset\\1149.warc.wet.gz', 'Dataset\\911.warc.wet.gz', 'Dataset\\1184.warc.wet.gz', 'Dataset\\1156.warc.wet.gz', 'Dataset\\1025.warc.wet.gz', 'Dataset\\1054.warc.wet.gz', 'Dataset\\1046.warc.wet.gz', 'Dataset\\1016.warc.wet.gz', 'Dataset\\1090.warc.wet.gz', 'Dataset\\1163.warc.wet.gz', 'Dataset\\1006.warc.wet.gz', 'Dataset\\1165.warc.wet.gz', 'Dataset\\976.warc.wet.gz', 'Dataset\\1196.warc.wet.gz', 'Dataset\\1063.warc.wet.gz', 'Dataset\\1091.warc.wet.gz', 'Dataset\\1097.warc.wet.gz', 'Dataset\\1185.warc.wet.gz', 'Dataset\\1099.warc.wet.gz', 'Dataset\\986.warc.wet.gz', 'Dataset\\1191.warc.wet.gz', 'Dataset\\1033.warc.wet.gz', 'Dataset\\1012.warc.wet.gz', 'Dataset\\1114.warc.wet.gz', 'Dataset\\963.warc.wet.gz', 'Dataset\\1132.warc.wet.gz', 'Dataset\\1187.warc.wet.gz', 'Dataset\\1017.warc.wet.gz', 'Dataset\\918.warc.wet.gz', 'Dataset\\937.warc.wet.gz', 'Dataset\\936.warc.wet.gz', 'Dataset\\1065.warc.wet.gz', 'Dataset\\1020.warc.wet.gz', 'Dataset\\958.warc.wet.gz', 'Dataset\\993.warc.wet.gz', 'Dataset\\1070.warc.wet.gz', 'Dataset\\1142.warc.wet.gz', 'Dataset\\1144.warc.wet.gz', 'Dataset\\1131.warc.wet.gz', 'Dataset\\1043.warc.wet.gz', 'Dataset\\1074.warc.wet.gz', 'Dataset\\1084.warc.wet.gz', 'Dataset\\959.warc.wet.gz', 'Dataset\\1019.warc.wet.gz', 'Dataset\\904.warc.wet.gz', 'Dataset\\1079.warc.wet.gz', 'Dataset\\1092.warc.wet.gz', 'Dataset\\1117.warc.wet.gz', 'Dataset\\1093.warc.wet.gz', 'Dataset\\1086.warc.wet.gz', 'Dataset\\1005.warc.wet.gz', 'Dataset\\1044.warc.wet.gz', 'Dataset\\1004.warc.wet.gz', 'Dataset\\971.warc.wet.gz', 'Dataset\\944.warc.wet.gz', 'Dataset\\997.warc.wet.gz', 'Dataset\\1152.warc.wet.gz', 'Dataset\\1154.warc.wet.gz', 'Dataset\\1057.warc.wet.gz', 'Dataset\\977.warc.wet.gz', 'Dataset\\1192.warc.wet.gz', 'Dataset\\1071.warc.wet.gz', 'Dataset\\1001.warc.wet.gz', 'Dataset\\1161.warc.wet.gz', 'Dataset\\950.warc.wet.gz', 'Dataset\\1134.warc.wet.gz', 'Dataset\\1155.warc.wet.gz', 'Dataset\\1146.warc.wet.gz', 'Dataset\\1182.warc.wet.gz', 'Dataset\\948.warc.wet.gz', 'Dataset\\1009.warc.wet.gz', 'Dataset\\1022.warc.wet.gz', 'Dataset\\1029.warc.wet.gz', 'Dataset\\1078.warc.wet.gz', 'Dataset\\1123.warc.wet.gz', 'Dataset\\939.warc.wet.gz', 'Dataset\\1169.warc.wet.gz', 'Dataset\\903.warc.wet.gz', 'Dataset\\1069.warc.wet.gz', 'Dataset\\1115.warc.wet.gz', 'Dataset\\1073.warc.wet.gz', 'Dataset\\1053.warc.wet.gz', 'Dataset\\1148.warc.wet.gz', 'Dataset\\988.warc.wet.gz', 'Dataset\\1062.warc.wet.gz', 'Dataset\\1076.warc.wet.gz', 'Dataset\\956.warc.wet.gz', 'Dataset\\1015.warc.wet.gz', 'Dataset\\1066.warc.wet.gz', 'Dataset\\955.warc.wet.gz', 'Dataset\\989.warc.wet.gz', 'Dataset\\1157.warc.wet.gz', 'Dataset\\914.warc.wet.gz', 'Dataset\\1118.warc.wet.gz', 'Dataset\\915.warc.wet.gz', 'Dataset\\1173.warc.wet.gz', 'Dataset\\964.warc.wet.gz', 'Dataset\\1045.warc.wet.gz', 'Dataset\\912.warc.wet.gz', 'Dataset\\1147.warc.wet.gz', 'Dataset\\975.warc.wet.gz', 'Dataset\\1122.warc.wet.gz', 'Dataset\\982.warc.wet.gz', 'Dataset\\910.warc.wet.gz', 'Dataset\\1049.warc.wet.gz', 'Dataset\\953.warc.wet.gz', 'Dataset\\1007.warc.wet.gz', 'Dataset\\1188.warc.wet.gz', 'Dataset\\1190.warc.wet.gz', 'Dataset\\1137.warc.wet.gz', 'Dataset\\913.warc.wet.gz', 'Dataset\\1038.warc.wet.gz', 'Dataset\\1150.warc.wet.gz', 'Dataset\\1061.warc.wet.gz', 'Dataset\\920.warc.wet.gz', 'Dataset\\1136.warc.wet.gz', 'Dataset\\1050.warc.wet.gz', 'Dataset\\969.warc.wet.gz', 'Dataset\\909.warc.wet.gz', 'Dataset\\1193.warc.wet.gz', 'Dataset\\1112.warc.wet.gz', 'Dataset\\943.warc.wet.gz', 'Dataset\\1032.warc.wet.gz', 'Dataset\\1067.warc.wet.gz', 'Dataset\\1102.warc.wet.gz', 'Dataset\\1021.warc.wet.gz', 'Dataset\\972.warc.wet.gz', 'Dataset\\1189.warc.wet.gz', 'Dataset\\1051.warc.wet.gz', 'Dataset\\1041.warc.wet.gz', 'Dataset\\1085.warc.wet.gz', 'Dataset\\1133.warc.wet.gz', 'Dataset\\952.warc.wet.gz', 'Dataset\\1023.warc.wet.gz', 'Dataset\\1026.warc.wet.gz', 'Dataset\\1151.warc.wet.gz', 'Dataset\\1072.warc.wet.gz', 'Dataset\\1153.warc.wet.gz', 'Dataset\\1127.warc.wet.gz', 'Dataset\\1068.warc.wet.gz', 'Dataset\\1082.warc.wet.gz', 'Dataset\\905.warc.wet.gz', 'Dataset\\954.warc.wet.gz', 'Dataset\\1010.warc.wet.gz', 'Dataset\\922.warc.wet.gz', 'Dataset\\926.warc.wet.gz', 'Dataset\\990.warc.wet.gz', 'Dataset\\966.warc.wet.gz', 'Dataset\\1042.warc.wet.gz', 'Dataset\\1035.warc.wet.gz', 'Dataset\\1139.warc.wet.gz', 'Dataset\\1013.warc.wet.gz', 'Dataset\\1162.warc.wet.gz', 'Dataset\\1030.warc.wet.gz', 'Dataset\\1077.warc.wet.gz', 'Dataset\\1143.warc.wet.gz', 'Dataset\\1060.warc.wet.gz', 'Dataset\\1014.warc.wet.gz', 'Dataset\\1003.warc.wet.gz', 'Dataset\\1197.warc.wet.gz', 'Dataset\\1158.warc.wet.gz', 'Dataset\\991.warc.wet.gz', 'Dataset\\1167.warc.wet.gz', 'Dataset\\1106.warc.wet.gz', 'Dataset\\934.warc.wet.gz', 'Dataset\\1121.warc.wet.gz', 'Dataset\\1024.warc.wet.gz', 'Dataset\\1028.warc.wet.gz', 'Dataset\\1059.warc.wet.gz', 'Dataset\\1096.warc.wet.gz', 'Dataset\\1120.warc.wet.gz', 'Dataset\\1130.warc.wet.gz', 'Dataset\\994.warc.wet.gz', 'Dataset\\945.warc.wet.gz', 'Dataset\\1160.warc.wet.gz', 'Dataset\\916.warc.wet.gz', 'Dataset\\946.warc.wet.gz', 'Dataset\\1126.warc.wet.gz', 'Dataset\\1128.warc.wet.gz', 'Dataset\\961.warc.wet.gz', 'Dataset\\1170.warc.wet.gz', 'Dataset\\1195.warc.wet.gz', 'Dataset\\1186.warc.wet.gz', 'Dataset\\932.warc.wet.gz', 'Dataset\\995.warc.wet.gz', 'Dataset\\1110.warc.wet.gz', 'Dataset\\1036.warc.wet.gz', 'Dataset\\1027.warc.wet.gz', 'Dataset\\1124.warc.wet.gz', 'Dataset\\1037.warc.wet.gz', 'Dataset\\1094.warc.wet.gz', 'Dataset\\930.warc.wet.gz', 'Dataset\\1034.warc.wet.gz', 'Dataset\\925.warc.wet.gz', 'Dataset\\1075.warc.wet.gz', 'Dataset\\1198.warc.wet.gz', 'Dataset\\907.warc.wet.gz', 'Dataset\\1116.warc.wet.gz', 'Dataset\\1166.warc.wet.gz', 'Dataset\\1164.warc.wet.gz', 'Dataset\\996.warc.wet.gz', 'Dataset\\929.warc.wet.gz'}",
        "{'Dataset\\1236.warc.wet.gz', 'Dataset\\1351.warc.wet.gz', 'Dataset\\1320.warc.wet.gz', 'Dataset\\1391.warc.wet.gz', 'Dataset\\1401.warc.wet.gz', 'Dataset\\1307.warc.wet.gz', 'Dataset\\1326.warc.wet.gz', 'Dataset\\1355.warc.wet.gz', 'Dataset\\1208.warc.wet.gz', 'Dataset\\1332.warc.wet.gz', 'Dataset\\1485.warc.wet.gz', 'Dataset\\1203.warc.wet.gz', 'Dataset\\1389.warc.wet.gz', 'Dataset\\1429.warc.wet.gz', 'Dataset\\1384.warc.wet.gz', 'Dataset\\1417.warc.wet.gz', 'Dataset\\1487.warc.wet.gz', 'Dataset\\1254.warc.wet.gz', 'Dataset\\1238.warc.wet.gz', 'Dataset\\1291.warc.wet.gz', 'Dataset\\1264.warc.wet.gz', 'Dataset\\1278.warc.wet.gz', 'Dataset\\1209.warc.wet.gz', 'Dataset\\1309.warc.wet.gz', 'Dataset\\1494.warc.wet.gz', 'Dataset\\1467.warc.wet.gz', 'Dataset\\1433.warc.wet.gz', 'Dataset\\1220.warc.wet.gz', 'Dataset\\1287.warc.wet.gz', 'Dataset\\1242.warc.wet.gz', 'Dataset\\1311.warc.wet.gz', 'Dataset\\1213.warc.wet.gz', 'Dataset\\1327.warc.wet.gz', 'Dataset\\1233.warc.wet.gz', 'Dataset\\1353.warc.wet.gz', 'Dataset\\1430.warc.wet.gz', 'Dataset\\1463.warc.wet.gz', 'Dataset\\1396.warc.wet.gz', 'Dataset\\1266.warc.wet.gz', 'Dataset\\1204.warc.wet.gz', 'Dataset\\1454.warc.wet.gz', 'Dataset\\1300.warc.wet.gz', 'Dataset\\1219.warc.wet.gz', 'Dataset\\1348.warc.wet.gz', 'Dataset\\1253.warc.wet.gz', 'Dataset\\1441.warc.wet.gz', 'Dataset\\1318.warc.wet.gz', 'Dataset\\1228.warc.wet.gz', 'Dataset\\1248.warc.wet.gz', 'Dataset\\1466.warc.wet.gz', 'Dataset\\1225.warc.wet.gz', 'Dataset\\1377.warc.wet.gz', 'Dataset\\1374.warc.wet.gz', 'Dataset\\1232.warc.wet.gz', 'Dataset\\1324.warc.wet.gz', 'Dataset\\1380.warc.wet.gz', 'Dataset\\1420.warc.wet.gz', 'Dataset\\1336.warc.wet.gz', 'Dataset\\1381.warc.wet.gz', 'Dataset\\1478.warc.wet.gz', 'Dataset\\1432.warc.wet.gz', 'Dataset\\1448.warc.wet.gz', 'Dataset\\1260.warc.wet.gz', 'Dataset\\1310.warc.wet.gz', 'Dataset\\1241.warc.wet.gz', 'Dataset\\1460.warc.wet.gz', 'Dataset\\1407.warc.wet.gz', 'Dataset\\1316.warc.wet.gz', 'Dataset\\1279.warc.wet.gz', 'Dataset\\1267.warc.wet.gz', 'Dataset\\1312.warc.wet.gz', 'Dataset\\1294.warc.wet.gz', 'Dataset\\1230.warc.wet.gz', 'Dataset\\1373.warc.wet.gz', 'Dataset\\1488.warc.wet.gz', 'Dataset\\1453.warc.wet.gz', 'Dataset\\1243.warc.wet.gz', 'Dataset\\1328.warc.wet.gz', 'Dataset\\1445.warc.wet.gz', 'Dataset\\1413.warc.wet.gz', 'Dataset\\1315.warc.wet.gz', 'Dataset\\1325.warc.wet.gz', 'Dataset\\1476.warc.wet.gz', 'Dataset\\1205.warc.wet.gz', 'Dataset\\1276.warc.wet.gz', 'Dataset\\1329.warc.wet.gz', 'Dataset\\1272.warc.wet.gz', 'Dataset\\1354.warc.wet.gz', 'Dataset\\1375.warc.wet.gz', 'Dataset\\1319.warc.wet.gz', 'Dataset\\1378.warc.wet.gz', 'Dataset\\1419.warc.wet.gz', 'Dataset\\1428.warc.wet.gz', 'Dataset\\1212.warc.wet.gz', 'Dataset\\1412.warc.wet.gz', 'Dataset\\1201.warc.wet.gz', 'Dataset\\1258.warc.wet.gz', 'Dataset\\1296.warc.wet.gz', 'Dataset\\1477.warc.wet.gz', 'Dataset\\1344.warc.wet.gz', 'Dataset\\1271.warc.wet.gz', 'Dataset\\1500.warc.wet.gz', 'Dataset\\1244.warc.wet.gz', 'Dataset\\1270.warc.wet.gz', 'Dataset\\1397.warc.wet.gz', 'Dataset\\1306.warc.wet.gz', 'Dataset\\1259.warc.wet.gz', 'Dataset\\1314.warc.wet.gz', 'Dataset\\1387.warc.wet.gz', 'Dataset\\1255.warc.wet.gz', 'Dataset\\1282.warc.wet.gz', 'Dataset\\1366.warc.wet.gz', 'Dataset\\1449.warc.wet.gz', 'Dataset\\1304.warc.wet.gz', 'Dataset\\1224.warc.wet.gz', 'Dataset\\1268.warc.wet.gz', 'Dataset\\1439.warc.wet.gz', 'Dataset\\1431.warc.wet.gz', 'Dataset\\1206.warc.wet.gz', 'Dataset\\1352.warc.wet.gz', 'Dataset\\1357.warc.wet.gz', 'Dataset\\1360.warc.wet.gz', 'Dataset\\1435.warc.wet.gz', 'Dataset\\1446.warc.wet.gz', 'Dataset\\1465.warc.wet.gz', 'Dataset\\1482.warc.wet.gz', 'Dataset\\1252.warc.wet.gz', 'Dataset\\1330.warc.wet.gz', 'Dataset\\1235.warc.wet.gz', 'Dataset\\1392.warc.wet.gz', 'Dataset\\1343.warc.wet.gz', 'Dataset\\1263.warc.wet.gz', 'Dataset\\1408.warc.wet.gz', 'Dataset\\1393.warc.wet.gz', 'Dataset\\1337.warc.wet.gz', 'Dataset\\1492.warc.wet.gz', 'Dataset\\1472.warc.wet.gz', 'Dataset\\1226.warc.wet.gz', 'Dataset\\1303.warc.wet.gz', 'Dataset\\1495.warc.wet.gz', 'Dataset\\1280.warc.wet.gz', 'Dataset\\1362.warc.wet.gz', 'Dataset\\1390.warc.wet.gz', 'Dataset\\1499.warc.wet.gz', 'Dataset\\1223.warc.wet.gz', 'Dataset\\1427.warc.wet.gz', 'Dataset\\1399.warc.wet.gz', 'Dataset\\1437.warc.wet.gz', 'Dataset\\1277.warc.wet.gz', 'Dataset\\1425.warc.wet.gz', 'Dataset\\1256.warc.wet.gz', 'Dataset\\1207.warc.wet.gz', 'Dataset\\1342.warc.wet.gz', 'Dataset\\1346.warc.wet.gz', 'Dataset\\1349.warc.wet.gz', 'Dataset\\1288.warc.wet.gz', 'Dataset\\1222.warc.wet.gz', 'Dataset\\1416.warc.wet.gz', 'Dataset\\1302.warc.wet.gz', 'Dataset\\1339.warc.wet.gz', 'Dataset\\1424.warc.wet.gz', 'Dataset\\1211.warc.wet.gz', 'Dataset\\1447.warc.wet.gz', 'Dataset\\1365.warc.wet.gz', 'Dataset\\1361.warc.wet.gz', 'Dataset\\1421.warc.wet.gz', 'Dataset\\1471.warc.wet.gz', 'Dataset\\1473.warc.wet.gz', 'Dataset\\1484.warc.wet.gz', 'Dataset\\1217.warc.wet.gz', 'Dataset\\1469.warc.wet.gz', 'Dataset\\1452.warc.wet.gz', 'Dataset\\1247.warc.wet.gz', 'Dataset\\1498.warc.wet.gz', 'Dataset\\1221.warc.wet.gz', 'Dataset\\1358.warc.wet.gz', 'Dataset\\1385.warc.wet.gz', 'Dataset\\1398.warc.wet.gz', 'Dataset\\1295.warc.wet.gz', 'Dataset\\1275.warc.wet.gz', 'Dataset\\1386.warc.wet.gz', 'Dataset\\1289.warc.wet.gz', 'Dataset\\1490.warc.wet.gz', 'Dataset\\1262.warc.wet.gz', 'Dataset\\1239.warc.wet.gz', 'Dataset\\1395.warc.wet.gz', 'Dataset\\1367.warc.wet.gz', 'Dataset\\1237.warc.wet.gz', 'Dataset\\1269.warc.wet.gz', 'Dataset\\1418.warc.wet.gz', 'Dataset\\1265.warc.wet.gz', 'Dataset\\1286.warc.wet.gz', 'Dataset\\1333.warc.wet.gz', 'Dataset\\1274.warc.wet.gz', 'Dataset\\1368.warc.wet.gz', 'Dataset\\1411.warc.wet.gz', 'Dataset\\1290.warc.wet.gz', 'Dataset\\1379.warc.wet.gz', 'Dataset\\1455.warc.wet.gz', 'Dataset\\1479.warc.wet.gz', 'Dataset\\1364.warc.wet.gz', 'Dataset\\1322.warc.wet.gz', 'Dataset\\1438.warc.wet.gz', 'Dataset\\1293.warc.wet.gz', 'Dataset\\1284.warc.wet.gz', 'Dataset\\1489.warc.wet.gz', 'Dataset\\1249.warc.wet.gz', 'Dataset\\1440.warc.wet.gz', 'Dataset\\1338.warc.wet.gz', 'Dataset\\1372.warc.wet.gz', 'Dataset\\1250.warc.wet.gz', 'Dataset\\1308.warc.wet.gz', 'Dataset\\1240.warc.wet.gz', 'Dataset\\1292.warc.wet.gz', 'Dataset\\1340.warc.wet.gz', 'Dataset\\1443.warc.wet.gz', 'Dataset\\1334.warc.wet.gz', 'Dataset\\1370.warc.wet.gz', 'Dataset\\1468.warc.wet.gz', 'Dataset\\1227.warc.wet.gz', 'Dataset\\1457.warc.wet.gz', 'Dataset\\1298.warc.wet.gz', 'Dataset\\1458.warc.wet.gz', 'Dataset\\1251.warc.wet.gz', 'Dataset\\1321.warc.wet.gz', 'Dataset\\1383.warc.wet.gz', 'Dataset\\1371.warc.wet.gz', 'Dataset\\1422.warc.wet.gz', 'Dataset\\1442.warc.wet.gz', 'Dataset\\1299.warc.wet.gz', 'Dataset\\1376.warc.wet.gz', 'Dataset\\1496.warc.wet.gz', 'Dataset\\1402.warc.wet.gz', 'Dataset\\1415.warc.wet.gz', 'Dataset\\1313.warc.wet.gz', 'Dataset\\1331.warc.wet.gz', 'Dataset\\1405.warc.wet.gz', 'Dataset\\1363.warc.wet.gz', 'Dataset\\1215.warc.wet.gz', 'Dataset\\1257.warc.wet.gz', 'Dataset\\1409.warc.wet.gz', 'Dataset\\1404.warc.wet.gz', 'Dataset\\1475.warc.wet.gz', 'Dataset\\1273.warc.wet.gz', 'Dataset\\1491.warc.wet.gz', 'Dataset\\1461.warc.wet.gz', 'Dataset\\1423.warc.wet.gz', 'Dataset\\1245.warc.wet.gz', 'Dataset\\1345.warc.wet.gz', 'Dataset\\1480.warc.wet.gz', 'Dataset\\1414.warc.wet.gz', 'Dataset\\1444.warc.wet.gz', 'Dataset\\1456.warc.wet.gz', 'Dataset\\1464.warc.wet.gz', 'Dataset\\1317.warc.wet.gz', 'Dataset\\1382.warc.wet.gz', 'Dataset\\1462.warc.wet.gz', 'Dataset\\1497.warc.wet.gz', 'Dataset\\1285.warc.wet.gz', 'Dataset\\1369.warc.wet.gz', 'Dataset\\1450.warc.wet.gz', 'Dataset\\1323.warc.wet.gz', 'Dataset\\1214.warc.wet.gz', 'Dataset\\1246.warc.wet.gz', 'Dataset\\1400.warc.wet.gz', 'Dataset\\1350.warc.wet.gz', 'Dataset\\1216.warc.wet.gz', 'Dataset\\1231.warc.wet.gz', 'Dataset\\1301.warc.wet.gz', 'Dataset\\1459.warc.wet.gz', 'Dataset\\1410.warc.wet.gz', 'Dataset\\1234.warc.wet.gz', 'Dataset\\1486.warc.wet.gz', 'Dataset\\1394.warc.wet.gz', 'Dataset\\1218.warc.wet.gz', 'Dataset\\1297.warc.wet.gz', 'Dataset\\1483.warc.wet.gz', 'Dataset\\1359.warc.wet.gz', 'Dataset\\1403.warc.wet.gz', 'Dataset\\1451.warc.wet.gz', 'Dataset\\1305.warc.wet.gz', 'Dataset\\1347.warc.wet.gz', 'Dataset\\1229.warc.wet.gz', 'Dataset\\1470.warc.wet.gz', 'Dataset\\1474.warc.wet.gz', 'Dataset\\1202.warc.wet.gz', 'Dataset\\1341.warc.wet.gz', 'Dataset\\1261.warc.wet.gz', 'Dataset\\1356.warc.wet.gz', 'Dataset\\1281.warc.wet.gz', 'Dataset\\1388.warc.wet.gz', 'Dataset\\1434.warc.wet.gz', 'Dataset\\1436.warc.wet.gz', 'Dataset\\1493.warc.wet.gz', 'Dataset\\1481.warc.wet.gz', 'Dataset\\1335.warc.wet.gz', 'Dataset\\1210.warc.wet.gz', 'Dataset\\1283.warc.wet.gz'}",
        "{'Dataset\\1550.warc.wet.gz', 'Dataset\\1800.warc.wet.gz', 'Dataset\\1793.warc.wet.gz', 'Dataset\\1670.warc.wet.gz', 'Dataset\\1665.warc.wet.gz', 'Dataset\\1737.warc.wet.gz', 'Dataset\\1768.warc.wet.gz', 'Dataset\\1713.warc.wet.gz', 'Dataset\\1770.warc.wet.gz', 'Dataset\\1611.warc.wet.gz', 'Dataset\\1695.warc.wet.gz', 'Dataset\\1605.warc.wet.gz', 'Dataset\\1529.warc.wet.gz', 'Dataset\\1743.warc.wet.gz', 'Dataset\\1610.warc.wet.gz', 'Dataset\\1777.warc.wet.gz', 'Dataset\\1558.warc.wet.gz', 'Dataset\\1546.warc.wet.gz', 'Dataset\\1570.warc.wet.gz', 'Dataset\\1613.warc.wet.gz', 'Dataset\\1645.warc.wet.gz', 'Dataset\\1681.warc.wet.gz', 'Dataset\\1643.warc.wet.gz', 'Dataset\\1707.warc.wet.gz', 'Dataset\\1631.warc.wet.gz', 'Dataset\\1771.warc.wet.gz', 'Dataset\\1779.warc.wet.gz', 'Dataset\\1630.warc.wet.gz', 'Dataset\\1594.warc.wet.gz', 'Dataset\\1530.warc.wet.gz', 'Dataset\\1607.warc.wet.gz', 'Dataset\\1562.warc.wet.gz', 'Dataset\\1506.warc.wet.gz', 'Dataset\\1701.warc.wet.gz', 'Dataset\\1598.warc.wet.gz', 'Dataset\\1769.warc.wet.gz', 'Dataset\\1714.warc.wet.gz', 'Dataset\\1527.warc.wet.gz', 'Dataset\\1656.warc.wet.gz', 'Dataset\\1503.warc.wet.gz', 'Dataset\\1668.warc.wet.gz', 'Dataset\\1776.warc.wet.gz', 'Dataset\\1715.warc.wet.gz', 'Dataset\\1573.warc.wet.gz', 'Dataset\\1746.warc.wet.gz', 'Dataset\\1647.warc.wet.gz', 'Dataset\\1729.warc.wet.gz', 'Dataset\\1752.warc.wet.gz', 'Dataset\\1675.warc.wet.gz', 'Dataset\\1575.warc.wet.gz', 'Dataset\\1535.warc.wet.gz', 'Dataset\\1595.warc.wet.gz', 'Dataset\\1653.warc.wet.gz', 'Dataset\\1723.warc.wet.gz', 'Dataset\\1791.warc.wet.gz', 'Dataset\\1586.warc.wet.gz', 'Dataset\\1698.warc.wet.gz', 'Dataset\\1687.warc.wet.gz', 'Dataset\\1725.warc.wet.gz', 'Dataset\\1516.warc.wet.gz', 'Dataset\\1583.warc.wet.gz', 'Dataset\\1648.warc.wet.gz', 'Dataset\\1663.warc.wet.gz', 'Dataset\\1501.warc.wet.gz', 'Dataset\\1555.warc.wet.gz', 'Dataset\\1571.warc.wet.gz', 'Dataset\\1636.warc.wet.gz', 'Dataset\\1538.warc.wet.gz', 'Dataset\\1742.warc.wet.gz', 'Dataset\\1764.warc.wet.gz', 'Dataset\\1580.warc.wet.gz', 'Dataset\\1644.warc.wet.gz', 'Dataset\\1762.warc.wet.gz', 'Dataset\\1511.warc.wet.gz', 'Dataset\\1629.warc.wet.gz', 'Dataset\\1659.warc.wet.gz', 'Dataset\\1682.warc.wet.gz', 'Dataset\\1696.warc.wet.gz', 'Dataset\\1711.warc.wet.gz', 'Dataset\\1790.warc.wet.gz', 'Dataset\\1797.warc.wet.gz', 'Dataset\\1758.warc.wet.gz', 'Dataset\\1761.warc.wet.gz', 'Dataset\\1721.warc.wet.gz', 'Dataset\\1523.warc.wet.gz', 'Dataset\\1740.warc.wet.gz', 'Dataset\\1747.warc.wet.gz', 'Dataset\\1799.warc.wet.gz', 'Dataset\\1780.warc.wet.gz', 'Dataset\\1783.warc.wet.gz', 'Dataset\\1710.warc.wet.gz', 'Dataset\\1717.warc.wet.gz', 'Dataset\\1565.warc.wet.gz', 'Dataset\\1748.warc.wet.gz', 'Dataset\\1504.warc.wet.gz', 'Dataset\\1604.warc.wet.gz', 'Dataset\\1655.warc.wet.gz', 'Dataset\\1509.warc.wet.gz', 'Dataset\\1576.warc.wet.gz', 'Dataset\\1741.warc.wet.gz', 'Dataset\\1753.warc.wet.gz', 'Dataset\\1514.warc.wet.gz', 'Dataset\\1619.warc.wet.gz', 'Dataset\\1525.warc.wet.gz', 'Dataset\\1685.warc.wet.gz', 'Dataset\\1612.warc.wet.gz', 'Dataset\\1709.warc.wet.gz', 'Dataset\\1716.warc.wet.gz', 'Dataset\\1689.warc.wet.gz', 'Dataset\\1660.warc.wet.gz', 'Dataset\\1515.warc.wet.gz', 'Dataset\\1528.warc.wet.gz', 'Dataset\\1666.warc.wet.gz', 'Dataset\\1788.warc.wet.gz', 'Dataset\\1755.warc.wet.gz', 'Dataset\\1781.warc.wet.gz', 'Dataset\\1518.warc.wet.gz', 'Dataset\\1640.warc.wet.gz', 'Dataset\\1544.warc.wet.gz', 'Dataset\\1775.warc.wet.gz', 'Dataset\\1678.warc.wet.gz', 'Dataset\\1679.warc.wet.gz', 'Dataset\\1614.warc.wet.gz', 'Dataset\\1730.warc.wet.gz', 'Dataset\\1620.warc.wet.gz', 'Dataset\\1589.warc.wet.gz', 'Dataset\\1626.warc.wet.gz', 'Dataset\\1560.warc.wet.gz', 'Dataset\\1676.warc.wet.gz', 'Dataset\\1564.warc.wet.gz', 'Dataset\\1796.warc.wet.gz', 'Dataset\\1596.warc.wet.gz', 'Dataset\\1628.warc.wet.gz', 'Dataset\\1637.warc.wet.gz', 'Dataset\\1547.warc.wet.gz', 'Dataset\\1587.warc.wet.gz', 'Dataset\\1703.warc.wet.gz', 'Dataset\\1700.warc.wet.gz', 'Dataset\\1552.warc.wet.gz', 'Dataset\\1531.warc.wet.gz', 'Dataset\\1556.warc.wet.gz', 'Dataset\\1584.warc.wet.gz', 'Dataset\\1646.warc.wet.gz', 'Dataset\\1782.warc.wet.gz', 'Dataset\\1794.warc.wet.gz', 'Dataset\\1568.warc.wet.gz', 'Dataset\\1635.warc.wet.gz', 'Dataset\\1641.warc.wet.gz', 'Dataset\\1649.warc.wet.gz', 'Dataset\\1567.warc.wet.gz', 'Dataset\\1608.warc.wet.gz', 'Dataset\\1622.warc.wet.gz', 'Dataset\\1720.warc.wet.gz', 'Dataset\\1760.warc.wet.gz', 'Dataset\\1657.warc.wet.gz', 'Dataset\\1699.warc.wet.gz', 'Dataset\\1688.warc.wet.gz', 'Dataset\\1561.warc.wet.gz', 'Dataset\\1585.warc.wet.gz', 'Dataset\\1658.warc.wet.gz', 'Dataset\\1639.warc.wet.gz', 'Dataset\\1789.warc.wet.gz', 'Dataset\\1597.warc.wet.gz', 'Dataset\\1778.warc.wet.gz', 'Dataset\\1672.warc.wet.gz', 'Dataset\\1536.warc.wet.gz', 'Dataset\\1521.warc.wet.gz', 'Dataset\\1745.warc.wet.gz', 'Dataset\\1661.warc.wet.gz', 'Dataset\\1578.warc.wet.gz', 'Dataset\\1692.warc.wet.gz', 'Dataset\\1712.warc.wet.gz', 'Dataset\\1718.warc.wet.gz', 'Dataset\\1505.warc.wet.gz', 'Dataset\\1533.warc.wet.gz', 'Dataset\\1680.warc.wet.gz', 'Dataset\\1772.warc.wet.gz', 'Dataset\\1735.warc.wet.gz', 'Dataset\\1677.warc.wet.gz', 'Dataset\\1543.warc.wet.gz', 'Dataset\\1559.warc.wet.gz', 'Dataset\\1774.warc.wet.gz', 'Dataset\\1519.warc.wet.gz', 'Dataset\\1625.warc.wet.gz', 'Dataset\\1787.warc.wet.gz', 'Dataset\\1553.warc.wet.gz', 'Dataset\\1563.warc.wet.gz', 'Dataset\\1551.warc.wet.gz', 'Dataset\\1554.warc.wet.gz', 'Dataset\\1532.warc.wet.gz', 'Dataset\\1569.warc.wet.gz', 'Dataset\\1507.warc.wet.gz', 'Dataset\\1526.warc.wet.gz', 'Dataset\\1690.warc.wet.gz', 'Dataset\\1733.warc.wet.gz', 'Dataset\\1591.warc.wet.gz', 'Dataset\\1582.warc.wet.gz', 'Dataset\\1765.warc.wet.gz', 'Dataset\\1719.warc.wet.gz', 'Dataset\\1697.warc.wet.gz', 'Dataset\\1795.warc.wet.gz', 'Dataset\\1590.warc.wet.gz', 'Dataset\\1691.warc.wet.gz', 'Dataset\\1759.warc.wet.gz', 'Dataset\\1572.warc.wet.gz', 'Dataset\\1549.warc.wet.gz', 'Dataset\\1638.warc.wet.gz', 'Dataset\\1581.warc.wet.gz', 'Dataset\\1650.warc.wet.gz', 'Dataset\\1727.warc.wet.gz', 'Dataset\\1704.warc.wet.gz', 'Dataset\\1542.warc.wet.gz', 'Dataset\\1545.warc.wet.gz', 'Dataset\\1792.warc.wet.gz', 'Dataset\\1693.warc.wet.gz', 'Dataset\\1785.warc.wet.gz', 'Dataset\\1750.warc.wet.gz', 'Dataset\\1738.warc.wet.gz', 'Dataset\\1749.warc.wet.gz', 'Dataset\\1773.warc.wet.gz', 'Dataset\\1642.warc.wet.gz', 'Dataset\\1708.warc.wet.gz', 'Dataset\\1763.warc.wet.gz', 'Dataset\\1566.warc.wet.gz', 'Dataset\\1616.warc.wet.gz', 'Dataset\\1540.warc.wet.gz', 'Dataset\\1517.warc.wet.gz', 'Dataset\\1602.warc.wet.gz', 'Dataset\\1520.warc.wet.gz', 'Dataset\\1686.warc.wet.gz', 'Dataset\\1706.warc.wet.gz', 'Dataset\\1599.warc.wet.gz', 'Dataset\\1513.warc.wet.gz', 'Dataset\\1652.warc.wet.gz', 'Dataset\\1592.warc.wet.gz', 'Dataset\\1634.warc.wet.gz', 'Dataset\\1726.warc.wet.gz', 'Dataset\\1593.warc.wet.gz', 'Dataset\\1623.warc.wet.gz', 'Dataset\\1724.warc.wet.gz', 'Dataset\\1510.warc.wet.gz', 'Dataset\\1731.warc.wet.gz', 'Dataset\\1739.warc.wet.gz', 'Dataset\\1767.warc.wet.gz', 'Dataset\\1522.warc.wet.gz', 'Dataset\\1603.warc.wet.gz', 'Dataset\\1662.warc.wet.gz', 'Dataset\\1557.warc.wet.gz', 'Dataset\\1624.warc.wet.gz', 'Dataset\\1606.warc.wet.gz', 'Dataset\\1600.warc.wet.gz', 'Dataset\\1632.warc.wet.gz', 'Dataset\\1651.warc.wet.gz', 'Dataset\\1669.warc.wet.gz', 'Dataset\\1621.warc.wet.gz', 'Dataset\\1786.warc.wet.gz', 'Dataset\\1617.warc.wet.gz', 'Dataset\\1798.warc.wet.gz', 'Dataset\\1754.warc.wet.gz', 'Dataset\\1512.warc.wet.gz', 'Dataset\\1756.warc.wet.gz', 'Dataset\\1627.warc.wet.gz', 'Dataset\\1537.warc.wet.gz', 'Dataset\\1751.warc.wet.gz', 'Dataset\\1728.warc.wet.gz', 'Dataset\\1732.warc.wet.gz', 'Dataset\\1574.warc.wet.gz', 'Dataset\\1683.warc.wet.gz', 'Dataset\\1705.warc.wet.gz', 'Dataset\\1502.warc.wet.gz', 'Dataset\\1702.warc.wet.gz', 'Dataset\\1609.warc.wet.gz', 'Dataset\\1671.warc.wet.gz', 'Dataset\\1654.warc.wet.gz', 'Dataset\\1766.warc.wet.gz', 'Dataset\\1674.warc.wet.gz', 'Dataset\\1615.warc.wet.gz', 'Dataset\\1579.warc.wet.gz', 'Dataset\\1667.warc.wet.gz', 'Dataset\\1548.warc.wet.gz', 'Dataset\\1577.warc.wet.gz', 'Dataset\\1784.warc.wet.gz', 'Dataset\\1734.warc.wet.gz', 'Dataset\\1684.warc.wet.gz', 'Dataset\\1601.warc.wet.gz', 'Dataset\\1539.warc.wet.gz', 'Dataset\\1694.warc.wet.gz', 'Dataset\\1722.warc.wet.gz', 'Dataset\\1664.warc.wet.gz', 'Dataset\\1673.warc.wet.gz', 'Dataset\\1744.warc.wet.gz', 'Dataset\\1618.warc.wet.gz', 'Dataset\\1757.warc.wet.gz', 'Dataset\\1524.warc.wet.gz', 'Dataset\\1736.warc.wet.gz', 'Dataset\\1541.warc.wet.gz', 'Dataset\\1508.warc.wet.gz', 'Dataset\\1588.warc.wet.gz', 'Dataset\\1534.warc.wet.gz'}",
        "{'Dataset\\1847.warc.wet.gz', 'Dataset\\1838.warc.wet.gz', 'Dataset\\1862.warc.wet.gz', 'Dataset\\1874.warc.wet.gz', 'Dataset\\1888.warc.wet.gz', 'Dataset\\1813.warc.wet.gz', 'Dataset\\1835.warc.wet.gz', 'Dataset\\1875.warc.wet.gz', 'Dataset\\1864.warc.wet.gz', 'Dataset\\1853.warc.wet.gz', 'Dataset\\1801.warc.wet.gz', 'Dataset\\1855.warc.wet.gz', 'Dataset\\1869.warc.wet.gz', 'Dataset\\1878.warc.wet.gz', 'Dataset\\1828.warc.wet.gz', 'Dataset\\1872.warc.wet.gz', 'Dataset\\1867.warc.wet.gz', 'Dataset\\1884.warc.wet.gz', 'Dataset\\1861.warc.wet.gz', 'Dataset\\1843.warc.wet.gz', 'Dataset\\1811.warc.wet.gz', 'Dataset\\1848.warc.wet.gz', 'Dataset\\1880.warc.wet.gz', 'Dataset\\1830.warc.wet.gz', 'Dataset\\1806.warc.wet.gz', 'Dataset\\1852.warc.wet.gz', 'Dataset\\1816.warc.wet.gz', 'Dataset\\1857.warc.wet.gz', 'Dataset\\1860.warc.wet.gz', 'Dataset\\1879.warc.wet.gz', 'Dataset\\1887.warc.wet.gz', 'Dataset\\1837.warc.wet.gz', 'Dataset\\1833.warc.wet.gz', 'Dataset\\1804.warc.wet.gz', 'Dataset\\1829.warc.wet.gz', 'Dataset\\1810.warc.wet.gz', 'Dataset\\1877.warc.wet.gz', 'Dataset\\1841.warc.wet.gz', 'Dataset\\1814.warc.wet.gz', 'Dataset\\1825.warc.wet.gz', 'Dataset\\1803.warc.wet.gz', 'Dataset\\1802.warc.wet.gz', 'Dataset\\1826.warc.wet.gz', 'Dataset\\1871.warc.wet.gz', 'Dataset\\1846.warc.wet.gz', 'Dataset\\1856.warc.wet.gz', 'Dataset\\1849.warc.wet.gz', 'Dataset\\1885.warc.wet.gz', 'Dataset\\1876.warc.wet.gz', 'Dataset\\1834.warc.wet.gz', 'Dataset\\1863.warc.wet.gz', 'Dataset\\1821.warc.wet.gz', 'Dataset\\1817.warc.wet.gz', 'Dataset\\1840.warc.wet.gz', 'Dataset\\1865.warc.wet.gz', 'Dataset\\1844.warc.wet.gz', 'Dataset\\1854.warc.wet.gz', 'Dataset\\1827.warc.wet.gz', 'Dataset\\1832.warc.wet.gz', 'Dataset\\1805.warc.wet.gz', 'Dataset\\1868.warc.wet.gz', 'Dataset\\1831.warc.wet.gz', 'Dataset\\1859.warc.wet.gz', 'Dataset\\1870.warc.wet.gz', 'Dataset\\1820.warc.wet.gz', 'Dataset\\1845.warc.wet.gz', 'Dataset\\1836.warc.wet.gz', 'Dataset\\1886.warc.wet.gz', 'Dataset\\1873.warc.wet.gz', 'Dataset\\1882.warc.wet.gz', 'Dataset\\1839.warc.wet.gz', 'Dataset\\1819.warc.wet.gz', 'Dataset\\1809.warc.wet.gz', 'Dataset\\1858.warc.wet.gz', 'Dataset\\1822.warc.wet.gz', 'Dataset\\1883.warc.wet.gz', 'Dataset\\1842.warc.wet.gz', 'Dataset\\1823.warc.wet.gz', 'Dataset\\1866.warc.wet.gz', 'Dataset\\1812.warc.wet.gz', 'Dataset\\1815.warc.wet.gz', 'Dataset\\1808.warc.wet.gz', 'Dataset\\1851.warc.wet.gz', 'Dataset\\1850.warc.wet.gz', 'Dataset\\1881.warc.wet.gz', 'Dataset\\1824.warc.wet.gz', 'Dataset\\1807.warc.wet.gz', 'Dataset\\1818.warc.wet.gz'}"                  
    ]

    combined = combine_sets(input_list)
    print(combined)
    print(len(combined))