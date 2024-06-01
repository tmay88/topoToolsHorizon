import arcpy
import datetime

class Toolbox(object):
    def __init__(self):
        self.label = "Delete All Field Values"
        self.alias = "delete_fields"
        self.tools = [DeleteFieldValues]

class DeleteFieldValues(object):
    def __init__(self):
        self.label = "Delete All Field Values"
        self.description = "Deletes all values from all fields in a feature class."
        self.canRunInBackground = False

    def getParameterInfo(self):
        fc_param = arcpy.Parameter(
            displayName="Input Feature Class",
            name="fc",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        return [fc_param]

    def execute(self, parameters, messages):
        fc = parameters[0].valueAsText

        fields = arcpy.ListFields(fc)
        with arcpy.da.UpdateCursor(fc, [field.name for field in fields]) as cursor:
            for row in cursor:
                for i, value in enumerate(row):
                    field = fields[i]
                    if field.type == "Date":
                        row[i] = datetime.datetime(1776, 7, 4)
                    elif field.type in ["SmallInteger", "Integer", "Single", "Double"]:
                        row[i] = 0
                    elif field.isNullable:
                        row[i] = None
                    else:
                        row[i] = ""

                cursor.updateRow(row)

        messages.addMessage("All field values have been deleted, Nulled or set to 0.")
