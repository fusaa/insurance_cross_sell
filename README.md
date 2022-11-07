# Introduction

An insurance company specialised in health coverage surveyed its customers about their interest in buying a new automobile insurance product that will start selling soon. They have questioned 380,000 people about their interest in the product. Customers' responses were saved in a database along with other features.

So then 127,000 new customers did not respond to the survey, and the company wishes to rank them, in terms of the likelihood of buying the news product, for receiving contact from the sales team. However, the sales team can't reach every single customer. It has been provisioned only 20 thousand phone calls. Given the circumstances, it is necessary to prioritise who will receive calls.

# Project Objective

Generate a list of the customers most likely to acquire the new product, so resources are used more efficiently (to rank customers). Metric to measure performance of the model Recall @K.

# Dataset

Dataset is from kaggle and original page can be found [here](https://www.kaggle.com/code/gabrielecarleo/health-insurance-using-logistic-regression).

id: Unique ID for the customer  
gender: Gender of the customer  
age: Customer age  
driving_license: 0 - Customer does not have, 1 - Customer already has DL  
region_code: Unique code for the region of the customer  
previously_insured: 1 - Customer already has Vehicle Insurance, 0 - Customer doesn't have Vehicle Insurance  
vehicle_age: Age of the Vehicle  
vehicle_damage: 1 - Customer got his/her vehicle damaged in the past, 0 - Customer didn't get his/her vehicle damaged in the past  
annual_premium: The amount customer needs to pay as premium in the year  
policy_sales_channel: Code for the channel of outreaching to the customer  
vintage: Number of Days, Customer has been associated with the company  
response: 1 - Customer is interested, 0 - Customer is not interested  

# Approach

Deliver:
- Model that ranks customer interest in the new product
- Model performance
- % of customers that can be reached with the specific model and effort

Tasks
- Cumulative Gain curve,
- Lift Curve,
- Recall at K

Interesting Data Insights:


- Sales Channel 43 and 123 have outstanding performance in percentage of positive feedbacks. In absolute values, sales channel 26 certainly shows something is going on there, followed by channels 154,156,157 and 163  - could investigate why.
![image](https://user-images.githubusercontent.com/66756007/196834242-bb2bcf91-6367-4360-ae35-1849c315416b.png)

- Some regions account for way more positives than others.
![image](https://user-images.githubusercontent.com/66756007/196834655-e69bb1c2-0547-4226-acbd-4041c31ad427.png)


# Feature Selection

Extra Trees Classifier was used for feature selection, hence the result:

![image](https://user-images.githubusercontent.com/66756007/196955362-9fcf1358-f2a1-4d03-8143-ce8111c5dbe0.png)


Vintage, annual_premium, age, region_code, vehicle_damage, policy_sales_channel and previously_insured have been selected to be part of the model, the other variables were considered of minor relevance and would just add unecessary dimensionality to the model.


# K-neighbors

Cumulative Gain Curve has been generated, with this model, it would be possible to achieve around 44% of interested customers by calling only the first 20%.
![image](https://user-images.githubusercontent.com/66756007/196956917-98937b24-1c46-420c-bafb-4fdc68bfc538.png)

# Logistic Regression

With this model we were able to rank customers in a way that it is possible to achieve roughly 100% of interested customers in acquiring an insurance by contacting only 50% of the customer list.
![image](https://user-images.githubusercontent.com/66756007/196957010-14745207-53c8-4bd5-bbdd-3afb110b1f24.png)

# Insights

![image](https://user-images.githubusercontent.com/66756007/200289391-083e13d1-2f5a-4ceb-8fb5-2c61179bce1b.png)

- Males are more interested
- People with driving licenses more likely to buy the new product
- The older the vehicle the more the interest.
- Damage in the vehicle in the past makes people want to do the car insurance.

![image](https://user-images.githubusercontent.com/66756007/200289485-fa0b832d-f20a-40f4-8cd6-b6dbf9a9abf8.png)

- Most interested age group for the product is between 40 and 50 years old.

![image](https://user-images.githubusercontent.com/66756007/200289545-f1088afe-4765-4bab-b6fb-92097df3b794.png)

- Regions 4,19, 23, 28, 38 and 51 are more likely to accept the product.

![image](https://user-images.githubusercontent.com/66756007/200289620-6566bdc0-3e08-4f31-b6e6-219c94bd95e6.png)

- Sales Channel 43 and 123 have a 100% rate of positives. While region 26 has a lot of positives.

![image](https://user-images.githubusercontent.com/66756007/200289681-ad01894a-220f-41d5-b9ce-5ddaaeea0bbc.png)

- Customers who are previously insured tend to refrain from taking the product.

## The amount of relevant customers hit when contacting 20.000 customers
![image](https://user-images.githubusercontent.com/66756007/200289854-119f2529-eebb-4858-8e83-96540eb8cd7d.png)

## Reaching out to 40.000 people what percentage will of interested people can be contacted?
![image](https://user-images.githubusercontent.com/66756007/200289948-adcd3a15-7dc4-4728-8702-335591262295.png)

## In order to reach 80% of interested customers on the chosen model how many people need to be contacted?
![image](https://user-images.githubusercontent.com/66756007/200290031-8da836f4-8428-4aa8-bbba-ecca111e32fd.png)

# Deploy

API was created and deployed to HEROKU - check API CODE [here](https://github.com/fusaa/insurance_cross_sell/tree/main/cross-sell-insurance-api). In addition, a Google Spreadsheet has been made, which is available to download from [this repository](https://github.com/fusaa/insurance_cross_sell/tree/main)(as .xlsx format - needs to be imported into Google Spreadsheets). The script for the Google Spreadsheet can be found [here](https://github.com/fusaa/insurance_cross_sell/blob/main/code_google.gs).

This way of deployment with an easy-to-use spreadsheet service will allow effortless management for the team. Observe that a button has been created: "Get Scores > Get Predictions" using Google Script on the spreadsheet. Code is also available in the repository. Users can update this list on the fly with new leads, and with a single click, they can get the customers' scores for prioritizing which ones to call.

![deploy](https://user-images.githubusercontent.com/66756007/200315857-cff3cb1b-4def-489e-b7c6-a832abca735e.gif)

