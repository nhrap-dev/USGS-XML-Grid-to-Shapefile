# USGS-XML-Grid-to-Shapefile

## Requirements

- Python 3.X
- Python Package Dependencies - (conda install PACKAGENAME) or (pip install PACKAGENAME)

```
geopandas
shapely
```

## Use

1. Download the repository
2. Open the file xml-grid-to-shapefile.py and modify the input file and output directory at the bottom of the script.

```
# specify the inputs
xml_grid = 'INPUT_GRID.xml'
output_directory = r'C:\projects\NEIC\shapefiles\EXAMPLE'

# run the function
gdf = xml_grid_to_shapefile(xml_grid, output_directory)
```

3. If you have hazpy installed, double click on run-with-hazpy.py
4. If you do **not** have hazpy installed, you will need to open a terminal, activate a python virtual environment that contains the package dependecies, then run xml-grid-to-shapefile.py
