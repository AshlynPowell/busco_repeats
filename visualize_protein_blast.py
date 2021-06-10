import sys
import numpy as np 
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.io import export_png
from bokeh.models import ColumnDataSource, DataTable, DateFormatter, TableColumn

Piwi = sys.argv[1]
Ago1 = sys.argv[2]
filePath = Piwi[0:20]

data = {}

with open(Piwi, 'r') as PiwiData:
    for line in PiwiData:
        if line.startswith('# D') or line.startswith('# F') or line.startswith('# T') or line.startswith("#") == False or line.startswith('# B'):
            continue
        elif line.startswith("# Q"):
            queryLine = line.strip('\n').split(' ')
            name = queryLine[2]
        else:
            hitsLine = line.strip('\n').split(' ')
            hits = int(hitsLine[1])
            data[name] = hits

with open(Ago1, 'r') as Ago1Data:
    for line in Ago1Data:
        if line.startswith('# D') or line.startswith('# F') or line.startswith('# T') or line.startswith("#") == False or line.startswith('# B'):
            continue
        elif line.startswith("# Q"):
            queryLine = line.strip('\n').split(' ')
            name = queryLine[2]
        else:
            hitsLine = line.strip('\n').split(' ')
            hits = int(hitsLine[1])
            data[name] = hits

allHits = sorted(data.values())
genes = [*range(0,len(allHits))]

p = figure(plot_height = 600, plot_width = 1200, 
           title = filePath,
          y_axis_label = 'Number of Hits', 
           x_axis_label = 'Genes')

p.line(x = genes, y = allHits, line_width = 3, color = "midnightblue")
#show(p)
export_png(p, filename=filePath + "lineplot.png")

writeLine = Piwi[0:20]
for item in sorted(data.keys()):
    writeLine += ',' + str(data[item])

with open('results.csv', 'a') as results:
    results.write("\n" + writeLine)









