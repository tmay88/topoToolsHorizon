import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = 'v20230131 WELL LOCATION SURVEYS'
        self.alias = 'v20230131 LOCATION SURVEYS'
        self.tools = [WELL_LOC_PLAN, WELL_PATH_PLAN]

class WELL_LOC_PLAN(object):
    def __init__(self):
        self.label = 'WELL_LOC_PLAN v20230131'
        self.description = 'Populates attribute constants for WELL_LOC_PLAN v20230131'
        self.canRunInBackground = False

    def getParameterInfo(self):
        in_features = arcpy.Parameter(
            displayName="Input Feature Class",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        return [in_features]

    def execute(self, parameters, messages):
        in_table = parameters[0].valueAsText
        field_dict1 = {
            "OXY_SRN_STATUS": "'VALIDATION'",
            "OXY_SURV_TYP": "'WEL'",
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
            "CLASS": "'UNKNOWN'",
            "TYPE": "'Horizontal'",
            "DESCRIPTION": "'NEW-WELL'",
            "PLANNING_STATUS": "'PLATTED'",
            "GCRS_EPSG_CODE": "4267",
            "GCRS_NM": "'GCS_NAD27'",
            "GRADE_ELEV": "0"
        }

        for field_name in field_dict1:
            arcpy.management.CalculateField(in_table, field_name, field_dict1[field_name], "PYTHON")

class WELL_PATH_PLAN(object):
    def __init__(self):
        self.label = 'WELL_PATH_PLAN v20230131'
        self.description = 'Populates attribute constants for WELL_PATH_PLAN v20230131'
        self.canRunInBackground = False

    def getParameterInfo(self):
        in_features = arcpy.Parameter(
            displayName="Input Feature Class",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        return [in_features]

    def execute(self, parameters, messages):
        in_table = parameters[0].valueAsText
        field_dict2 = {
            "OXY_SRN_STATUS": "'VALIDATION'",
            "OXY_SURV_TYP": "'WEL'",
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
            "CLASS": "'WELL_DRILL_PATH'",
        }

        for field_name in field_dict2:
            arcpy.management.CalculateField(in_table, field_name, field_dict2[field_name], "PYTHON")