PATH_ENCODER = '../../model_ml/one_hot_enconder.pkl'
PATH_SCALER = '../../model_ml/robust_escaler.pkl'
PATH_MODEL_ML = '../../model_ml/logistic_regresion.pkl'


#data information
numerical_columns = ['device_fraud_count','income','name_email_similarity','prev_address_months_count','current_address_months_count','customer_age','days_since_request','intended_balcon_amount','zip_count_4w','velocity_6h','velocity_24h','velocity_4w','bank_branch_count_8w','date_of_birth_distinct_emails_4w','credit_risk_score','bank_months_count','proposed_credit_limit','session_length_in_minutes','device_distinct_emails_8w','month']
categorical_columns = ['payment_type', 'employment_status', 'housing_status', 'source', 'device_os']
target_var = 'fraud_bool'
features_model = ['device_os_windows', 'housing_status_BA', 'month', 'credit_risk_score','customer_age', 'income', 'payment_type_AC',
                'employment_status_CC', 'date_of_birth_distinct_emails_4w', 'has_other_cards', 'email_is_free', 'employment_status_CA', 
                'device_os_linux', 'proposed_credit_limit','current_address_months_count', 'bank_months_count']