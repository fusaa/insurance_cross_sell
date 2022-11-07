import requests
# load dataset
df_test = x_validation
df_test['response'] = y_validation

df_test = df_test.sample(10)

#converting df to json

data = json.dumps( df_test.to_dict(orient = 'records'))


 #API call
url = 'http://0.0.0.0:5000/predict'
#url = 'https:// ... heroku...'
header = {'Content-type': 'application/json'}

r = requests.post( url, data=data, headers=header)
print('Status code {}'.format(r.status_code))

d1 = pd.DataFrame(r.json(), columns = r.json()[0].keys() )
d1.sort_values('score', ascending = False).head()
