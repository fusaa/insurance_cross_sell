# Health Insurance Class
import pickle
import pandas as pd
# from sklearn import linear_model as lm

class HealthInsurance:
    def __init__(self):
        self.home_path = './'
        self.annual_premium_scaler = pickle.load(open(self.home_path + 'annual_premium_scaler.pkl', 'rb'))
        self.age_scaler = pickle.load(open(self.home_path + 'age_scaler.pkl', 'rb'))
        self.vintage_scaler = pickle.load(open(self.home_path + 'vintage_scaler.pkl', 'rb'))
        self.target_encode_gender_scaler = pickle.load(open(self.home_path + 'target_encode_gender.pkl', 'rb'))
        self.target_encode_region_code_scaler = pickle.load(open(self.home_path + 'target_encode_region.pkl', 'rb'))
        self.fe_policy_sales_channel_scaler = pickle.load(open(self.home_path + 'fe_policy_sales_channel.pkl', 'rb'))

    def data_cleaning(self, df1):
        # Column rename
        # columns_names = [ ... ]
        #
        # 5.48m
        # df1.columns = cols_names

        return df1

    def feature_engineering(self, df_clean):
        # Vehicle Damage map label
        map_key = {'Yes': 1, 'No': 0}
        df_clean.loc[:, 'vehicle_damage'] = df_clean['vehicle_damage'].map(map_key)

        # One Hot Encoding Vehicle
        # df_clean = pd.get_dummies(df_clean, prefix='vehicle_age', columns=['vehicle_age'])

        return df_clean

    def data_preparation(self, df_clean):
        # Standardization

        df_clean['annual_premium'] = self.annual_premium_scaler.transform(df_clean[['annual_premium']].values)

        # rescaling
        df_clean['age'] = self.age_scaler.transform(df_clean[['age']].values)
        df_clean['vintage'] = self.vintage_scaler.transform(df_clean[['vintage']].values)

        # Doing Gender one hot
        df_clean.loc[:, 'gender'] = df_clean['gender'].map(self.target_encode_gender_scaler)

        # Target Encoding Region
        df_clean.loc[:, 'region_code'] = df_clean['region_code'].map(self.target_encode_region_code_scaler)
        # pickle.dump(t_enc_region, open('./target_encode_region.pkl', 'wb'))

        # One Hot Encoding Vehicle
        df_clean = pd.get_dummies(df_clean, prefix='vehicle_age', columns=['vehicle_age'])

        # use pandas to do transform, not saving it

        # Frequency Encoding Policy Channel
        # group by var and count # of examples.

        df_clean.loc[:, 'policy_sales_channel'] = df_clean['policy_sales_channel'].map(
            self.fe_policy_sales_channel_scaler)

        # Vehicle Damage map label
        #         map_key = {'Yes':1,'No':0}
        #         df_clean.loc[:,'vehicle_damage'] = df_clean['vehicle_damage'].map(map_key)
        # use pandas to do transform, not saving it

        cols_selected = ['vintage', 'annual_premium', 'age', 'region_code',
                         'vehicle_damage', 'previously_insured', 'policy_sales_channel']

        return df_clean[cols_selected]

    def get_prediction(self, model, original_data, test_data):
        # prediction
        pred = model.predict_proba(test_data)

        # join prediction into original data
        original_data['prediction'] = pred[:,1].tolist()

        return original_data.to_json(orient='records', date_format='iso')

