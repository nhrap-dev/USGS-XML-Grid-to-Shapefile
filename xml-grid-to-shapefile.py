import geopandas as gpd
from shapely.geometry import Point

# define function


def xml_grid_to_shapefile(xml_grid, output_directory, convex_hull=False, pga_threshold=0):
    with open(xml_grid) as xml:
        lines = xml.read()
        split = lines.split('\n')
        spaced = [x.split(' ') for x in split]
        props = [x for x in spaced if x[0].startswith('<grid_field')]
        fields = []
        for prop in props:
            name = [x for x in prop if 'name' in x][0].split(
                '=')[1].replace('"', '').replace("'", '')
            unit = [x for x in prop if 'unit' in x][0].split(
                '=')[1].replace('"', '').replace("'", '')
            field = ' '.join([name, unit])
            fields.append(field)
        del fields[0]
        values = [list(map(float, x))
                  for x in spaced if not x[0].startswith('<') and x[0] != '']
        geoms = [Point(x[0], x[1]) for x in values]
        values = [x[2:] for x in values]
        gdf = gpd.GeoDataFrame(values, columns=fields, geometry=geoms)
        if pga_threshold > 0:
            pga_column = [x for x in gdf.columns if 'PGA' in x][0]
            gdf = gdf[gdf[pga_column] >= pga_threshold]
        if convex_hull:
            ch = gdf.unary_union.convex_hull
            gdf = gpd.GeoDataFrame(geometry=gpd.GeoSeries(ch))
        if '.shp' not in output_directory:
            if not output_directory.endswith('/'):
                output_directory = output_directory + '/'
            output_directory = output_directory + 'output_grid.shp'
        gdf.to_file(output_directory, driver='ESRI Shapefile')
        print('Success! Output saved at ' + output_directory)


def xml_grid_to_gdf(xml_grid, convex_hull=False, pga_threshold=0):
    with open(xml_grid) as xml:
        lines = xml.read()
        split = lines.split('\n')
        spaced = [x.split(' ') for x in split]
        props = [x for x in spaced if x[0].startswith('<grid_field')]
        fields = []
        for prop in props:
            name = [x for x in prop if 'name' in x][0].split(
                '=')[1].replace('"', '').replace("'", '')
            unit = [x for x in prop if 'unit' in x][0].split(
                '=')[1].replace('"', '').replace("'", '')
            field = ' '.join([name, unit])
            fields.append(field)
        del fields[0]
        values = [list(map(float, x))
                  for x in spaced if not x[0].startswith('<') and x[0] != '']
        geoms = [Point(x[0], x[1]) for x in values]
        values = [x[2:] for x in values]
        gdf = gpd.GeoDataFrame(values, columns=fields, geometry=geoms)
        if pga_threshold > 0:
            pga_column = [x for x in gdf.columns if 'PGA' in x][0]
            gdf = gdf[gdf[pga_column] >= pga_threshold]
        if convex_hull:
            ch = gdf.unary_union.convex_hull
            gdf = gpd.GeoDataFrame(geometry=gpd.GeoSeries(ch))
        return gdf


# specify the inputs
xml_grid = r'C:\projects\NEIC\TwoPAGER\EXAMPLE_GRID.xml'
output_directory = r'C:\projects\NEIC\TwoPAGER\EXAMPLE_SHAPEFILE.shp'

# run the function
gdf = xml_grid_to_shapefile(xml_grid, output_directory)
