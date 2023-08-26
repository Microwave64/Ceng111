import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.model_selection
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import sklearn.metrics
import statsmodels.api as sm
import math





#Data read
file_path = './excel_table.csv'
path_bandrol = "./yayın_genre.csv"
lst = ["GDP", "Interest rate"]
month_lst = [
            "Ocak",
            "Şubat",
            "Mart",
            "Nisan",
            "Mayıs",
            "Haziran",
            "Temmuz",
            "Ağustos",
            "Eylül",   
            "Ekim",
            "Kasım",   
            "Aralık"
]
dpd_lst = []




#LINEAR REGRESSION FUNCTION
def Linear_func(file_path, future_val ,data_y, data_x = "Year"):
    #List for return predictions
    lst = []

    #Reading data from excel
    df = pd.read_csv(file_path)    

    #Processing data to use it in sklearn
    df_binary = df[[data_x, data_y]]
    
    
    #plotting the Scatter plot to check relationship
    # sns.lmplot(x = data_x, y = data_y, data = df_binary, order = 2, ci = None)
    # plt.show()


    df_binary.fillna(method = 'ffill', inplace = True)

    #Training model
    X = np.array(df_binary[data_x]).reshape(-1,1)
    Y = np.array(df_binary[data_y]).reshape(-1,1)


    #Split model and test data
    
    X_train , X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y, test_size = 0.3)
    reg = LinearRegression()
    reg.fit(X_train, Y_train)
    # score = reg.score(X_test, Y_test)
    # print(score)

    #Results for grapgh and real wanted_prediction
    y_pred = reg.predict(X_test)


    # reg.fit(X,Y)#NOT SURE ABOUT ITS NECESSITY
    np_fut_arr = np.array(future_val).reshape(-1,1)
    fut_predict = reg.predict(np_fut_arr)

    #Score
    score1 = reg.score(X,Y)
    # print(score1)

    #Graph
    # plt.scatter(X_test, Y_test, color = 'b')
    # plt.plot(X_test, y_pred, color = 'r')
    # plt.show() 


    return float(fut_predict[0][0])







#Polynomial Regression
def poly_reg(file_path, future_val, data_y, data_x = "Year"):
    #Data reading
    df = pd.read_csv(file_path)
    
    #Processing data to use it in sklearn
    df_binary = df[[data_x, data_y]]
    df_binary.fillna(method = 'ffill', inplace = True)
    X = np.array(df_binary[data_x]).reshape(-1,1)
    y = np.array(df_binary[data_y]).reshape(-1,1)


    #Regression Lin1
    X_train , X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.25)
    lin = LinearRegression()
    lin.fit(X_train, Y_train)

    #Poly features    
    poly = PolynomialFeatures(degree = (1,16))
    X_poly = poly.fit_transform(X_train)
    poly.fit(X_poly, Y_train)

    #Reg Lin2
    lin2 = LinearRegression()
    lin2.fit(X_poly, Y_train)

    """
    #Graphs
    plt.scatter(X, y, color='blue')
 
    plt.plot(X, lin.predict(X), color='red')
    plt.title('Linear Regression')
    plt.xlabel(data_x)
    plt.ylabel(data_y)
    
    plt.show()
    """

    #prediction
    pred_arr = np.array([[future_val]])
    pred_ling =lin.predict(pred_arr)
    pred_poly = lin2.predict(poly.fit_transform(pred_arr))


    """
    # Graph2 Visualising the Polynomial Regression results
    plt.scatter(X, y, color='blue')
    
    plt.plot(X, lin2.predict(poly.fit_transform(X)),
            color='red')
    plt.title('Polynomial Regression')
    plt.xlabel(data_x)
    plt.ylabel(data_y)
    
    plt.show()
    """
            
            #Score Values
    score1 = lin.score(X_test, Y_test)
    score2 = lin2.score(X_poly, Y_train)
    # print("Score-Linear:", score1)
    # print("Score-Polynomial:", score2)

    if (score1 > score2):
        return pred_ling[0][0]    
    return float(pred_poly[0][0])








def poly_lin_regression(file_path, wanted_str, deter_lst):
    # Reading data from excel
    df = pd.read_csv(file_path)
    df = df.dropna()
    year = df["Year"]
    year = year.iloc[-1] + 1
    start_year = year - df.shape[0]


    # Processing Data
    X = np.array(df[deter_lst])
    y = np.array(df[wanted_str]).reshape(-1, 1)

    #Finding the most certain degree for regression
    max_score = 0
    y_pred_certain = 0   
    # degree_pol = 8 


    pre_gra_lst = []
    # number_degrees = [2,3,4,5,6,7]
    score_lst = []
    year_lst = []
    for i in range(start_year, year):
        year_lst.append(i)
    
    stat_lst = [year]
    poly_linear_lst = ["^Bandrol alan kitap adedi", "PPP", "^Ücretsiz dağıtılan ders kitabı adedi"]
    linear_func_lst = ["^Toplam nüfus", "Interest rate", "GDP"]
    poly_lst = ["^Yayınevi sayısı", "^Dağıtım şirketi sayısı"]


    for i in range(1, len(deter_lst)):    
        if (deter_lst[i] in poly_linear_lst):
            pass
        elif(deter_lst[i] in linear_func_lst):
            stat_lst.append(Linear_func(file_path, year, deter_lst[i]))
        elif(deter_lst[i] in poly_lst):
            stat_lst.append(poly_reg(file_path, year, deter_lst[i]))
    
    
    
        #Poly model
    # if(wanted_str in poly_linear_lst):
    #     degree_pol = 1

    poly_model = PolynomialFeatures(degree = 1, include_bias=False)  
    
    poly_x_values = poly_model.fit_transform(X)
    poly_model.fit(poly_x_values, y)
    
    #Linear Regression
    regression_model = LinearRegression()
    regression_model.fit(poly_x_values, y)
        

    #Prediction
    pred_lst = []
    pred_lst += stat_lst
    pred_lst = np.array(pred_lst).reshape(1, -1)    
    y_pred = regression_model.predict(poly_model.fit_transform(pred_lst))

    pre_gra_lst.append(y_pred[0][0])


    score = regression_model.score(poly_x_values, y)
    score_lst.append(score)
    if (score > max_score):
        max_score = score
        y_pred_certain = y_pred

                #GRAPHS
    # plt.scatter(number_degrees, score_lst, color="green")
    # plt.plot(number_degrees, score_lst, color="red") 
    # plt.title("Degree vs Score") 
    # plt.show()
    
    # print("max_score:", max_score)
    # print("Score lst:", score_lst)
    
    # plt.scatter(number_degrees, pre_gra_lst, color="green")
    # plt.plot(number_degrees, pre_gra_lst, color="red") 
    # plt.title("Degree vs Prediction")
    # plt.show()



    # if(wanted_str == "^Bandrol alan kitap adedi"):
    #     plt.scatter(year_lst, y, color="green")
    #     plt.plot(year_lst, y, color="red") 
    #     plt.title("Year vs Bandrol")
    #     plt.ylabel("Bandrol alan kitap adedi")
    #     plt.xlabel("Year")
    #     plt.show()

        #Statistical Table
    # if(wanted_str == "^Bandrol alan kitap adedi"):
    #     print(max_score)
    #     const = sm.add_constant(X)
    #     model = sm.OLS(y, const)
    #     results = model.fit()
    #     print(results.summary())
    
    return float(y_pred_certain[0][0])






def main_func(file_path, until):
    #Dataframe
    df = pd.read_csv(file_path)

    #Data Bandrol per year
    df_band = pd.read_csv(path_bandrol)
    band_dict = dict.fromkeys(month_lst, None)
    df_new_band = dict.fromkeys(month_lst, None)
    band_total = 0
    tot = 0

    #Year
    year = df["Year"]
    year = year.iloc[-1] + 1
    
    year_dict = {"Year":[year]}


    #Total Population
    population = int(Linear_func(file_path, year, "^Toplam nüfus"))

    #Yayınevi Sayısı
    yayevi_num = int(poly_reg(file_path, year, "^Yayınevi sayısı"))

    #Dağıtım Şirketi
    distribution_comp = int(poly_reg(file_path, year, "^Dağıtım şirketi sayısı"))

    #Interest Rate
    interest_rate = round(Linear_func(file_path, year, "Interest rate"), 2)

    #GDP
    gdp_lst = ["Year","Interest rate"] 
    gdp = int(Linear_func(file_path, year, "GDP"))

    #PPP
    ppp_lst = ["Year", "^Toplam nüfus", "GDP"]
    ppp = round(poly_lin_regression(file_path, "PPP", ppp_lst),1)
    
    #Bandrol alan kitap adedi
    for month in month_lst:
        band_pred = int(Linear_func(path_bandrol, year, month))
        band_dict[month] = band_pred
        band_total += band_pred

    bandrol_dlst = ["Year", "^Toplam nüfus", "^Yayınevi sayısı", "^Dağıtım şirketi sayısı", "GDP"]
    bandrol_num = int(poly_lin_regression(file_path, "^Bandrol alan kitap adedi", bandrol_dlst))

    for month in month_lst:
        band_dict[month] = [math.floor(band_dict[month] * (bandrol_num/band_total))]
        tot += band_dict[month][0]

    #Insert year value
    print(tot)
    year_dict.update(band_dict)
    #Append total estimated bandrol
    tot_dict = {"TOPLAM": [tot]}
    year_dict.update(tot_dict)

    print(year_dict)
    

    #Write bandrol per month table 
    df_new_band = pd.DataFrame(year_dict)
    df_new_band.to_csv(path_bandrol, mode = 'a', index = False, header = False)





    #Meb Free Distrubution
    meb_booklet_lst = ["Year", "^Toplam nüfus", "GDP"]
    ind_meb = "^Ücretsiz dağıtılan ders kitabı adedi"
    meb_booklet_num =  int(poly_lin_regression(file_path, ind_meb, meb_booklet_lst))

    #Total book
    total_book_num = bandrol_num + meb_booklet_num




    #DATA FRAME
    df_new = pd.DataFrame({"Year": [year], 
                           "^Toplam nüfus": [population],
                           "^Yayınevi sayısı": [yayevi_num],
                           "^Bandrol alan kitap adedi": [bandrol_num],
                           "^Ücretsiz dağıtılan ders kitabı adedi": [meb_booklet_num],
                           "^Üretilen toplam kitap adedi": [total_book_num],
                           "^Dağıtım şirketi sayısı": [distribution_comp],
                           "GDP": [gdp],
                           "PPP": [ppp],
                           "Interest rate": [interest_rate],
                           })


    df_new.to_csv(file_path, mode = 'a', index = False, header = False)

    if (year < until):
        return main_func(file_path, until)

main_func(file_path, 2028)