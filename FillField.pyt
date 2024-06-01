import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = "Fill Field"
        self.alias = "Fill Filed"
        self.tools = [FillFieldTool]


class FillFieldTool(object):
    def __init__(self):
        self.label = "Fill Field"
        self.description = "Fills a selected field in the attribute table with a user-specified value"
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Define the parameter for the layer
        layer = arcpy.Parameter(
            displayName="Input Layer",
            name="layer",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        # Define the parameter for the field
        field = arcpy.Parameter(
            displayName="Field",
            name="field",
            datatype="Field",
            parameterType="Required",
            direction="Input")

        # Set the 'Obtained from' property of the field parameter to the 'Input Layer' parameter
        field.parameterDependencies = [layer.name]

        # Define the parameter for the value
        value = arcpy.Parameter(
            displayName="Value",
            name="value",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        params = [layer, field, value]

        # Set the list of fields for the 'Field' parameter
        try:
            if layer.value:
                params[1].filter.list = [f.name for f in arcpy.ListFields(layer.value)]
        except:
            pass

        return params

    def execute(self, parameters, messages):
        layer = parameters[0].valueAsText
        field = parameters[1].valueAsText
        value = parameters[2].valueAsText

        with arcpy.da.UpdateCursor(layer, [field]) as cursor:
            for row in cursor:
                row[0] = value
                cursor.updateRow(row)

        messages.addMessage("Field '{}' in layer '{}' has been filled with value '{}'.".format(field, layer, value))

