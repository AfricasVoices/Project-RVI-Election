from core_data_modules.cleaners import Codes, somali
from dateutil.parser import isoparse
from src.pipeline_configuration_spec import *


PIPELINE_CONFIGURATION = PipelineConfiguration(
    pipeline_name="SDC Rapid SMS survey S02",
    description="Impact Assessment, Minority Inclusion, and Service Delivery Evaluation on SDC Projects in Somalia",
    test_participant_uuids=[
        "avf-participant-uuid-368c7741-7034-474a-9a87-6ae32a51f5a0",
        "avf-participant-uuid-5ca68e07-3dba-484b-a29c-7a6c989036b7",
        "avf-participant-uuid-45d15c2d-623c-4f89-bd91-7518147bf1dc",
        "avf-participant-uuid-88ef05ba-4c56-41f8-a00c-29104abab73e",
        "avf-participant-uuid-d9745740-3da5-43cc-a9d1-37fccb75380b",
        "avf-participant-uuid-96ff0ba1-a7df-4715-84c5-9c90e9093eb4"
    ],
    engagement_database=EngagementDatabaseClientConfiguration(
        credentials_file_url="gs://avf-credentials/avf-engagement-databases-firebase-credentials-file.json",
        # Sync back to IMAQAL-2 for now because the current IMAQAL pool has duplicated CSV messages that need
        # understanding.
        # TODO: Overwrite the IMAQAL pool with the current IMAQAL-2 pool and change this ref to use that IMAQAL
        #       pool as soon as possible.
        database_path="engagement_databases/IMAQAL-2"
    ),
    uuid_table=UUIDTableClientConfiguration(
        credentials_file_url="gs://avf-credentials/avf-id-infrastructure-firebase-adminsdk-6xps8-b9173f2bfd.json",
        table_name="avf-global-urn-to-participant-uuid",
        uuid_prefix="avf-participant-uuid-"
    ),
    operations_dashboard=OperationsDashboardConfiguration(
        credentials_file_url="gs://avf-credentials/avf-dashboards-firebase-adminsdk-gvecb-ef772e79b6.json"
    ),
    rapid_pro_sources=[
        RapidProSource(
            rapid_pro=RapidProClientConfiguration(
                domain="textit.com",
                token_file_url="gs://avf-credentials/imaqal-text-it-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    FlowResultConfiguration("SOMREP_s02_sms_ad", "somrep_s02_feedback_mechanism", "somrep_s02_feedback_mechanism"),
                    FlowResultConfiguration("SOMREP_s02_sms_ad", "somrep_s02_reason_feedback", "somrep_s02_reason_feedback"),

                    FlowResultConfiguration("SOMREP_s02_sms_ad", "somrep_s02_gov_services", "somrep_s02_gov_services"),
                    FlowResultConfiguration("SOMREP_s02_sms_ad", "somrep_s02_reasons_gov_services", "somrep_s02_reasons_gov_services"),

                    FlowResultConfiguration("SOMREP_s02_sms_ad", "somrep_s02_inclusion", "somrep_s02_inclusion"),
                    FlowResultConfiguration("SOMREP_s02_sms_ad", "somrep_s02_reasons_inclusion", "somrep_s02_reasons_inclusion"),
                    
                    FlowResultConfiguration("SOMREP_s02_sms_ad", "somrep_s02_resilience_support", "somrep_s02_resilience_support"),
                    FlowResultConfiguration("SOMREP_s02_sms_ad", "somrep_s02_reason_resilience_support", "somrep_s02_reason_resilience_support"),

                    FlowResultConfiguration("CHASP_s02_sms_ad", "chasp_s02_complains_feedback", "chasp_s02_complains_feedback"),
                    FlowResultConfiguration("CHASP_s02_sms_ad", "chasp_s02_reasons_complains", "chasp_s02_reasons_complains"),

                    FlowResultConfiguration("CHASP_s02_sms_ad", "chasp_s02_gov_services", "chasp_s02_gov_services"),
                    FlowResultConfiguration("CHASP_s02_sms_ad", "chasp_s02_reasons_gov_services", "chasp_s02_reasons_gov_services"),

                    FlowResultConfiguration("CHASP_s02_sms_ad", "chasp_s02_inclusion", "chasp_s02_inclusion"),
                    FlowResultConfiguration("CHASP_s02_sms_ad", "chasp_s02_reasons_inclusion", "chasp_s02_reasons_inclusion"),

                    FlowResultConfiguration("CHASP_s02_sms_ad", "chasp_s02_support", "chasp_s02_support"),
                    FlowResultConfiguration("CHASP_s02_sms_ad", "chasp_s02_reasons_support", "chasp_s02_reasons_support"),

                    FlowResultConfiguration("SIRA_s02_sms_ad", "sira_s02_feedback_mechanism", "sira_s02_feedback_mechanism"),
                    FlowResultConfiguration("SIRA_s02_sms_ad", "sira_s02_reasons_feedback", "sira_s02_reasons_feedback"),

                    FlowResultConfiguration("SIRA_s02_sms_ad", "sira_s02_gov_services", "sira_s02_gov_services"),
                    FlowResultConfiguration("SIRA_s02_sms_ad", "sira_s02_reasons_gov_services", "sira_s02_reasons_gov_services"),

                    FlowResultConfiguration("SIRA_s02_sms_ad", "sira_s02_inclusion", "sira_s02_inclusion"),
                    FlowResultConfiguration("SIRA_s02_sms_ad", "sira_s02_reasons_inclusion", "sira_s02_reasons_inclusion"),

                    FlowResultConfiguration("SIRA_s02_sms_ad", "sira_s02_support", "sira_s02_support"),
                    FlowResultConfiguration("SIRA_s02_sms_ad", "sira_s02_reasons_support", "sira_s02_reasons_support"),

                    FlowResultConfiguration("R2P_s01_sms_ad", "r2p_s01_inclusion", "r2p_s01_inclusion"),
                    FlowResultConfiguration("R2P_s01_sms_ad", "r2p_s01_reasons_inclusion", "r2p_s01_reasons_inclusion"),

                    FlowResultConfiguration("R2P_s01_sms_ad", "r2p_s01_governance", "r2p_s01_governance"),
                    FlowResultConfiguration("R2P_s01_sms_ad", "r2p_s01_reasons_governance", "r2p_s01_reasons_governance"),

                    FlowResultConfiguration("R2P_s01_sms_ad", "r2p_s01_impact", "r2p_s01_impact"),
                    FlowResultConfiguration("R2P_s01_sms_ad", "r2p_s01_reasons_impact", "r2p_s01_reasons_impact"),

                    FlowResultConfiguration("R2P_s01_sms_ad", "r2p_s01_support", "r2p_s01_support"),
                    FlowResultConfiguration("R2P_s01_sms_ad", "r2p_s01_reasons_support", "r2p_s01_reasons_support"),

                    FlowResultConfiguration("sdc_survey_s02e01_activation", "rqa_s02e01", "sdc_survey_s02e01"),
                    FlowResultConfiguration("sdc_survey_s02e02_activation", "rqa_s02e02", "sdc_survey_s02e02"),
                    FlowResultConfiguration("sdc_survey_s02e03_activation", "rqa_s02e03", "sdc_survey_s02e03"),

                    FlowResultConfiguration("sdc_survey_s02e01_follow_up_activation", "rqa_s02e01_follow_up", "sdc_survey_s02e01_follow_up"),
                    FlowResultConfiguration("sdc_survey_s02e02_follow_up_activation", "rqa_s02e02_follow_up", "sdc_survey_s02e02_follow_up"),
                    FlowResultConfiguration("sdc_survey_s02e03_follow_up_activation", "rqa_s02e03_follow_up", "sdc_survey_s02e03_follow_up"),

                    FlowResultConfiguration("sdc_survey_s02_demog", "imaqal_pool_district", "location"),
                    FlowResultConfiguration("sdc_survey_s02_demog", "imaqal_pool_gender", "gender"),
                    FlowResultConfiguration("sdc_survey_s02_demog", "imaqal_pool_age", "age"),
                    FlowResultConfiguration("sdc_survey_s02_demog", "imaqal_pool_recently_displaced", "recently_displaced"),
                    FlowResultConfiguration("sdc_survey_s02_demog", "imaqal_pool_disability", "disability"),
                    FlowResultConfiguration("sdc_survey_s02_demog", "imaqal_pool_household_language", "household_language"),
                    FlowResultConfiguration("sdc_survey_s02_demog", "imaqal_pool_clan", "clan"),
                ]
            )
        )
    ],
    google_form_sources=[
        GoogleFormSource(
            # https://forms.gle/uHkHH17vYRgcYwgY8
            google_form_client=GoogleFormsClientConfiguration(
                credentials_file_url="gs://avf-credentials/pipeline-runner-service-acct-avf-data-core-64cc71459fe7.json"
            ),
            sync_config=GoogleFormToEngagementDBConfiguration(
                form_id="1htXX0AoaHVwPhWyu7lVTWITjf5SC0SNaja4wftyLf5I",
                question_configurations=[
                    # CHASP
                    QuestionConfiguration(engagement_db_dataset="chasp_s02_support", question_titles=["Using a scale of 0 to 5, with 5 indicating the highest level of satisfaction, how do you rate your satisfaction with the quality of health services provided by the project implemented by Save the Children in your community?"]),
                    QuestionConfiguration(engagement_db_dataset="chasp_s02_reasons_support", question_titles=["In order to improve, we would like to know the reason for your rating of level of satisfaction with Save the Children project."]),
                    QuestionConfiguration(engagement_db_dataset="chasp_s02_complains_feedback", question_titles=["Using a scale of 0 to 5, with 5 being the highest level of satisfaction, how satisfied are you with the complaints & feedback mechanism of the Save the Children project and the follow-up on feedback submitted?"]),
                    QuestionConfiguration(engagement_db_dataset="chasp_s02_reasons_complains", question_titles=["In order to improve, we would like to know the reason for your rating of complaints & feedback mechanism of Save the Children project."]),
                    QuestionConfiguration(engagement_db_dataset="chasp_s02_inclusion", question_titles=["On a scale of 0 to 5, with 5 being the highest, to what extent do you feel included and have participated in decision making processes regarding healthcare services in your community?"]),
                    QuestionConfiguration(engagement_db_dataset="chasp_s02_reasons_inclusion", question_titles=["In order to improve, we would like to know the reason for your rating of decision making processes in the healthcare services access by Save the Children."]),
                    QuestionConfiguration(engagement_db_dataset="chasp_s02_gov_services", question_titles=["Rate your satisfaction with government services in your community, in relation to healthcare services, on a scale of 0 to 5, with 5 indicating high satisfaction."]),
                    QuestionConfiguration(engagement_db_dataset="chasp_s02_reasons_gov_services", question_titles=["In order to improve, we would like to know the reason for your rating of government services."]),

                    # SOMREP
                    QuestionConfiguration(engagement_db_dataset="somrep_s02_resilience_support", question_titles=["Using a scale of 0 to 5, with 5 indicating the highest level of satisfaction, how do you rate your satisfaction with the quality of support provided by the SomRep  project implemented by OXFAM and COOPI in your community?"]),
                    QuestionConfiguration(engagement_db_dataset="somrep_s02_reason_resilience_support", question_titles=["In order to improve, we would like to know the reason for your rating on level of satisfaction with OXFAM and COOPI."]),
                    QuestionConfiguration(engagement_db_dataset="somrep_s02_feedback_mechanism", question_titles=["Using a scale of 0 to 5, with 5 being the highest level of satisfaction, how satisfied are you with the complaints & feedback mechanism of SOMREP implemented by OXFAM and COOPI and the follow-up on feedback submitted?"]),
                    QuestionConfiguration(engagement_db_dataset="somrep_s02_reason_feedback", question_titles=["In order to improve, we would like to know the reason for your rating on complaints & feedback mechanism of OXFAM and COOPI."]),
                    QuestionConfiguration(engagement_db_dataset="somrep_s02_inclusion", question_titles=["On a scale of 0 to 5, with 5 being the highest, to what extent do you feel included and have participated in decision making processes on resilience initiatives in your community?"]),
                    QuestionConfiguration(engagement_db_dataset="somrep_s02_reasons_inclusion", question_titles=["In order to improve, we would like to know the reason for your rating on decision making processes of initiatives for the SomReP."]),
                    QuestionConfiguration(engagement_db_dataset="somrep_s02_gov_services", question_titles=["Rate your satisfaction with government services, in regards to resilience, in your community on a scale of 0 to 5, with 5 indicating high satisfaction."]),
                    QuestionConfiguration(engagement_db_dataset="somrep_s02_reasons_gov_services", question_titles=["In order to improve, we would like to know the reason for your rating of government services (SomReP)."]),

                    # R2P
                    QuestionConfiguration(engagement_db_dataset="r2p_s01_support", question_titles=["Using a scale of 0 to 5, with 5 indicating the highest level of satisfaction, how do you rate the effectiveness of the peace dialogues and mediation efforts facilitated by the 'Road to Peace' project implemented by PDRC and Horn Centre in resolving conflicts in your community?"]),
                    QuestionConfiguration(engagement_db_dataset="r2p_s01_reasons_support", question_titles=["In order to improve, we would like to know the reason for your rating of level of satisfaction with PDRC and Horn Centre initiatives."]),
                    QuestionConfiguration(engagement_db_dataset="r2p_s01_inclusion", question_titles=["Using a scale of 0 to 5, with 5 being the highest, to what extent do you feel that you and your community were included in the peacebuilding and decision making processes initiated by the 'Road to Peace' project by PDRC and Horn Centre?"]),
                    QuestionConfiguration(engagement_db_dataset="r2p_s01_reasons_inclusion", question_titles=["In order to improve, we would like to know the reason for your rating of decision making processes of PDRC."]),
                    QuestionConfiguration(engagement_db_dataset="r2p_s01_impact", question_titles=["Using a scale of 0 to 5, with 5 being the highest, how do you rate the impact of the 'Road to Peace' project on improving relationships and trust between different clans or groups in your community?"]),
                    QuestionConfiguration(engagement_db_dataset="r2p_s01_reasons_impact", question_titles=["In order to improve, we would like to know the reason for your rating of the impact of R2P project."]),
                    QuestionConfiguration(engagement_db_dataset="r2p_s01_governance", question_titles=["Using a scale of 0 to 5, with 5 indicating high satisfaction, how satisfied are you with the support provided by the 'Road to Peace' project in strengthening local governance and rule of law in your community?"]),
                    QuestionConfiguration(engagement_db_dataset="r2p_s01_reasons_governance", question_titles=["In order to improve, we would like to know the reason for your rating of support provided by R2P."]),

                    QuestionConfiguration(engagement_db_dataset="location", question_titles=["Degmadee ayaad ku nooshahay?\nIn which district of Somalia do you currently live?"]),
                    QuestionConfiguration(engagement_db_dataset="gender", question_titles=["Mahadsanid. Ma waxaad tahay Rag mise Dumar? Fadlan kaga jawaab Rag ama Dumar.\nWhat is your gender?"]),
                    QuestionConfiguration(engagement_db_dataset="age", question_titles=["Da'daadu maxay tahay? Fadlan kaga jawaab tiro.\nHow old are you? Please answer with a number in years."]),
                    QuestionConfiguration(engagement_db_dataset="recently_displaced", question_titles=["Ma waxaad tahay qof soo barakacay dhawaan? Hadii haa ay tahay jawaabtadu, Maxa kusoo barakiciyay?\nAre you currently displaced? If so, what made you leave your home?"]),
                    QuestionConfiguration(engagement_db_dataset="disability", question_titles=["Wax naafo ah miyaad leedahay?\nDo you have a disability?"]),
                    QuestionConfiguration(engagement_db_dataset="household_language", question_titles=["Luuqaddee ayaad caadi ahaan gurigiinna dhexdiisa uga hadashaan?\nWhat language do you usually speak in your household?"])
                ]
            )
        ),
    ],
    coda_sync=CodaConfiguration(
        coda=CodaClientConfiguration(credentials_file_url="gs://avf-credentials/coda-production.json"),
        sync_config=CodaSyncConfiguration(
            dataset_configurations=[
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_Survey_s02e01",
                    engagement_db_dataset="sdc_survey_s02e01",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/sdc_survey_s02e01"),
                                                coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="sdc_survey_s02e01"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_Survey_s02e02",
                    engagement_db_dataset="sdc_survey_s02e02",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/sdc_survey_s02e02"),
                                                coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="sdc_survey_s02e02"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_Survey_s02e03",
                    engagement_db_dataset="sdc_survey_s02e03",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/sdc_survey_s02e03"),
                                                coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="sdc_survey_s02e03"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_Survey_s02e01_follow_up",
                    engagement_db_dataset="sdc_survey_s02e01_follow_up",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/sdc_survey_s02e01_follow_up"),
                                                coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="sdc_survey_s02e01_follow_up"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_Survey_s02e02_follow_up",
                    engagement_db_dataset="sdc_survey_s02e02_follow_up",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/sdc_survey_s02e02_follow_up"),
                                                coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="sdc_survey_s02e02_follow_up"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SDC_Survey_s02e03_follow_up",
                    engagement_db_dataset="sdc_survey_s02e03_follow_up",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/sdc_survey_s02e03_follow_up"),
                                                coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="sdc_survey_s02e03_follow_up"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="CHASP_S02_complains_feedback",
                    engagement_db_dataset="chasp_s02_complains_feedback",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_complains_feedback"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="chasp_s02_complains_feedback"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="CHASP_S02_reasons_complains",
                    engagement_db_dataset="chasp_s02_reasons_complains",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_reasons_complains"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="chasp_s02_reasons_complains"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="CHASP_S02_gov_services",
                    engagement_db_dataset="chasp_s02_gov_services",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_gov_services"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="chasp_s02_gov_services"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="CHASP_S02_reasons_gov_services",
                    engagement_db_dataset="chasp_s02_reasons_gov_services",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_reasons_gov_services"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="chasp_s02_reasons_gov_services"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="CHASP_S02_inclusion",
                    engagement_db_dataset="chasp_s02_inclusion",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_inclusion"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="chasp_s02_inclusion"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="CHASP_S02_reasons_inclusion",
                    engagement_db_dataset="chasp_s02_reasons_inclusion",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_reasons_inclusion"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="chasp_s02_reasons_inclusion"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="CHASP_S02_support",
                    engagement_db_dataset="chasp_s02_support",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_support"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="chasp_s02_support"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="CHASP_S02_reasons_support",
                    engagement_db_dataset="chasp_s02_reasons_support",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_reasons_support"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="chasp_s02_reasons_support"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SOMREP_S02_feedback_mechanism",
                    engagement_db_dataset="somrep_s02_feedback_mechanism",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_feedback_mechanism"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="somrep_s02_feedback_mechanism"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SOMREP_S02_reason_feedback",
                    engagement_db_dataset="somrep_s02_reason_feedback",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_reason_feedback"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="somrep_s02_reason_feedback"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SOMREP_S02_gov_services",
                    engagement_db_dataset="somrep_s02_gov_services",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_gov_services"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="somrep_s02_gov_services"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SOMREP_S02_reasons_gov_services",
                    engagement_db_dataset="somrep_s02_reasons_gov_services",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_reasons_gov_services"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="somrep_s02_reasons_gov_services"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SOMREP_S02_inclusion",
                    engagement_db_dataset="somrep_s02_inclusion",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_inclusion"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="somrep_s02_inclusion"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SOMREP_S02_reasons_inclusion",
                    engagement_db_dataset="somrep_s02_reasons_inclusion",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_reasons_inclusion"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="somrep_s02_reasons_inclusion"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SOMREP_S02_resilience_support",
                    engagement_db_dataset="somrep_s02_resilience_support",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_resilience_support"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="somrep_s02_resilience_support"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SOMREP_S02_reason_resilience_support",
                    engagement_db_dataset="somrep_s02_reason_resilience_support",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_reason_resilience_support"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="somrep_s02_reason_resilience_support"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SIRA_S02_feedback_mechanism",
                    engagement_db_dataset="sira_s02_feedback_mechanism",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_feedback_mechanism"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="sira_s02_feedback_mechanism"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SIRA_S02_reasons_feedback",
                    engagement_db_dataset="sira_s02_reasons_feedback",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_reasons_feedback"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="sira_s02_reasons_feedback"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SIRA_S02_gov_services",
                    engagement_db_dataset="sira_s02_gov_services",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_gov_services"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="sira_s02_gov_services"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SIRA_S02_reasons_gov_services",
                    engagement_db_dataset="sira_s02_reasons_gov_services",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_reasons_gov_services"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="sira_s02_reasons_gov_services"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SIRA_S02_inclusion",
                    engagement_db_dataset="sira_s02_inclusion",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_inclusion"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="sira_s02_inclusion"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SIRA_S02_reasons_inclusion",
                    engagement_db_dataset="sira_s02_reasons_inclusion",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_reasons_inclusion"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="sira_s02_reasons_inclusion"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SIRA_S02_support",
                    engagement_db_dataset="sira_s02_support",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_support"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="sira_s02_support"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="SIRA_S02_reasons_support",
                    engagement_db_dataset="sira_s02_reasons_support",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_reasons_support"), 
                        coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="sira_s02_reasons_support"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="R2P_S01_inclusion",
                    engagement_db_dataset="r2p_s01_inclusion",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_inclusion"), 
                                                coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="r2p_s01_inclusion"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="R2P_S01_reasons_inclusion",
                    engagement_db_dataset="r2p_s01_reasons_inclusion",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_reasons_inclusion"), 
                                                coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="r2p_s01_reasons_inclusion"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="R2P_S01_governance",
                    engagement_db_dataset="r2p_s01_governance",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_governance"), 
                                                coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="r2p_s01_governance"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="R2P_S01_reasons_governance",
                    engagement_db_dataset="r2p_s01_reasons_governance",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_reasons_governance"), 
                                                coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="r2p_s01_reasons_governance"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="R2P_S01_impact",
                    engagement_db_dataset="r2p_s01_impact",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_impact"), 
                                                coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="r2p_s01_impact"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="R2P_S01_reasons_impact",
                    engagement_db_dataset="r2p_s01_reasons_impact",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_reasons_impact"), 
                                                coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="r2p_s01_reasons_impact"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="R2P_S01_support",
                    engagement_db_dataset="r2p_s01_support",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_support"), 
                                                coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="r2p_s01_support"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="R2P_S01_reasons_support",
                    engagement_db_dataset="r2p_s01_reasons_support",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_reasons_support"), 
                                                coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="r2p_s01_reasons_support"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="IMAQAL_age",
                    engagement_db_dataset="age",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/age"),
                                                auto_coder=lambda text: str(
                                                    somali.DemographicCleaner.clean_age_within_range(text))
                                                ),
                    ],
                    ws_code_match_value="age",
                    dataset_users_file_url="gs://avf-project-datasets/2022/IMAQAL-POOL/coda_users.json"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="IMAQAL_gender",
                    engagement_db_dataset="gender",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/gender"),
                                                auto_coder=somali.DemographicCleaner.clean_gender)
                    ],
                    ws_code_match_value="gender",
                    dataset_users_file_url="gs://avf-project-datasets/2022/IMAQAL-POOL/coda_users.json"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="IMAQAL_household_language",
                    engagement_db_dataset="household_language",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/household_language"), 
                                                coda_code_schemes_count=2, auto_coder=None)
                    ],
                    ws_code_match_value="household_language",
                    dataset_users_file_url="gs://avf-project-datasets/2022/IMAQAL-POOL/coda_users.json"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="IMAQAL_location",
                    engagement_db_dataset="location",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/mogadishu_sub_district"),
                                                auto_coder=somali.DemographicCleaner.clean_mogadishu_sub_district),
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/somalia_district"), auto_coder=lambda text:
                        somali.DemographicCleaner.clean_somalia_district(text)
                        if somali.DemographicCleaner.clean_mogadishu_sub_district == Codes.NOT_CODED else Codes.NOT_CODED),
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/somalia_region"), auto_coder=None),
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/somalia_state"), auto_coder=None),
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/somalia_zone"), auto_coder=None),
                    ],
                    ws_code_match_value="location",
                    dataset_users_file_url="gs://avf-project-datasets/2022/IMAQAL-POOL/coda_users.json"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="IMAQAL_recently_displaced",
                    engagement_db_dataset="recently_displaced",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/recently_displaced"),
                                                auto_coder=somali.DemographicCleaner.clean_yes_no)
                    ],
                    ws_code_match_value="recently_displaced",
                    dataset_users_file_url="gs://avf-project-datasets/2022/IMAQAL-POOL/coda_users.json"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="IMAQAL_disability",
                    engagement_db_dataset="disability",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/disability"),
                                                auto_coder=somali.DemographicCleaner.clean_yes_no)
                    ],
                    ws_code_match_value="disability",
                    dataset_users_file_url="gs://avf-project-datasets/2022/IMAQAL-POOL/coda_users.json"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="IMAQAL_clan",
                    engagement_db_dataset="clan",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/clan"))
                    ],
                    ws_code_match_value="clan",
                    dataset_users_file_url="gs://avf-project-datasets/2022/IMAQAL-POOL/coda_users.json"
                ),
            ],
            ws_correct_dataset_code_scheme=load_code_scheme("ws_correct_dataset"),
            project_users_file_url="gs://avf-project-datasets/2023/SDC-Survey/coda_users.json",
        )
    ),
    archive_configuration=ArchiveConfiguration(
        archive_upload_bucket="gs://pipeline-execution-backup-archive",
        bucket_dir_path="2024/SDC-Survey-S02"
    ),
    analysis=AnalysisConfiguration(
        google_drive_upload=GoogleDriveUploadConfiguration(
            credentials_file_url="gs://avf-credentials/pipeline-runner-service-acct-avf-data-core-64cc71459fe7.json",
            drive_dir="sdc_survey_s02_analysis_outputs"
        ),
        dataset_configurations=[
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sdc_survey_s02e01"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sdc_survey_s02e01_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/sdc_survey_s02e01"),
                        analysis_dataset="sdc_survey_s02e01"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sdc_survey_s02e02"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sdc_survey_s02e02_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/sdc_survey_s02e02"),
                        analysis_dataset="sdc_survey_s02e02"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sdc_survey_s02e03"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sdc_survey_s02e03_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/sdc_survey_s02e03"),
                        analysis_dataset="sdc_survey_s02e03"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sdc_survey_s02e01_follow_up"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sdc_survey_s02e01_follow_up_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/sdc_survey_s02e01_follow_up"),
                        analysis_dataset="sdc_survey_s02e01_follow_up"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sdc_survey_s02e02_follow_up"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sdc_survey_s02e02_follow_up_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/sdc_survey_s02e02_follow_up"),
                        analysis_dataset="sdc_survey_s02e02_follow_up"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sdc_survey_s02e03_follow_up"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sdc_survey_s02e03_follow_up_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/sdc_survey_s02e03_follow_up"),
                        analysis_dataset="sdc_survey_s02e03_follow_up"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sira_s02_feedback_mechanism"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sira_s02_feedback_mechanism_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_feedback_mechanism"),
                        analysis_dataset="sira_s02_feedback_mechanism"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sira_s02_reasons_feedback"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sira_s02_reasons_feedback_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_reasons_feedback"),
                        analysis_dataset="sira_s02_reasons_feedback"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sira_s02_gov_services"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sira_s02_gov_services_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_gov_services"),
                        analysis_dataset="sira_s02_gov_services"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sira_s02_reasons_gov_services"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sira_s02_reasons_gov_services_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_reasons_gov_services"),
                        analysis_dataset="sira_s02_reasons_gov_services"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sira_s02_inclusion"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sira_s02_inclusion_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_inclusion"),
                        analysis_dataset="sira_s02_inclusion"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sira_s02_reasons_inclusion"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sira_s02_reasons_inclusion_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_reasons_inclusion"),
                        analysis_dataset="sira_s02_reasons_inclusion"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sira_s02_support"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sira_s02_support_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_support"),
                        analysis_dataset="sira_s02_support"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["sira_s02_reasons_support"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="sira_s02_reasons_support_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/sira_s02_reasons_support"),
                        analysis_dataset="sira_s02_reasons_support"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["somrep_s02_feedback_mechanism"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="somrep_s02_feedback_mechanism_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_feedback_mechanism"),
                        analysis_dataset="somrep_s02_feedback_mechanism"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["somrep_s02_reason_feedback"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="somrep_s02_reason_feedback_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_reason_feedback"),
                        analysis_dataset="somrep_s02_reason_feedback"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["somrep_s02_gov_services"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="somrep_s02_gov_services_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_gov_services"),
                        analysis_dataset="somrep_s02_gov_services"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["somrep_s02_reasons_gov_services"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="somrep_s02_reasons_gov_services_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_reasons_gov_services"),
                        analysis_dataset="somrep_s02_reasons_gov_services"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["somrep_s02_inclusion"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="somrep_s02_inclusion_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_inclusion"),
                        analysis_dataset="somrep_s02_inclusion"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["somrep_s02_reasons_inclusion"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="somrep_s02_reasons_inclusion_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_reasons_inclusion"),
                        analysis_dataset="somrep_s02_reasons_inclusion"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["somrep_s02_resilience_support"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="somrep_s02_resilience_support_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_resilience_support"),
                        analysis_dataset="somrep_s02_resilience_support"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["somrep_s02_reason_resilience_support"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="somrep_s02_reason_resilience_support_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/somrep_s02_reason_resilience_support"),
                        analysis_dataset="somrep_s02_reason_resilience_support"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["chasp_s02_complains_feedback"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="chasp_s02_complains_feedback_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_complains_feedback"),
                        analysis_dataset="chasp_s02_complains_feedback"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["chasp_s02_reasons_complains"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="chasp_s02_reasons_complains_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_reasons_complains"),
                        analysis_dataset="chasp_s02_reasons_complains"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["chasp_s02_gov_services"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="chasp_s02_gov_services_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_gov_services"),
                        analysis_dataset="chasp_s02_gov_services"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["chasp_s02_reasons_gov_services"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="chasp_s02_reasons_gov_services_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_reasons_gov_services"),
                        analysis_dataset="chasp_s02_reasons_gov_services"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["chasp_s02_inclusion"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="chasp_s02_inclusion_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_inclusion"),
                        analysis_dataset="chasp_s02_inclusion"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["chasp_s02_reasons_inclusion"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="chasp_s02_reasons_inclusion_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_reasons_inclusion"),
                        analysis_dataset="chasp_s02_reasons_inclusion"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["chasp_s02_support"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="chasp_s02_support_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_support"),
                        analysis_dataset="chasp_s02_support"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["chasp_s02_reasons_support"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="chasp_s02_reasons_support_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/chasp_s02_reasons_support"),
                        analysis_dataset="chasp_s02_reasons_support"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["r2p_s01_inclusion"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="r2p_s01_inclusion_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_inclusion"),
                        analysis_dataset="r2p_s01_inclusion"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["r2p_s01_reasons_inclusion"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="r2p_s01_reasons_inclusion_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_reasons_inclusion"),
                        analysis_dataset="r2p_s01_reasons_inclusion"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["r2p_s01_governance"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="r2p_s01_governance_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_governance"),
                        analysis_dataset="r2p_s01_governance"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["r2p_s01_reasons_governance"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="r2p_s01_reasons_governance_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_reasons_governance"),
                        analysis_dataset="r2p_s01_reasons_governance"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["r2p_s01_impact"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="r2p_s01_impact_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_impact"),
                        analysis_dataset="r2p_s01_impact"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["r2p_s01_reasons_impact"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="r2p_s01_reasons_impact_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_reasons_impact"),
                        analysis_dataset="r2p_s01_reasons_impact"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["r2p_s01_support"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="r2p_s01_support_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_support"),
                        analysis_dataset="r2p_s01_support"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["r2p_s01_reasons_support"],
                dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
                raw_dataset="r2p_s01_reasons_support_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("rqas/sdc_somalia/r2p_s01_reasons_support"),
                        analysis_dataset="r2p_s01_reasons_support"
                    )
                ]
            ),
            OperatorDatasetConfiguration(
                raw_dataset="operator_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/imaqal_operator"),
                        analysis_dataset="operator",
                        analysis_location=AnalysisLocations.SOMALIA_OPERATOR
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["age"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="age_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/age"),
                        analysis_dataset="age"
                    ),
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/age_category"),
                        analysis_dataset="age_category",
                        age_category_config=AgeCategoryConfiguration(
                            age_analysis_dataset="age",
                            categories={
                                (10, 14): "10 to 14",
                                (15, 17): "15 to 17",
                                (18, 35): "18 to 35",
                                (36, 54): "36 to 54",
                                (55, 99): "55 to 99"
                            }
                        )
                    ),
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["gender"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="gender_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/gender"),
                        analysis_dataset="gender"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["location"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="location_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/mogadishu_sub_district"),
                        analysis_dataset="mogadishu_sub_district",
                        analysis_location=AnalysisLocations.MOGADISHU_SUB_DISTRICT
                    ),
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/somalia_district"),
                        analysis_dataset="district",
                        analysis_location=AnalysisLocations.SOMALIA_DISTRICT
                    ),
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/somalia_region"),
                        analysis_dataset="region",
                        analysis_location=AnalysisLocations.SOMALIA_REGION
                    ),
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/somalia_state"),
                        analysis_dataset="state",
                        analysis_location=AnalysisLocations.SOMALIA_STATE
                    ),
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/somalia_zone"),
                        analysis_dataset="zone",
                        analysis_location=AnalysisLocations.SOMALIA_ZONE
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["recently_displaced"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="recently_displaced",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/recently_displaced"),
                        analysis_dataset="recently_displaced"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["disability"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="disability",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/disability"),
                        analysis_dataset="disability"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["household_language"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="household_language",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/household_language"),
                        analysis_dataset="household_language"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["clan"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="clan",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/clan"),
                        analysis_dataset="clan"
                    )
                ]
            ),
        ],
        ws_correct_dataset_code_scheme=load_code_scheme("ws_correct_dataset"),
        traffic_labels=[]
    )
)
