import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = 'v20230131 SECTION SURVEYS'
        self.alias = 'v20230131 SECTION SURVEYS'
        self.tools = [SECTION_CORNER, SECTION_AREA]

class SECTION_CORNER(object):
    def __init__(self):
        self.label = 'SECTION_CORNER v20230131'
        self.description = 'Populates attribute constants for SECTION_CORNER v20230131'
        self.canRunInBackground = False

    def getParameterInfo(self):
        in_features = arcpy.Parameter(
            displayName="Input Feature Class",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")
        
        parameters = [in_features]

        return parameters

    def execute(self, parameters, messages):
        in_table = parameters[0].valueAsText
        field_dict1 = {
            "OXY_SRN_STATUS": "'Validation'",
            "SURV_CO": "'HORIZON SURVEY INC.'",
            "SURV_NM": "'BRYON CAREY'",
            "SURV_TEL": "'281-855-6200'",
            "SURV_EMAIL": "'BRYON@HORIZONSURVEY.COM'",
            "SURV_RPLS": "'6661'",
            "LAND_STATE": "'TX'",
            "LAND_PLSS": "'NA'",
            "LAND_GOVT": "'NA'",
            "LAND_PRIVATE": "'NA'",
            "LAND_MER": "'NA'",
            "LAND_TWP_DIR": "'NA'",
            "LAND_RNG_DIR": "'NA'",
            "LAND_ALIQUOT": "'NA'",
            "LAND_FRAC_LOT": "'NA'",
            "GMTC_GCRS_EPSG_CODE": "6318",
            "GMTC_VCRS_EPSG_CODE": "6360",
            "GMTC_GEOID": "'GEOID18'",
            "GMTC_SURV_METH": "'GNSS'",
            "GMTC_SURV_FIX": "'NA'",
            "CLASS": "'CORNER'",
            "TYPE": "'ARTIFICIAL'",
            "SOURCE": "'CALCULATED'"
        }


        for field_name in field_dict1:
            arcpy.management.CalculateField(in_table, field_name, field_dict1[field_name], "PYTHON")

class SECTION_AREA(object):
    def __init__(self):
        self.label = 'SECTION_AREA v20230131'
        self.description = 'Populates attribute constants for SECTION_AREA v20230131'
        self.canRunInBackground = False
    
    def getParameterInfo(self):
        in_features = arcpy.Parameter(
            displayName="Input Feature Class",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")
        
        parameters = [in_features]

        return parameters

    def execute(self, parameters, messages):
        in_table = parameters[0].valueAsText
        field_dict2 = {
            "OXY_SRN_STATUS": "'Validation'",
            "SURV_CO": "'HORIZON SURVEY INC.'",
            "SURV_NM": "'BRYON CAREY'",
            "SURV_TEL": "'281-855-6200'",
            "SURV_EMAIL": "'BRYON@HORIZONSURVEY.COM'",
            "SURV_RPLS": "'6661'",
            "LAND_STATE": "'TX'",
            "LAND_PLSS": "'NA'",
            "LAND_GOVT": "'NA'",
            "LAND_PRIVATE": "'NA'",
            "LAND_MER": "'NA'",
            "LAND_TWP_DIR": "'NA'",
            "LAND_RNG_DIR": "'NA'",
            "LAND_ALIQUOT": "'NA'",
            "LAND_FRAC_LOT": "'NA'",
            "GMTC_GCRS_EPSG_CODE": "6318",
            "GMTC_VCRS_EPSG_CODE": "6360",
            "GMTC_GEOID": "'GEOID18'",
            "GMTC_SURV_METH": "'GNSS'",
            "GMTC_SURV_FIX": "'NA'",
            "CLASS": "'Corner'",
            "TYPE": "'Artificial'",
        }


        for field_name in field_dict2:
            arcpy.management.CalculateField(in_table, field_name, field_dict2[field_name], "PYTHON")

        messages.addMessage("Attribute Constants fill complete.")
