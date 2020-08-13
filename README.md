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

3. Run the script

- If you have hazpy installed, double click on run-with-hazpy.py
- If you do not have hazpy installed, you will need to open a terminal, activate a python virtual environment that contains the package dependecies, then run xml-grid-to-shapefile.py

### Optional

The xml_grid_to_shapefile method has optional parameters that may be beneficial. They can be added indepdently or used together.

- convex_hull - this will export a convex hull, or the minimum bounding polygon, around the xml grid points. To use:

  ```
  gdf = xml_grid_to_shapefile(xml_grid, output_directory, convex_hull=True)
  ```

- pga_threshold - this will limit the grid that is converted by a minimum PGA. A good default is 10 (>= 0.1 PGA) since the value is expressed as a percentage.

  ```
  gdf = xml_grid_to_shapefile(xml_grid, output_directory, pga_threshold=10)
  ```

- here is an example using the optional parameters in conjunction

  ```
  gdf = xml_grid_to_shapefile(xml_grid, output_directory, convex_hull=True, pga_threshold=10)
  ```
