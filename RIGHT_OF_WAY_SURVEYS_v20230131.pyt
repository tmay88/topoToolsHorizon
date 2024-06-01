import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = 'RIGHT OF WAY SURVEYS v20230131'
        self.alias = 'RIGHT OF WAY SURVEYS v20230131'
        self.tools = [ROW_POINT, ROW_EDGES, ROW_ELECTRIC, ROW_FLOWLINE, ROW_MULTIUSE, ROW_PIPELINE, ROW_ROAD, ROW_FACILITY, ROW_PAD, ROW_FIBERLINE]

class ROW_POINT(object):
    def __init__(self):
        self.label = 'ROW_POINT v20230131'
        self.description = 'Populates attribute constants for ROW_POINT v20230131'
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
            "OXY_SURV_TYP": "'ROW'",
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
            "PLANNING_STATUS": "'PLATTED'"
        }

        for field_name in field_dict1:
            arcpy.management.CalculateField(in_table, field_name, field_dict1[field_name], "PYTHON")

class ROW_EDGES(object):
    def __init__(self):
        self.label = 'ROW_EDGES v20230131'
        self.description = 'Populates attribute constants for ROW_EDGES v20230131'
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
            "OXY_SURV_TYP": "'ROW'",
            "TYPE": "'ROW'",
            "PLANNING_STATUS": "'PLATTED'"
        }

        for field_name in field_dict2:
            arcpy.management.CalculateField(in_table, field_name, field_dict2[field_name], "PYTHON")

class ROW_ELECTRIC(object):
    def __init__(self):
        self.label = 'ROW_ELECTRICAL v20230131'
        self.description = 'Populates attribute constants for ROW_ELECTRICAL v20230131'
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
        field_dict3 = {
            "OXY_SRN_STATUS": "'VALIDATION'",
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
            "CLASS": "'ELECTRIC LINE'",
            "OXY_SURV_TYP": "'ROW'",
            "TYPE": "'EASEMENT'",
            "PLANNING_STATUS": "'PLATTED'"
        }

        for field_name in field_dict3:
            arcpy.management.CalculateField(in_table, field_name, field_dict3[field_name], "PYTHON")

class ROW_FLOWLINE(object):
    def __init__(self):
        self.label = 'ROW_FLOWLINE v20230131'
        self.description = 'Populates attribute constants for ROW_FLOWLINE v20230131'
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
        field_dict4 = {
            "OXY_SRN_STATUS": "'VALIDATION'",
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
            "CLASS": "'Flowline'",
            "OXY_SURV_TYP": "'ROW'",
            "TYPE": "'EASEMENT'",
            "PLANNING_STATUS": "'PLATTED'",
            "CMDTY": "'OTHER'",
            "LOC_DESC": "'OTHER'",
            "MATERIAL": "'UNKNOWN'",
            "PRESSURE_PSI": "'0'",
            "OUTSIDE_DIAM": "'UNKNOWN'",
            "NML_DIAM": "'UNKNOWN'",
            "NML_WAL_THICKNS": "'UNKNOWN'",
            "ROW_OFFSET_1": "15",
            "ROW_OFFSET_2": "15",
        }

        for field_name in field_dict4:
            arcpy.management.CalculateField(in_table, field_name, field_dict4[field_name], "PYTHON")

class ROW_MULTIUSE(object):
    def __init__(self):
        self.label = 'ROW_MULTIUSE v20230131'
        self.description = 'Populates attribute constants for ROW_MULTIUSE v20230131'
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
        field_dict5 = {
            "OXY_SRN_STATUS": "'VALIDATION'",
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
            "CLASS": "'MULTIUSE'",
            "OXY_SURV_TYP": "'ROW'",
            "TYPE": "'EASEMENT'",
            "PLANNING_STATUS": "'PLATTED'",
            "ROW_OFFSET_1": "15",
            "ROW_OFFSET_2": "15",
        }

        for field_name in field_dict5:
            arcpy.management.CalculateField(in_table, field_name, field_dict5[field_name], "PYTHON")

class ROW_PIPELINE(object):
    def __init__(self):
        self.label = 'ROW_PIPELINE v20230131'
        self.description = 'Populates attribute constants for ROW_PIPELINE v20230131'
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
        field_dict6 = {
            "OXY_SRN_STATUS": "'VALIDATION'",
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
            "CLASS": "'PIPELINE'",
            "OXY_SURV_TYP": "'ROW'",
            "TYPE": "'EASEMENT'",
            "PLANNING_STATUS": "'PLATTED'",
            "CMDTY": "'OTHER'",
            "LOC_DESC": "'OTHER'",
            "MATERIAL": "'UNKNOWN'",
            "PRESSURE_PSI": "'0'",
            "OUTSIDE_DIAM": "'UNKNOWN'",
            "NML_DIAM": "'UNKNOWN'",
            "NML_WAL_THICKNS": "'UNKNOWN'",
            "ROW_OFFSET_1": "15",
            "ROW_OFFSET_2": "15"
        }

        for field_name in field_dict6:
            arcpy.management.CalculateField(in_table, field_name, field_dict6[field_name], "PYTHON")

class ROW_ROAD(object):
    def __init__(self):
        self.label = 'ROW_ROAD v20230131'
        self.description = 'Populates attribute constants for ROW_ROAD v20230131'
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
        field_dict7 = {
            "OXY_SRN_STATUS": "'VALIDATION'",
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
            "CLASS": "'ROAD'",
            "OXY_SURV_TYP": "'ROW'",
            "TYPE": "'EASEMENT'",
            "PLANNING_STATUS": "'PLATTED'",
            "INSTALLATION": "'SURFACE'",
            "ROW_OFFSET_1": "15",
            "ROW_OFFSET_2": "15"
        }

        for field_name in field_dict7:
            arcpy.management.CalculateField(in_table, field_name, field_dict7[field_name], "PYTHON")

class ROW_FACILITY(object):
    def __init__(self):
        self.label = 'ROW_FACILITY v20230131'
        self.description = 'Populates attribute constants for ROW_FACILITY v20230131'
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
        field_dict8 = {
            "OXY_SRN_STATUS": "'VALIDATION'",
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
            "CLASS": "'FACILITY'",
            "OXY_SURV_TYP": "'ROW'",
            "TYPE": "'EASEMENT'",
            "PLANNING_STATUS": "'PLATTED'",
            "INSTALLATION": "'SURFACE'",
            "ROW_OFFSET": "0",
        }

        for field_name in field_dict8:
            arcpy.management.CalculateField(in_table, field_name, field_dict8[field_name], "PYTHON")

class ROW_PAD(object):
    def __init__(self):
        self.label = 'ROW_PAD v20230131'
        self.description = 'Populates attribute constants for ROW_PAD v20230131'
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
        field_dict9 = {
            "OXY_SRN_STATUS": "'VALIDATION'",
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
            "CLASS": "'PAD'",
            "OXY_SURV_TYP": "'ROW'",
            "TYPE": "'EASEMENT'",
            "PLANNING_STATUS": "'PLATTED'",
            "INSTALLATION": "'SURFACE'",
            "ROW_OFFSET": "0",
        }

        for field_name in field_dict9:
            arcpy.management.CalculateField(in_table, field_name, field_dict9[field_name], "PYTHON")

class ROW_FIBERLINE(object):
    def __init__(self):
        self.label = 'ROW_FIBERLINE v20230131'
        self.description = 'Populates attribute constants for ROW_FIBERLINE v20230131'
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
        field_dict10 = {
            "OXY_SRN_STATUS": "'VALIDATION'",
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
            "CLASS": "'FIBERLINE'",
            "OXY_SURV_TYP": "'ROW'",
            "TYPE": "'EASEMENT'",
            "PLANNING_STATUS": "'PLATTED'",
            "MATERIAL": "'FIBER_OPTIC'",
            "ROW_OFFSET_1": "15",
            "ROW_OFFSET_2": "15"
        }

        for field_name in field_dict10:
            arcpy.management.CalculateField(in_table, field_name, field_dict10[field_name], "PYTHON")