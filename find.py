"""Locate wkt errors."""
from __future__ import print_function
import arcpy
import os



def get_wkt_error_oids(feature):
    badones = []
    with arcpy.da.SearchCursor(feature,
                               ['SHAPE@WKT', 'OID@', 'SHAPE@'],
                               where_clause='OBJECTID > 0',
                               sql_clause=(None, 'ORDER BY OBJECTID')) as cursor:
        row = None
        while True:
            try:
                row = cursor.next()
                wkt = row[0]
                # if row[1] == 3808:
                #     print(wkt)
            except RuntimeError:
                print(row[1] + 1)
                print
                badones.append(row[1] + 1)
            except StopIteration:
                print('Complete')
                break
    print(badones)


if __name__ == '__main__':
    workspace = r'C:\Users\kwalker\AppData\Roaming\ESRI\Desktop10.3\ArcCatalog\Connection to sgid.agrc.utah.gov.sde'
    feature_path = os.path.join(workspace, 'SGID10.CADASTRE.Parcels_Tooele_LIR')
    get_wkt_error_oids(feature_path)
