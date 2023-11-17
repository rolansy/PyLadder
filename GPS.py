from gmplot import gmplot
import csv

gmap=gmplot.GoogleMapPlotter(28.689169, 77.324448, 17 )

'''with open ('route.csv','r') as f:
    rr=csv.reader(f)
    
    for r in rr:
        lat=float(r[0])
        long=float(r[1])
        print(lat)
        print(long)
        print(lat+long)
        '''