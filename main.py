import streamlit
import pandas

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

###
# streamlit.set_page_config(layout="wide")
streamlit.title("Deteksi Dini Status Risiko Diabetes")
streamlit.write("Posbindu Masjid Al Amin Mejing Kidul")
###

## Title
streamlit.write("Mohon isi data sesuai dengan petunjuk yang disediakan.")
##

### BUILD MODEL WITH "SIX (6)" INDEPENDENT VARIABLE BASED ON mRMR METHOD
## Read CSV & Define Feature
df = pandas.read_csv('https://raw.githubusercontent.com/danisnurman/psbnd2/main/diabetes_binary_5050split_health_indicators_BRFSS2015.csv')
# streamlit.dataframe(df, use_container_width=True)
#

## Feature Cols
mrmr_features = ['Diabetes_binary', 'Age', 'GenHlth', 'HighBP', 'HighChol', 'BMI', 'DiffWalk']
df = df[mrmr_features]
##

## Data Discretization & Transformation
# for index in range(df.shape[0]):
#     if df.loc[index,'BMI'] < 18.5:
#         df.loc[index,'BMI'] = 1
#     elif (df.loc[index,'BMI'] >= 18.5) & (df.loc[index,'BMI'] <= 24.9):
#         df.loc[index,'BMI'] = 2
#     elif (df.loc[index,'BMI'] >= 25.0) & (df.loc[index,'BMI'] <= 29.9):
#         df.loc[index,'BMI'] = 3
#     elif (df.loc[index,'BMI'] >= 30.0) & (df.loc[index,'BMI'] <= 100.0):
#         df.loc[index,'BMI'] = 4
#     else:
#         df.loc[index,'BMI'] = 1000

df['Diabetes_binary'] = df['Diabetes_binary'].astype('int64')
df['HighBP'] = df['HighBP'].astype('int64')
df['HighChol'] = df['HighChol'].astype('int64')
df['BMI'] = df['BMI'].astype('int64')
df['GenHlth'] = df['GenHlth'].astype('int64')
df['DiffWalk'] = df['DiffWalk'].astype('int64')
df['Age'] = df['Age'].astype('int64')

## Split the data
X = df.drop(columns='Diabetes_binary')
y = df.Diabetes_binary

## Predictions
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

## Classifier
clf = DecisionTreeClassifier()

## Perform training
clf = clf.fit(X_train, y_train)

## Predict result from dataset
y_pred = clf.predict(X_test)

## Calculate the accuracy score
acc_score = round((accuracy_score(y_test, y_pred)*100),2)
streamlit.write("")
streamlit.write("Model Accuracy : ", acc_score, "%")
streamlit.write("")

## Concatenate actual data & predicted data
# dfConcat = X_test.copy()
# dfConcat['y_testdata'] = y_test
# dfConcat.reset_index(inplace=True)
# dfConcat['y_predict'] = y_pred
# streamlit.write(dfConcat)
##

### GET VARIABLE INPUT FROM USER

## Age Categorization
streamlit.write("1. Berapa usia Anda?")
age = streamlit.number_input(label="Jawaban (scale 18-120)", min_value=18, max_value=120, step=1, key=1)

# Age Categorization Function
def checkAgeCategory(age):
    if(age>=18 and age<=24):
        ageStatus = "(1) 18-24 tahun"
        ageCat = 1
    elif(age>=25 and age<=29):
        ageStatus = "(2) 25-29 tahun"
        ageCat = 2
    elif(age>=30 and age<=34):
        ageStatus = "(3) 30-34 tahun"
        ageCat = 3
    elif(age>=35 and age<=39):
        ageStatus = "(4) 35-39 tahun"
        ageCat = 4
    elif(age>=40 and age<=44):
        ageStatus = "(5) 40-44 tahun"
        ageCat = 5
    elif(age>=45 and age<=49):
        ageStatus = "(6) 45-49 tahun"
        ageCat = 6
    elif(age>=50 and age<=54):
        ageStatus = "(7) 50-54 tahun"
        ageCat = 7
    elif(age>=55 and age<=59):
        ageStatus = "(8) 55-59 tahun"
        ageCat = 8
    elif(age>=60 and age<=64):
        ageStatus = "(9) 60-64 tahun"
        ageCat = 9
    elif(age>=65 and age<=69):
        ageStatus = "(10) 65-69 tahun"
        ageCat = 10
    elif(age>=70 and age<=74):
        ageStatus = "(11) 70-74 tahun"
        ageCat = 11
    elif(age>=75 and age<=79):
        ageStatus = "(12) 75-79 tahun"
        ageCat = 12
    elif(age>=80 and age<=120):
        ageStatus = "(13) 80 tahun atau lebih"
        ageCat = 13
    else:
        ageStatus = "(14) Tidak tahu/menolak untuk menjawab"
        ageCat = 0
    return ageStatus, ageCat
#

ageStatus, ageCat = checkAgeCategory(age)
streamlit.write("Kategori Usia: ", ageCat)
## End of Age Categorization

streamlit.write("")

## General Health Scale
streamlit.write("2. Bagaimana kondisi kesehatan Anda secara umum?")
generalHealth = streamlit.number_input(label="Jawaban (skala: 1 = luar biasa, 2 = sangat baik, 3 = baik, 4 = cukup, 5 = buruk)", min_value=1, max_value=5, key=2)
## General Health Scale

streamlit.write("")

## High Blood Pressure
streamlit.write("3. Apakah Anda dinyatakan mengalami tekanan darah tinggi oleh petugas Posbindu?")
bloodPressure = streamlit.number_input(label="Jawaban (0=tidak, 1=ya)", min_value=0, max_value=1, key=3)
## End of High Blood Pressure

streamlit.write("")

## High Chol
streamlit.write("4. Apakah Anda dinyatakan mengalami kolesterol tinggi oleh petugas Posbindu?")
cholCat = streamlit.number_input(label="Jawaban (0=tidak, 1=ya)", min_value=0, max_value=1, key=4)

# # Chol Status Function
# def checkCholStatus(cholesterol):
#     if(cholesterol>=50.0 and cholesterol<=200):
#         cholStatus = "Normal"
#         cholCat = 0
#     else:
#         cholStatus = "Tinggi"
#         cholCat = 1
#     return cholStatus, cholCat
# #

# cholStatus, cholCat = checkCholStatus(cholesterol)
# streamlit.write("Status kolesterol: ", cholStatus)
# streamlit.write("Kategori kolesterol: ", cholCat)
## End of High Chol

streamlit.write("")

## BMI
# User Input
streamlit.write("5. Apa status Indeks Massa Tubuh (IMT) Anda berdasarkan pemeriksaan oleh petugas Posbindu?")
# bmiCategory = streamlit.number_input(label="Jawaban (skala: 1 = Berat badan kurang, 2 = Normal, 3 = Kegemukan, 4 = Obesitas)", min_value=1, max_value=4, key=5)

# // BMI Counting Function
weight = streamlit.number_input(label="Mohon masukkan hasil pengukuran berat badan (dalam kg)", min_value=10.0, max_value=200.0, step=.1, format="%0.1f", key=51)
height = streamlit.number_input(label="Mohon masukkan hasil pengukuran tinggi badan (dalam cm)", min_value=10.0, max_value=200.0, step=.1, format="%0.1f", key=52)
bmi = weight / ((height/100)*(height/100))
bmi = round(bmi, 1)
#

# BMI Status Function
def checkBMIStatus(bmi):
    if(bmi>=10.0 and bmi<18.5):
        bmiStatus = "Berat badan kurang"
        bmiCat = 1
    elif(bmi>=18.5 and bmi<=24.9):
        bmiStatus = "Normal"
        bmiCat = 2
    elif(bmi>=25.0 and bmi<=29.9):
        bmiStatus = "Kegemukan"
        bmiCat = 3
    elif(bmi>=30.0 and bmi<=34.9):
        bmiStatus = "Obesitas"
        bmiCat = 4
    elif(bmi>=35.0 and bmi<=100.0):
        bmiStatus = "Obesitas berat"
        bmiCat = 5
    else:
        bmiStatus = ""
        bmiCat = 0
    return bmiStatus, bmiCat
#
bmiStatus, bmiCat = checkBMIStatus(bmi)
# Dont show BMI if above 100
if(bmi<100):
    streamlit.write("IMT anda: ", bmi)
else:
    streamlit.write("IMT anda:")
# // End of BMI Counting Function

# // BMI Category Function
# def checkBMIStatus(bmi):
#     if(bmi==1):
#         bmiStatus = "Berat badan kurang"
#         bmiCat = 1
#     elif(bmi==2):
#         bmiStatus = "Normal"
#         bmiCat = 2
#     elif(bmi==3):
#         bmiStatus = "Kegemukan"
#         bmiCat = 3
#     elif(bmi==4):
#         bmiStatus = "Obesitas"
#         bmiCat = 4
#     else:
#         bmiStatus = ""
#         bmiCat = 0
#     return bmiStatus, bmiCat
# bmiStatus, bmiCat = checkBMIStatus(bmiCategory)
# streamlit.write("Kategori IMT: ", bmiStatus)
# // End of BMI Category Function
# streamlit.write("BMI category: ", bmiCat)
## End of BMI

streamlit.write("")

## Difficulty Walk
streamlit.write("6. Apakah anda mengalami kesulitan berjalan atau menaiki tangga")
difficultyWalk = streamlit.number_input(label="Jawaban (0=tidak, 1=ya)", min_value=0, max_value=1, key=6)
## End of Difficulty Walk

streamlit.write("")
### End of GET VARIABLE INPUT FROM USER

## POST Data
dataFromUser = [[ageCat, generalHealth, bloodPressure, cholCat, bmiCat, difficultyWalk]]
# streamlit.write(dataFromUser)

## Predict New Data
result = clf.predict(dataFromUser)

## Check Diabetes Risk
if(result==0):
    streamlit.write("Status Diabetes: Tidak Berisiko.")
elif(result==1):
    streamlit.write("Status Diabetes: BERISIKO!")
else:
    streamlit.write("Error!")
###