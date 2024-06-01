import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = 'TOPOGRAPHIC SURVEYS v20230131'
        self.alias = 'TOPOGRAPHIC SURVEYS v20230131'
        self.tools = [TOPO_ELECTRICAL, TOPO_FACILITY, TOPO_FIBERLINE, TOPO_FLOWLINE, TOPO_HAZARD_LN, TOPO_HAZARD_PY, TOPO_MULTIUSE, TOPO_PAD, TOPO_PIPELINE, TOPO_POI, TOPO_ROAD, TOPO_WELL_SHL]

class TOPO_ELECTRICAL(object):
    def __init__(self):
        self.label = 'TOPO_ELECTRICAL v20230131'
        self.description = 'Populates attribute constants for TOPO_ELECTRICAL v20230131'
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
            "OXY_SURV_TYP": "'TOP'",
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
            "CONSTR_STATUS": "'UNKNOWN'",
            "INSTALLATION": "'OTHER'"
        }

        for field_name in field_dict1:
            arcpy.management.CalculateField(in_table, field_name, field_dict1[field_name], "PYTHON")

class TOPO_FACILITY(object):
    def __init__(self):
        self.label = 'TOPO_FACILITY v20230131'
        self.description = 'Populates attribute constants for TOPO_FACILITY v20230131'
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
            "OXY_SURV_TYP": "'TOP'",
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
            "CONSTR_STATUS": "'UNKNOWN'",
            "INSTALLATION": "'OTHER'"
        }

        for field_name in field_dict2:
            arcpy.management.CalculateField(in_table, field_name, field_dict2[field_name], "PYTHON")

class TOPO_FIBERLINE(object):
    def __init__(self):
        self.label = 'TOPO_FIBERLINE v20230131'
        self.description = 'Populates attribute constants for TOPO_FIBERLINE v20230131'
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
            "OXY_SURV_TYP": "'TOP'",
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
            "CONSTR_STATUS": "'UNKNOWN'",
            "INSTALLATION": "'OTHER'"
        }

        for field_name in field_dict3:
            arcpy.management.CalculateField(in_table, field_name, field_dict3[field_name], "PYTHON")

class TOPO_FLOWLINE(object):
    def __init__(self):
        self.label = 'TOPO_FLOWLINE v20230131'
        self.description = 'Populates attribute constants for TOPO_FLOWLINE v20230131'
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
            "OXY_SURV_TYP": "'TOP'",
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
            "CONSTR_STATUS": "'UNKNOWN'",
            "INSTALLATION": "'OTHER'"
        }

        for field_name in field_dict4:
            arcpy.management.CalculateField(in_table, field_name, field_dict4[field_name], "PYTHON")

class TOPO_HAZARD_LN(object):
    def __init__(self):
        self.label = 'TOPO_HAZARD_LN v20230131'
        self.description = 'Populates attribute constants for TOPO_HAZARD_LN v20230131'
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
            "OXY_SURV_TYP": "'TOP'",
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
            "CLASS": "'HAZARD'",
            "CONSTR_STATUS": "'UNKNOWN'",
            "INSTALLATION": "'OTHER'"
        }

        for field_name in field_dict5:
            arcpy.management.CalculateField(in_table, field_name, field_dict5[field_name], "PYTHON")

class TOPO_HAZARD_PY(object):
    def __init__(self):
        self.label = 'TOPO_HAZARD_PY v20230131'
        self.description = 'Populates attribute constants for TOPO_HAZARD_PY v20230131'
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
            "OXY_SURV_TYP": "'TOP'",
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
            "CLASS": "'HAZARD'",
            "CONSTR_STATUS": "'UNKNOWN'",
            "INSTALLATION": "'OTHER'"
        }

        for field_name in field_dict6:
            arcpy.management.CalculateField(in_table, field_name, field_dict6[field_name], "PYTHON")

class TOPO_MULTIUSE(object):
    def __init__(self):
        self.label = 'TOPO_MULTIUSE v20230131'
        self.description = 'Populates attribute constants for TOPO_MULTIUSE v20230131'
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
            "OXY_SURV_TYP": "'TOP'",
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
            "CONSTR_STATUS": "'UNKNOWN'",
            "INSTALLATION": "'OTHER'"
        }

        for field_name in field_dict7:
            arcpy.management.CalculateField(in_table, field_name, field_dict7[field_name], "PYTHON")

class TOPO_PAD(object):
    def __init__(self):
        self.label = 'TOPO_PAD v20230131'
        self.description = 'Populates attribute constants for TOPO_PAD v20230131'
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
            "OXY_SURV_TYP": "'TOP'",
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
            "CONSTR_STATUS": "'UNKNOWN'",
            "INSTALLATION": "'OTHER'",
            "PAD_DESIGN": "'NA'"
        }

        for field_name in field_dict8:
            arcpy.management.CalculateField(in_table, field_name, field_dict8[field_name], "PYTHON")

class TOPO_PIPELINE(object):
    def __init__(self):
        self.label = 'TOPO_PIPELINE v20230131'
        self.description = 'Populates attribute constants for TOPO_PIPELINE v20230131'
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
            "OXY_SURV_TYP": "'TOP'",
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
            "CONSTR_STATUS": "'UNKNOWN'",
            "INSTALLATION": "'OTHER'",
            "LOC_DESC": "'OTHER'",
            "MATERIAL": "'UNKNOWN'",
            "OUTSIDE_DIAM": "'NA'",
            "NML_DIAM": "'NA'",
            "NML_WAL_THICKNS": "'NA'",
            "CONDITION": "'NA'",
            "AGE": "'NA'",
            "SOIL_TYP": "'NA'",
            "SITE_CONDITIONS": "'NA'",
            "PRESSURE_PSI": "'NA'"
        }

        for field_name in field_dict9:
            arcpy.management.CalculateField(in_table, field_name, field_dict9[field_name], "PYTHON")

class TOPO_POI(object):
    def __init__(self):
        self.label = 'TOPO_POI v20230131'
        self.description = 'Populates attribute constants for TOPO_POI v20230131'
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
            "OXY_SURV_TYP": "'TOP'",
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
            "CONSTR_STATUS": "'UNKNOWN'",
            "INSTALLATION": "'OTHER'"
        }

        for field_name in field_dict10:
            arcpy.management.CalculateField(in_table, field_name, field_dict10[field_name], "PYTHON")

class TOPO_ROAD(object):
    def __init__(self):
        self.label = 'TOPO_ROAD v20230131'
        self.description = 'Populates attribute constants for TOPO_ROAD v20230131'
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
        field_dict11 = {
            "OXY_SRN_STATUS": "'VALIDATION'",
            "OXY_SURV_TYP": "'TOP'",
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
            "CONSTR_STATUS": "'UNKNOWN'",
            "INSTALLATION": "'OTHER'"
        }

        for field_name in field_dict11:
            arcpy.management.CalculateField(in_table, field_name, field_dict11[field_name], "PYTHON")

class TOPO_WELL_SHL(object):
    def __init__(self):
        self.label = 'TOPO_WELL_SHL v20230131'
        self.description = 'Populates attribute constants for TOPO_WELL_SHL v20230131'
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
        field_dict12 = {
            "OXY_SRN_STATUS": "'VALIDATION'",
            "OXY_SURV_TYP": "'TOP'",
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
            "CONSTR_STATUS": "'UNKNOWN'",
            "INSTALLATION": "'OTHER'"
        }

        for field_name in field_dict12:
            arcpy.management.CalculateField(in_table, field_name, field_dict12[field_name], "PYTHON")