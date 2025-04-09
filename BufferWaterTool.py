import arcpy
# Set environments
arcpy.env.workspace = "D:\Liberty\G_650\PyScripting\PythonGP\PythonGP\Data\SanJuan.gdb"
# Create list of feature classes to Buffer
bufferList = [arcpy.GetParameterAsText(0),arcpy.GetParameterAsText(1)]
# Initialize a new Python list of feature classes to be Unioned together
unionList = []
for fc in bufferList:
    # Buffer each feature class and dissolve any overlapping polygons
    arcpy.Buffer_analysis(fc, fc + "Buffer", "1000 meters", "", "", "ALL")
    # Add each buffer feature class to a list of feature classes to Union
    unionList.append(fc + "Buffer")
# Union the buffered feature classes
arcpy.Union_analysis(unionList, arcpy.GetParameterAsText(2))
