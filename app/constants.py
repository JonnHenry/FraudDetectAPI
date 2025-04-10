PATH_ENCODER = '../../model_ml/one_hot_enconder.pkl'
PATH_SCALER = '../../model_ml/robust_escaler.pkl'
PATH_MODEL_ML = '../../model_ml/xgb.pkl'


#data information
numerical_columns = ['device_fraud_count','income','name_email_similarity','prev_address_months_count','current_address_months_count','customer_age','days_since_request','intended_balcon_amount','zip_count_4w','velocity_6h','velocity_24h','velocity_4w','bank_branch_count_8w','date_of_birth_distinct_emails_4w','credit_risk_score','bank_months_count','proposed_credit_limit','session_length_in_minutes','device_distinct_emails_8w','month']
categorical_columns = ['payment_type', 'employment_status', 'housing_status', 'source', 'device_os']
target_var = 'fraud_bool'
features_model = ['payment_type_AC', 'proposed_credit_limit', 'customer_age',
       'housing_status_BC', 'date_of_birth_distinct_emails_4w',
       'name_email_similarity', 'credit_risk_score', 'email_is_free',
       'device_os_linux', 'zip_count_4w', 'device_os_windows',
       'has_other_cards', 'device_os_other', 'income', 'employment_status_CA',
       'bank_months_count', 'housing_status_BE', 'housing_status_BA',
       'bank_branch_count_8w', 'keep_alive_session', 'housing_status_BB',
       'current_address_months_count', 'phone_home_valid']