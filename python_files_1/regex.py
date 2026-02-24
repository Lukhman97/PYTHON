# import re

# ip="world hello"

# regex=r"hello"


# op=re.match(regex,ip)
# print(op)


# ip="world hello world hello world hello"

# regex=r"hello"
# op=re.search(regex,ip)
# print(op)



# ip="world hello world hello world hello"

# regex=r"hello"
# op=re.findall(regex,ip)
# print(op)



# regex="c.t"
# op=re.match(regex,"c1lcat")
# print(op)


# regex="c.t"
# op=re.search(regex,"c1lcat")
# print(op)

# ip="put"
# regex=r"p.t"
# if len(ip)>=3:
#     op=re.search(regex,ip)
#     print(op)
#     print("it is valid")
# else:
#     print("invalid")


# regex1="^icici"
# op=re.match(regex1,"icicia20")
# if (op):
#     print("valid")
# else:
#     print("invalid")


# regex1="gmail.com$"
# op=re.search(regex1,"lukhman786@2gmail.com")
# if (op):
#     print("valid")
# else:
#     print("invalid")

# regax1=r"\d"
# op=re.search(regax1,"hello123")
# if (op):
#     print("valid")
# else:
#     print("invalid")


# regax1=r"\w"
# op=re.search(regax1,"hello123")
# if (op):
#     print("valid")
# else:
#     print("invalid")

# regax1=r"\s"
# op=re.search(regax1,"hello123 world")
# if (op):
#     print("valid")
# else:
#     print("invalid")



# regax1=r"[abc]"
# op=re.search(regax1,"a")
# if (op):
#     print("valid")
# else:
#     print("invalid")


# regax1=r"[aeiou]"
# op=re.search(regax1,"e")
# if (op):
#     print("valid")
# else:
#     print("invalid")

# regax1=r"[a-z]"
# op=re.search(regax1,"1z")
# if (op):
#     print("valid")
# else:
#     print("invalid")

# regax1=r"[^aeiou]"
# op=re.search(regax1,"uoieat")
# if (op):
#     print("valid")
# else:
#     print("invalid")


# regax1=r"\w{5,}"
# op=re.search(regax1,"helloo")
# if (op):
#     print("valid")
# else:
#     print("invalid")


# regax1=r"\w{5,10}$"
# op=re.search(regax1,"hellohelloaahha")
# if (op):
#     print("valid")
# else:
#     print("invalid")


# regex1=r"^[A-Z]{5}\d{4}[A-Z]{1}$"
# op=re.search(regex1,"RMXAD3456a")
# if (op):
#     print("valid")
# else:
#     print("invalid")




# import re
# regex1=r"^[A-Z]{1}[a-z]{6}[1-9]{1}"
# ip="Lukhman7"
# op=re.search(regex1,ip)
# if (op):
#     print("valid")
# else:
#     print("invalid")


# regex1=r"^[A-Z]{5}\d{4}[A-Z]{1}$"
# op=re.search(regex1,"RMXAD3456a")
# if (op):
#     print("valid")
# else:
#     print("invalid")


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
from IPython.display import Image
from wordcloud import WordCloud, STOPWORDS
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
#Default theme
import seaborn as sns
sns.set_theme(context='notebook',
style='whitegrid',
palette='seismic',
font='Lucida Calligraphy',
font_scale=1.5,
rc=None)
import matplotlib
matplotlib.rcParams['figure.figsize'] = [8, 8]
matplotlib.rcParams.update({'font.size': 15})
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('precision',4)
companies = pd.read_csv("../input/companies-profit/1000_Companies.csv")
companies.head(2)
print(f'\033[96m')
print(companies.shape)
print(companies.size)
print(f'\033[95m')
companies.info()
companies.isnull().sum()
companies.describe()
companies['State'].value_counts()
text = " ".join(Company for Company in companies["State"])
#font = "Quicksand-Bold.ttf"
word_cloud = WordCloud(width = 1600,
height = 800,
colormap = 'jet',
background_color = "white").generate(text)
plt.figure(figsize = (30, 6))
plt.imshow(word_cloud, interpolation = "gaussian")
plt.axis("off")
plt.show()
plt.subplots(figsize=(20,8))
p = sns.barplot(x=companies["State"],y=companies["Profit"],palette="Set1",
saturation=2, edgecolor = "yellow", linewidth = 2.5,)
p.axes.set_title("\n State\n", fontsize=35)
plt.ylabel("Profit" , fontsize = 25)
plt.xlabel("\nState" , fontsize = 25)
# plt.yscale("log")
plt.xticks(rotation = 90)
for container in p.containers:
p.bar_label(container,label_type = "center",padding = 8,size = 25,color =
"black",rotation = 0,
bbox={"boxstyle": "round", "pad": 0.6, "facecolor": "pink", "edgecolor":
"black", "alpha": 1})
sns.despine(left=True, bottom=True)
plt.show()
plt.subplots(figsize=(20,8))
p = sns.barplot(x=companies["State"],y=companies["R&D Spend"],palette="Set1",
saturation=2, edgecolor = "yellow", linewidth = 2.5,)
p.axes.set_title("\n State\n", fontsize=35)
plt.ylabel("R&D Spend" , fontsize = 25)
plt.xlabel("\nState" , fontsize = 25)
# plt.yscale("log")
plt.xticks(rotation = 90)
for container in p.containers:
p.bar_label(container,label_type = "center",padding = 8,size = 25,color =
"black",rotation = 0,
bbox={"boxstyle": "round", "pad": 0.6, "facecolor": "pink", "edgecolor":
"black", "alpha": 1})
sns.despine(left=True, bottom=True)
plt.show()
sns.displot(data=companies, x="Marketing Spend", kde=True, bins = 100,color =
"red", facecolor = "#3F7F7F",height = 5, aspect = 3.5);
companies.plot(kind='kde', subplots=True, layout=(2,2), sharex=False, figsize=
(16,8))
plt.show()
plt.figure(figsize=(8,6))
sns.heatmap(companies.corr(),annot=True,cmap='Blues');
# Correlation Matrix
companies_correlation = companies.corr()
companies_correlation['Profit'].sort_values(ascending=False)
import category_encoders as ce
encoder = ce.OrdinalEncoder(['State'])
companies_encoded = encoder.fit_transform(companies)
companies_encoded.head(2)
X = companies_encoded.drop(["Profit"],axis=1)
y = companies_encoded['Profit']
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test =
train_test_split(X,y,test_size=0.3,random_state=21)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score,r2_score
model_LinearRegression = LinearRegression()
model_LinearRegression.fit(X_train, y_train)
# Finally, predict on test data
pred_test_LinearRegression = model_LinearRegression.predict(X_test)
r2_test_LinearRegression = r2_score(y_test,
pred_test_LinearRegression).round(4)
mse_test_LinearRegression = mean_squared_error(y_test,
pred_test_LinearRegression).round(4)
rmse_test_LinearRegression = np.sqrt(mean_squared_error(y_test,
pred_test_LinearRegression)).round(4)
mae_test_LinearRegression = mean_absolute_error(y_test,
pred_test_LinearRegression).round(4)
print(f'\033[94m')
print('R2 Score : ', r2_test_LinearRegression)
print(f'\033[92m')
print('MSE : ', mse_test_LinearRegression)
print('RMSE : ', rmse_test_LinearRegression)
print('MAE : ', mae_test_LinearRegression)
from sklearn.linear_model import Lasso
model_lasso = Lasso(alpha = 0.8)
model_lasso.fit(X_train, y_train)
# Finally, predict on test data
pred_test_lasso = model_lasso.predict(X_test)
r2_test_lasso = r2_score(y_test, pred_test_lasso).round(4)
mse_test_lasso = mean_squared_error(y_test, pred_test_lasso).round(4)
rmse_test_lasso = np.sqrt(mean_squared_error(y_test,
pred_test_lasso)).round(4)
mae_test_lasso = mean_absolute_error(y_test, pred_test_lasso).round(4)
print(f'\033[94m')
print('R2 Score : ', r2_test_lasso)
print(f'\033[92m')
print('MSE : ', mse_test_lasso)
print('RMSE : ', rmse_test_lasso)
print('MAE : ', mae_test_lasso)
from sklearn.linear_model import Ridge
model_Ridge = Ridge()
model_Ridge.fit(X_train, y_train)
# Finally, predict on test data
pred_test_Ridge = model_Ridge.predict(X_test)
r2_test_Ridge = r2_score(y_test, pred_test_Ridge).round(4)
mse_test_Ridge = mean_squared_error(y_test, pred_test_Ridge).round(4)
rmse_test_Ridge = np.sqrt(mean_squared_error(y_test,
pred_test_Ridge)).round(4)
mae_test_Ridge = mean_absolute_error(y_test, pred_test_Ridge).round(4)
print(f'\033[94m')
print('R2 Score : ', r2_test_Ridge)
print(f'\033[92m')
print('MSE : ', mse_test_Ridge)
print('RMSE : ', rmse_test_Ridge)
print('MAE : ', mae_test_Ridge)
from xgboost import XGBRegressor
model_xgb = XGBRegressor(random_state=42)
model_xgb.fit(X_train, y_train)
# Finally, predict on test data
pred_test_xgb = model_xgb.predict(X_test)
r2_test_xgb = r2_score(y_test, pred_test_xgb).round(4)
mse_test_xgb = mean_squared_error(y_test, pred_test_xgb).round(4)
rmse_test_xgb = np.sqrt(mean_squared_error(y_test, pred_test_xgb)).round(4)
mae_test_xgb = mean_absolute_error(y_test, pred_test_xgb).round(4)
print(f'\033[94m')
print('R2 Score : ', r2_test_xgb)
print(f'\033[92m')
print('MSE : ', mse_test_xgb)
print('RMSE : ', rmse_test_xgb)
print('MAE : ', mae_test_xgb)
from sklearn.linear_model import ElasticNet
model_ElasticNet = ElasticNet()
model_ElasticNet.fit(X_train, y_train)
# Finally, predict on test data
pred_test_ElasticNet = model_ElasticNet.predict(X_test)
r2_test_ElasticNet = r2_score(y_test, pred_test_ElasticNet).round(4)
mse_test_ElasticNet = mean_squared_error(y_test,
pred_test_ElasticNet).round(4)
rmse_test_ElasticNet = np.sqrt(mean_squared_error(y_test,
pred_test_ElasticNet)).round(4)
mae_test_ElasticNet = mean_absolute_error(y_test,
pred_test_ElasticNet).round(4)
print(f'\033[94m')
print('R2 Score : ', r2_test_ElasticNet)
print(f'\033[92m')
print('MSE : ', mse_test_ElasticNet)
print('RMSE : ', rmse_test_ElasticNet)
print('MAE : ', mae_test_ElasticNet)
from sklearn.ensemble import RandomForestRegressor
model_RandomForestRegressor = RandomForestRegressor()
model_RandomForestRegressor.fit(X_train, y_train)
# Finally, predict on test data
pred_test_RandomForestRegressor = model_RandomForestRegressor.predict(X_test)
r2_test_RandomForestRegressor = r2_score(y_test,
pred_test_RandomForestRegressor).round(4)
mse_test_RandomForestRegressor = mean_squared_error(y_test,
pred_test_RandomForestRegressor).round(4)
rmse_test_RandomForestRegressor = np.sqrt(mean_squared_error(y_test,
pred_test_RandomForestRegressor)).round(4)
mae_test_RandomForestRegressor = mean_absolute_error(y_test,
pred_test_RandomForestRegressor).round(4)
print(f'\033[94m')
print('R2 Score : ', r2_test_RandomForestRegressor)
print(f'\033[92m')
print('MSE : ', mse_test_RandomForestRegressor)
print('RMSE : ', rmse_test_RandomForestRegressor)
print('MAE : ', mae_test_RandomForestRegressor)
from sklearn.neighbors import KNeighborsRegressor
model_KNeighborsRegressor = KNeighborsRegressor()
model_KNeighborsRegressor.fit(X_train, y_train)
# Finally, predict on test data
pred_test_KNeighborsRegressor = model_KNeighborsRegressor.predict(X_test)
r2_test_KNeighborsRegressor = r2_score(y_test,
pred_test_KNeighborsRegressor).round(4)
mse_test_KNeighborsRegressor = mean_squared_error(y_test,
pred_test_KNeighborsRegressor).round(4)
rmse_test_KNeighborsRegressor = np.sqrt(mean_squared_error(y_test,
pred_test_KNeighborsRegressor)).round(4)
mae_test_KNeighborsRegressor = mean_absolute_error(y_test,
pred_test_KNeighborsRegressor).round(4)
print(f'\033[94m')
print('R2 Score : ', r2_test_KNeighborsRegressor)
print(f'\033[92m')
print('MSE : ', mse_test_KNeighborsRegressor)
print('RMSE : ', rmse_test_KNeighborsRegressor)
print('MAE : ', mae_test_KNeighborsRegressor)
from sklearn.ensemble import BaggingRegressor
model_BaggingRegressor = BaggingRegressor()
model_BaggingRegressor.fit(X_train, y_train)
# Finally, predict on test data
pred_test_BaggingRegressor = model_BaggingRegressor.predict(X_test)
r2_test_BaggingRegressor = r2_score(y_test,
pred_test_BaggingRegressor).round(4)
mse_test_BaggingRegressor = mean_squared_error(y_test,
pred_test_BaggingRegressor).round(4)
rmse_test_BaggingRegressor = np.sqrt(mean_squared_error(y_test,
pred_test_BaggingRegressor)).round(4)
mae_test_BaggingRegressor = mean_absolute_error(y_test,
pred_test_BaggingRegressor).round(4)
print(f'\033[94m')
print('R2 Score : ', r2_test_BaggingRegressor)
print(f'\033[92m')
print('MSE : ', mse_test_BaggingRegressor)
print('RMSE : ', rmse_test_BaggingRegressor)
print('MAE : ', mae_test_BaggingRegressor)
from sklearn.ensemble import HistGradientBoostingRegressor
model_HistGradientBoostingRegressor = HistGradientBoostingRegressor()
model_HistGradientBoostingRegressor.fit(X_train, y_train)
# Finally, predict on test data
pred_test_HistGradientBoostingRegressor =
model_HistGradientBoostingRegressor.predict(X_test)
r2_test_HistGradientBoostingRegressor = r2_score(y_test,
pred_test_HistGradientBoostingRegressor).round(4)
mse_test_HistGradientBoostingRegressor = mean_squared_error(y_test,
pred_test_HistGradientBoostingRegressor).round(4)
rmse_test_HistGradientBoostingRegressor = np.sqrt(mean_squared_error(y_test,
pred_test_HistGradientBoostingRegressor)).round(4)
mae_test_HistGradientBoostingRegressor = mean_absolute_error(y_test,
pred_test_HistGradientBoostingRegressor).round(4)
print(f'\033[94m')
print('R2 Score : ', r2_test_HistGradientBoostingRegressor)
print(f'\033[92m')
print('MSE : ', mse_test_HistGradientBoostingRegressor)
print('RMSE : ', rmse_test_HistGradientBoostingRegressor)
print('MAE : ', mae_test_HistGradientBoostingRegressor)
from sklearn.ensemble import ExtraTreesRegressor
model_ExtraTreesRegressor = ExtraTreesRegressor()
model_ExtraTreesRegressor.fit(X_train, y_train)
# Finally, predict on test data
pred_test_ExtraTreesRegressor = model_ExtraTreesRegressor.predict(X_test)
r2_test_ExtraTreesRegressor = r2_score(y_test,
pred_test_ExtraTreesRegressor).round(4)
mse_test_ExtraTreesRegressor = mean_squared_error(y_test,
pred_test_ExtraTreesRegressor).round(4)
rmse_test_ExtraTreesRegressor = np.sqrt(mean_squared_error(y_test,
pred_test_ExtraTreesRegressor)).round(4)
mae_test_ExtraTreesRegressor= mean_absolute_error(y_test,
pred_test_ExtraTreesRegressor).round(4)
print(f'\033[94m')
print('R2 Score : ', r2_test_ExtraTreesRegressor)
print(f'\033[92m')
print('MSE : ', mse_test_ExtraTreesRegressor)
print('RMSE : ', rmse_test_ExtraTreesRegressor)
print('MAE : ', mae_test_ExtraTreesRegressor)
from sklearn.ensemble import AdaBoostRegressor
model_AdaBoostRegressor = AdaBoostRegressor()
model_AdaBoostRegressor.fit(X_train, y_train)
# Finally, predict on test data
pred_test_AdaBoostRegressor = model_AdaBoostRegressor.predict(X_test)
r2_test_AdaBoostRegressor = r2_score(y_test,
pred_test_AdaBoostRegressor).round(4)
mse_test_AdaBoostRegressor = mean_squared_error(y_test,
pred_test_AdaBoostRegressor).round(4)
rmse_test_AdaBoostRegressor = np.sqrt(mean_squared_error(y_test,
pred_test_AdaBoostRegressor)).round(4)
mae_test_AdaBoostRegressor= mean_absolute_error(y_test,
pred_test_AdaBoostRegressor).round(4)
print(f'\033[94m')
print('R2 Score : ', r2_test_AdaBoostRegressor)
print(f'\033[92m')
print('MSE : ', mse_test_AdaBoostRegressor)
print('RMSE : ', rmse_test_AdaBoostRegressor)
print('MAE : ', mae_test_AdaBoostRegressor)
from sklearn.neural_network import MLPRegressor
model_MLPRegressor = MLPRegressor()
model_MLPRegressor.fit(X_train, y_train)
# Finally, predict on test data
pred_test_MLPRegressor = model_MLPRegressor.predict(X_test)
r2_test_MLPRegressor = r2_score(y_test, pred_test_MLPRegressor).round(4)
mse_test_MLPRegressor = mean_squared_error(y_test,
pred_test_MLPRegressor).round(4)
rmse_test_MLPRegressor = np.sqrt(mean_squared_error(y_test,
pred_test_MLPRegressor)).round(4)
mae_test_MLPRegressor= mean_absolute_error(y_test,
pred_test_MLPRegressor).round(4)
print(f'\033[94m')
print('R2 Score : ', r2_test_MLPRegressor)
print(f'\033[92m')
print('MSE : ', mse_test_MLPRegressor)
print('RMSE : ', rmse_test_MLPRegressor)
print('MAE : ', mae_test_MLPRegressor)
from sklearn.linear_model import HuberRegressor
model_HuberRegressor = HuberRegressor()
model_HuberRegressor.fit(X_train, y_train)
# Finally, predict on test data
pred_test_HuberRegressor = model_HuberRegressor.predict(X_test)
r2_test_HuberRegressor = r2_score(y_test, pred_test_HuberRegressor).round(4)
mse_test_HuberRegressor = mean_squared_error(y_test,
pred_test_HuberRegressor).round(4)
rmse_test_HuberRegressor = np.sqrt(mean_squared_error(y_test,
pred_test_HuberRegressor)).round(4)
mae_test_HuberRegressor= mean_absolute_error(y_test,
pred_test_HuberRegressor).round(4)
print(f'\033[94m')
print('R2 Score : ', r2_test_HuberRegressor)
print(f'\033[92m')
print('MSE : ', mse_test_HuberRegressor)
print('RMSE : ', rmse_test_HuberRegressor)
print('MAE : ', mae_test_HuberRegressor)
from sklearn.linear_model import BayesianRidge
model_BayesianRidge = BayesianRidge()
model_BayesianRidge.fit(X_train, y_train)
# Finally, predict on test data
pred_test_BayesianRidge = model_BayesianRidge.predict(X_test)
r2_test_BayesianRidge = r2_score(y_test, pred_test_BayesianRidge).round(4)
mse_test_BayesianRidge = mean_squared_error(y_test,
pred_test_BayesianRidge).round(4)
rmse_test_BayesianRidge = np.sqrt(mean_squared_error(y_test,
pred_test_BayesianRidge)).round(4)
mae_test_BayesianRidge= mean_absolute_error(y_test,
pred_test_BayesianRidge).round(4)
print(f'\033[94m')
print('R2 Score : ', r2_test_BayesianRidge)
print(f'\033[92m')
print('MSE : ', mse_test_BayesianRidge)
print('RMSE : ', rmse_test_BayesianRidge)
print('MAE : ', mae_test_BayesianRidge)
models = pd.DataFrame({
'Model': [
'LinearRegression', 'LassoRegression', 'RidgeRegression',
'ElasticNetRegressor', 'XGBRegressor', 'RandomForestRegressor',
'KNeighborsRegressor', 'BaggingRegressor',
'HistGradientBoostingRegressor', 'ExtraTreesRegressor', 'HuberRegressor'
'AdaBoostRegressor', ' MLPRegressor', 'HuberRegressor',
'BayesianRidge'
],
'R2 Score': [
r2_test_LinearRegression,r2_test_lasso, r2_test_Ridge,
r2_test_ElasticNet, r2_test_xgb, r2_test_RandomForestRegressor,
r2_test_KNeighborsRegressor,
r2_test_BaggingRegressor,r2_test_HistGradientBoostingRegressor,
r2_test_ExtraTreesRegressor,
r2_test_AdaBoostRegressor, r2_test_MLPRegressor,
r2_test_HuberRegressor, r2_test_BayesianRidge
],
'MSE': [
mse_test_LinearRegression,mse_test_lasso, mse_test_Ridge,
mse_test_ElasticNet, mse_test_xgb, mse_test_RandomForestRegressor,
mse_test_KNeighborsRegressor, mse_test_BaggingRegressor,
mse_test_HistGradientBoostingRegressor, mse_test_ExtraTreesRegressor,
mse_test_AdaBoostRegressor, mse_test_MLPRegressor,
mse_test_HuberRegressor, mse_test_BayesianRidge
],
'RMSE': [
rmse_test_LinearRegression,rmse_test_lasso, rmse_test_Ridge,
rmse_test_ElasticNet, rmse_test_xgb, rmse_test_RandomForestRegressor,
rmse_test_KNeighborsRegressor, rmse_test_BaggingRegressor,
rmse_test_HistGradientBoostingRegressor, rmse_test_ExtraTreesRegressor,
rmse_test_AdaBoostRegressor, rmse_test_MLPRegressor,
rmse_test_HuberRegressor, rmse_test_BayesianRidge
],
'MAE': [
mae_test_LinearRegression,mae_test_lasso, mae_test_Ridge,
mae_test_ElasticNet, mae_test_xgb, mae_test_RandomForestRegressor,
mae_test_KNeighborsRegressor, mae_test_BaggingRegressor,
mae_test_HistGradientBoostingRegressor, mae_test_ExtraTreesRegressor,
mae_test_AdaBoostRegressor, mae_test_MLPRegressor,
mae_test_HuberRegressor, mae_test_BayesianRidge
]
})
pd.set_option('precision',2)
models.sort_values(by='R2 Score', ascending=False).style.background_gradient(
cmap='coolwarm').hide_index().set_properties({
'font-family': 'Lucida Calligraphy',
'color': 'LigntGreen',
'font-size': '15px'
})
p = plt.figure(figsize=(18,16))
p = sns.set_theme(style="white")
p= models=models.sort_values(by='R2 Score',ascending=False)[:20]
p = sns.barplot(y= 'Model', x= 'R2 Score', data= models)
for container in p.containers:
p.bar_label(container,label_type = 'center',padding = 2,size = 15,color =
"Red",rotation = 0,
bbox={"boxstyle": "round", "pad": 0.3, "facecolor": "yellow", "edgecolor":
"black", "alpha": 1})
plt.title('COMPARE THE MODEL')
plt.xlabel('R2 Score')
plt.ylabel('Model');
print(f'\033[94m')
prediction = model_xgb.predict(X_test)
print(prediction)
cross_checking = pd.DataFrame({'Actual' : y_test , 'Predicted' : prediction})
cross_checking.head()
cross_checking['Error'] = cross_checking['Actual'] -
cross_checking['Predicted']
cross_checking.head()
cross_checking_final = cross_checking[cross_checking['Error'] <= 20]
cross_checking_final.sample(25).style.background_gradient(
cmap='coolwarm').set_properties({
'font-family': 'Lucida Calligraphy',
'color': 'LigntGreen',
'font-size': '15px'
})
print(f'\033[93m')
prediction = model_KNeighborsRegressor.predict(X_test)
print(prediction)
cross_checking = pd.DataFrame({'Actual' : y_test , 'Predicted' : prediction})
cross_checking.head()
cross_checking['Error'] = cross_checking['Actual'] -
cross_checking['Predicted']
cross_checking.head()
cross_checking_final = cross_checking[cross_checking['Error'] <= 20]
cross_checking_final.sample(25).style.background_gradient(
cmap='coolwarm').set_properties({
'font-family': 'Lucida Calligraphy',
'color': 'LigntGreen',
'font-size': '15px'
})