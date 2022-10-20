# Introduction

An insurance company specialised in health coverage surveyed its customers about their interest in buying a new automobile insurance product that will start selling soon. They have questioned 380,000 people about their interest in the product. Customers' responses were saved in a database along with other features.

So then 127,000 new customers did not respond to the survey, and the company wishes to rank them, in terms of the likelihood of buying the news product, for receiving contact from the sales team. However, the sales team can't reach every single customer. It has been provisioned only 20 thousand phone calls. Given the circumstances, it is necessary to prioritise who will receive calls.

# Project Objective

Generate a list of the customers most likely to acquire the new product, so resources are used more efficiently (to rank customers).

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
- Precision at K
- Recall at K

Interesting Data Insights:


- Sales Channel 43 and 123 have outstanding performance in percentage of positive feedbacks. In absolute values, sales channel 26 certainly shows something is going on there, followed by channels 154,156,157 and 163  - could investigate why.
![image](https://user-images.githubusercontent.com/66756007/196834242-bb2bcf91-6367-4360-ae35-1849c315416b.png)

- Some regions account for way more positives than others.
![image](https://user-images.githubusercontent.com/66756007/196834655-e69bb1c2-0547-4226-acbd-4041c31ad427.png)


# Feature Selection

Tree Classifier was used for feature selection, the importance order 


