# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd


plots_basic = {'AGE': 'https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/exploracion_cat_basic_AGE.html',
 'DEFAULT PAYMENT NEX MONTH': 'https://htmlpreview.github.io/?https://github.com/ancastillar/Default-of-Credit-Card_/blob/main/imgs/exploracion_cat_basic_default%20payment%20next%20month.html',
 'EDUCATION': 'https://htmlpreview.github.io/?https://github.com/ancastillar/Default-of-Credit-Card_/blob/main/imgs/exploracion_cat_basic_EDUCATION.html',
 'MARRIAGE': 'https://htmlpreview.github.io/?https://github.com/ancastillar/Default-of-Credit-Card_/blob/main/imgs/exploracion_cat_basic_MARRIAGE.html',
 'SEX': 'https://htmlpreview.github.io/?https://github.com/ancastillar/Default-of-Credit-Card_/blob/main/imgs/exploracion_cat_basic_SEX.html'}

 #--------------------------------------------------------------------------------------------------------------------------------------------------------


plots_repay = { "PAY_1": "https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/default_PAY_0.html",
                 "PAY_2": "https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/default_PAY_2.html",
                 "PAY_3": "https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/default_PAY_3.html",
                 "PAY_4": "https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/default_PAY_4.html",
                 "PAY_5": "https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/default_PAY_5.html",
                 "PAY_6": "https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/default_PAY_6.html"}


#----------------------------------------------------------------------------------------------------------------------------------------------------

plots_others_dist = {"A": "https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/bill_amount_age_marriage.html",
                     "B": "https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/bill_amount_default_educa_sex.html"}


#------------------------------------------------------------------------------------------------------------------------------------------------------

n_cluster_clients = {"2": "https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/cant_clients_n2.html", 
                     "3": "https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/cant_clients_n3.html"}



#------------------------------------------------------------------------------------------------------------------------------------------------------


car_clusters = {"2": "https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/mean_var_cluster_2.html",
                "3": "https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/mean_var_cluster_3.html"}




#------------------------------------------------------------------------------------------------------------------------------------------------------


var_clusters = {"1": "https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/mic_cluster_1.html",
                "2": "https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/mic_cluster_2.html"}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server


colors = {
    'background': '#111111',
    'text': '#EE1A26',
    'subtext':'slategray'
    ,'title':'gray'
}

################################layout aplicación#############################

app.layout =html.Div([
    dcc.Tabs(id="tabs-styled-with-props", value='tab-1', children=[
                                                                   
        dcc.Tab(label='Presentation', value='tab-1'),        
        dcc.Tab(label='Data Exploration', value='tab-2'),  
        dcc.Tab(label='Customer segmentation', value='tab-3'),
        dcc.Tab(label='Variables selection', value='tab-4'),   
        dcc.Tab(label='Modeling', value='tab-5'),    
        dcc.Tab(label='Testing', value='tab-6'),                                                                                                         
        dcc.Tab(label='Conclusions', value='tab-7'),    
    ], colors={
        "border": "white",
        "primary": "#58C4C8",
        "background": "#93DDE0"
    }),
    html.Div(id='tabs-content-props')
    
  
])



# Define callback to update graph

@app.callback(
    Output('graph3',  component_property="src"),
    Input("colorscale-dropdown_1",  component_property="value")
)

def figure_1(value):
    return plots_basic[value]


# Define callback to update graph

@app.callback(
    Output('graph4',  component_property="src"),
    Input("colorscale-dropdown_2",  component_property="value")
)
def figure_2(value):
    return plots_repay[value]
  


@app.callback(
    Output('graph5',  component_property="src"),
    Input("colorscale-dropdown_3",  component_property="value")
)


def figure_3(value):
    return plots_others_dist[value]
  

#----------------------------------------------------------------------------
@app.callback(
    Output('graph6',  component_property="src"),
    Input("colorscale-dropdown_4",  component_property="value")
)
def figure_4(value):
    return n_cluster_clients[value]


#----------------------------------------------------------------------------
@app.callback(
    Output('graph7',  component_property="src"),
    Input("colorscale-dropdown_5",  component_property="value")
)
def figure_5(value):
    return car_clusters[value]



#----------------------------------------------------------------------------
@app.callback(
    Output('graph8',  component_property="src"),
    Input("colorscale-dropdown_6",  component_property="value")
)
def figure_6(value):
    return var_clusters[value]

##########################################################################################
@app.callback(Output('tabs-content-props', 'children'),
              Input('tabs-styled-with-props', 'value'))






def render_content(tab):
#
    
    if tab == 'tab-1':
        return html.Div([html.Div( " ",style={'padding': 45}), html.H1(
        children='Natalia Castilla Reyes',
        style={
            'textAlign': 'center',
             'color': "#69797A"
        }
    ), 
   html.Img(src='https://raw.githubusercontent.com/ancastillar/Proyecto_Final_Series_Tiempo/dd3a88183b02567ba1de6581d1a0ddc18ec6cca2/modelo_elon_musk_bitcoin/output/IMG_20210828_141534-01.jpeg',
            
            style={'height': '25%',
                'width': '25%',  'textAlign': 'center', 'padding-left':'40%', 'padding-right':'55%'}),

    html.H6(
        children="Hi! I'm Natalia, I graduated in physics and I'm currently doing a master's degree in statistics at the National University of Colombia. My interest in data started in my undergraduate with a subject called information theory and since then I have strived to learn many tools that allow me to develop my creativity with data. I love programming, but I like much more to study the theoretical part behind each algorithm and then experiment with modifying it to obtain different results. My main interest in learning new things lies in being able to share my technical knowledge with others in a fun and clear way.",
        style={
            'textAlign': 'center',
             'color': "#69797A",  'padding-left':'10%', 'display': 'inline-block'
        }),
   
   html.Div( " ",style={'padding': 45}),
   html.H5(
        children='Background: Modeling to reduce credit risk, NLP, ETL',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),
    html.H5(
        children='Main projects: Sale of written-off portfolio (177.9 Bn COP)',
        style={
           
             'color': "#84B5EA",  'padding-left':'10%',
        }),
   html.H5(
        children='Programming languages: Python, C++, SQL, Spark',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block'
        }),
    html.H5(
        children='Analitics and ML: Keras, NumPy, Pandas, TensorFlow, Scikit-learn,Scipy, Stats',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%'
        }),

   html.Div( " ",style={'padding': 20}),

   html.H3(
        children='CONTACT:',
        style={
            
             'color': "#69797A", 'padding-left':'10%',
        }),
   dcc.Link('Github', href ="https://github.com/ancastillar",    style={ 'font-size' : '250%',  'padding-left':'10%', 'color': "#31B1D5"}),
   html.H1(
        children='',
        style={
            'textAlign': 'center',
             'color': "#69797A",
        }),
   dcc.Link('Linkedin', href ="https://www.linkedin.com/in/astridnataliacr/",    style={ 'font-size' : '250%', 'padding-left':'10%', 'color': "#31B1D5"}),
  


  
    ])
###############################################################################################################3
#################################################################################################################

#-----------------------------------------------------------------------        
    if tab == 'tab-2':
        return html.Div([html.Div( " ",style={'padding': 45}),
                         html.H1(
        children='Payment default analysis: Credit cards',
        style={
            'textAlign': 'center',
             'color': "#69797A"
        }
    ), 
    html.Embed(src='https://media2.giphy.com/media/TDyxBGZcViZnoye8iN/giphy.gif?cid=ecf05e47kwr8nwla4yk365teefdzijszjpg62k5bbqfvnhfy&rid=giphy.gif&ct=g',
               style={'width': '40%', 'float': 'center', 'display': 'inline-block','padding-left':'30%', 'padding-right':'50%'}),
               
     html.H6(
        children="The objective of this project is to predict the probability of default on a given obligation, in this case, credit cards. This will allow the generation of strategies that minimize the risk of deterioration of the client's financial health. Additionally, to facilitate the development of collection strategies, it is proposed to use clustering algorithms to find homogeneous segments within the population and thus provide differential treatment to each customer.",
        style={
            'textAlign': 'center',
             'color': "#69797A",  'padding-left':'10%', 'display': 'inline-block'
        }),

    html.Div( " ",style={'padding': 25}),
     html.H3(
        children='Description of data:',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),

     html.Div(
        children="This dataset contains information on defaults, demographic factors, credit data, payment history, and bill statements of credit card customers in Taiwan from April 2005 through September 2005.",
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),
      dcc.Link('Download the data here', href ="https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients",    style={ 'font-size' : '100%',  'padding-left':'10%', 'color': "#31B1D5"}),
    
    
   
     html.H5(
        children='Variables',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%',
        }),

     html.Div(
        children='ID: Identification of each credit.',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

      html.Div(
        children='LIMIT_BAL: Limit of credit granted in NT dollars (includes individual and family credit).',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',

        }),
      html.Div(
        children="'SEX: Gender (1=male, 2=female).",
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
  
        }),

      html.Div(
        children='EDUCATION: (1=higher education, 2=university, 3=secondary education, 4=other, 5=unknown, 6=unknown).',
        style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',

        }),

      html.Div(
        children='MARRIAGE: Marital status (1=married, 2=single, 3=other).',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
    
        }),

       html.Div(
        children='PAY0 - PAY6: Past payment history. Past monthly payment records (April through September 2005) have been tracked as follows: PAY0 = the reimbursement status in September 2005; PAY6 = the reimbursement status in April 2005. The measurement scale of the repayment status is: -2: No consumption; -1: Paid in full; 0: Use of revolving credit; 1 = late payment for one month; . . .; 9 = late payment for nine months or more.',
        style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

       html.Div(
        children='BILL_AMT1 - BILL_AMT6: Invoice statement amount from April through September 2005 (NT dollars).',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%'
        }),

      html.Div(
        children='PAY_AMT1 - PAY_AMT6 : Amount of the previous payment from April to September 2005 (NT dollar).',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),
       html.H3(
        children='EDA',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),

       html.H5(
        children='Exploring each variable',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%',
        }),
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


       html.Div([
       
      html.Label([
          "Select the variable of interest:",
          dcc.Dropdown(
              id='colorscale-dropdown_1', 
              
              options=[{'label': 'Género', 'value':'SEX'},{'label': 'Education', 'value': 'EDUCATION'},{'label': 'Marital status', 'value': 'MARRIAGE'},
                       {'label': 'Age', 'value': 'AGE'}, {'label': 'Target Variable', 'value': 'DEFAULT PAYMENT NEX MONTH'}]               
              ,value='DEFAULT PAYMENT NEX MONTH')])
       ], style={'color': "#9EBBDA",  'padding-left':'10%', 'display': 'inline-block','fontSize': 16, 'textAlign': 'center',} ),
      
     html.Embed( id='graph3',  src ="https://htmlpreview.github.io/?https://github.com/ancastillar/Default-of-Credit-Card_/blob/main/imgs/exploracion_cat_basic_MARRIAGE.html",  style={'width': '100%', 'height': 500,'float': 'center', 'padding-left':'5%','display': 'inline-block',}),
     html.Div(
        children='*  Remarks: We have an unbalanced classification problem, therefore we must employ sampling techniques to avoid overfitting in one category. We can also observe that the age distribution of the clients is between [21,79] years; most of the clients have marital status: single or married; no drastic unbalance is observed in the gender variable.',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

    html.H6(
        children='Analysis of the quota limit with respect to the level of education of each client.',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%',
        }),

    html.Embed(  src ="https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/bill_amount_edu.html", 
                style={'width': '100%', 'height': 650,'float': 'center', 'padding-left':'5%','display': 'inline-block',}), 
  

    html.Div(
        children='* Remarks: Those clients with university education have the possibility of acquiring larger quotas, while clients without higher education have the smallest quotas. It can also be observed that the distribution of quotas is quite skewed, there seem to be a few clients with quite high quotas; which does not necessarily mean that they are outliers in the distribution.',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

   html.H6(
        children='Analysis of the quota limit with respect to credit fulfillment',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%',
        }),

  html.Embed(  src ="https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/bins_limit_default.html", 
                style={'width': '100%', 'height': 450,'float': 'center', 'padding-left':'5%','display': 'inline-block',}),   
  html.Div(
        children='* Remarks: The largest number of defaulting clients is found in those loans with the smallest quota, on the other hand, the number of defaulting clients decreases as the quota of their obligation increases.',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),
   html.Div( " ",style={'padding': 15}),
#----------------------------------------------------------------------------------------------------------------------------------  
  
   html.Div([
   html.Label([
          "Select the month in which you want to view the credit status:",
          dcc.Dropdown(
              id='colorscale-dropdown_2', 
              
              options=[{'label': 'September', 'value':'PAY_1'},{'label': 'August', 'value': 'PAY_2'},{'label': 'July', 'value': 'PAY_3'},
                       {'label': 'June', 'value': 'PAY_4'}, {'label': 'May', 'value': 'PAY_5'},{'label': 'April', 'value': 'PAY_6'} ]               
              ,value='PAY_1')])
       ], style={'color': "#9EBBDA",  'padding-left':'10%', 'display': 'inline-block','fontSize': 16, 'textAlign': 'center',} ),
      
     html.Embed( id='graph4',  src ="https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/default_PAY_0.html",
                style={'width': '100%', 'height': 420,'float': 'center', 'padding-left':'5%','display': 'inline-block',}),
     html.Div(
        children='* Remarks: In all months it is presented that the largest number of clients with default are 2 months late in their payments. Note: The majority of clients with good payment behavior are in status 0 (Use of revolving credit) and -1 (paid in full).',
         
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),
   html.Div( " ",style={'padding': 15}),      
  html.H6(
        children='Analysis of non-compliance with respect to the level of education and marital status of each client.',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%',
        }),

  html.Embed(  src ="https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/pay_defaults_marriage_edu.html", 
                style={'width': '100%', 'height': 420,'float': 'center', 'padding-left':'5%','display': 'inline-block',}),   
  html.Div(
        children='* Remarks: Here we can observe a clear difference, single people tend to default much more on their obligations, regardless of their level of education. This is possible because married people have a more stable income and a larger support network.',
      
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

      html.Div( " ",style={'padding': 15}),
     html.H6(
        children='Analysis of some other distributions',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%',
        }),
#-------------------------------------------------------------------------------------------------------------------------------


   html.Div([
   html.Label([
          "Select another distribution to explore:",
          dcc.Dropdown(
              id='colorscale-dropdown_3', 
              
              options=[{'label': 'Credit quota with respect to age', 'value':'A'},{'label': 'Credit quota with respect to gender', 'value': 'B'}, ]               
              ,value='A')])
       ], style={'color': "#9EBBDA",  'padding-left':'10%', 'display': 'inline-block','fontSize': 16, 'textAlign': 'center',} ),
    html.Embed( id='graph5',  src ="https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/bill_amount_default_educa_sex.html",
                style={'width': '100%', 'height': 420,'float': 'center', 'padding-left':'5%','display': 'inline-block',}),  
    html.Div(
        children='* Remarks: Many of the people in Taiwan become married for a long time :). Many of the highest quotas are found in married people, except for young people.',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),


      html.H6(
        children='Correlation analysis',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%',
        }),

      html.Img(src='https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/correlations.png',
            
            style={'height': '50%',
                'width': '70%',  'textAlign': 'center', 'float':'center', 'display': 'inline-block', 'padding-left':'20%', 'padding-right':'20%'}),

      html.Div(
        children='* Remarks: We have highly correlated variables, but if we inspect a bit more we realize that most are lag variables (autoregressive in nature)..',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

     html.H4(
        children='Variable engineering',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%',
        }),


     html.Div(
        children='* Creation of trend variables: Payment and transaction behavior.',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

    html.Div(
    children='* Creation of basic statistical variables: average, maximum, standard deviation.',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),
    
    html.Div(
    children='* Ratio between the payment habit of each month with respect to transactions.',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

       html.Div(
       children='* Cumulative performance.',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

     dcc.Link('If you want to see in detail the process of variable creation click here', href ="https://github.com/ancastillar/Final_Project_Data_Science_Nanodegree",    style={ 'font-size' : '100%',  'padding-left':'10%', 'color': "#31B1D5"}),
    

    ], )


######################################################################################################################################   
    if tab == 'tab-3':
            return html.Div([html.Div( " ",style={'padding': 45}), html.H1(
            children='Clustering for customer segmentation',
            style={
                'textAlign': 'center',
                'color': "#69797A"
            }
        ), 
       html.Embed(src='https://dashee87.github.io/images/kmeans_bad.gif',
               style={'width': '45%', 'float': 'center', 'display': 'inline-block','padding-left':'30%', 'padding-right':'50%'}),

       html.Div( " ",style={'padding': 25}),

      html.H6(
        children='To provide a differentiated treatment to each client, it is usual to make models that allow segmenting the population into groups with similar characteristics. In this way, it is much easier to develop collection strategies together with the analytics team. The most used algorithm is K-means, however, this does not mean that it is the best but for the exploration objectives of this project this one will be used (I invite you to try more and if you get a better score contact me!). To train the algorithm I used credit behavior variables.',
        style={
            'textAlign': 'center',
             'color': "#69797A",  'padding-left':'10%', 'display': 'inline-block'
        }),

    html.Div( " ",style={'padding': 25}),

     html.H3(
        children='Variables:',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),

     html.Div(
        children='*LIMIT_BAL: Credit quota..',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

      html.Div(
        children='*AGE: Age of each customer.',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

      html.Div(
        children='*BILL_AMT1 - BILL_AMT6: Historical debt behavior.',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),
      html.Div(
        children='*PAY_AMT_AT: Trend indicating the increase in payments.',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),
        html.Div(
        children='*PAY_AMT_BT: Trend indicating a decrease in payments.',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

        html.Div(
        children='*ratio_bill_pay_bin_AT, ratio_bill_pay_bin_BT: Ratio between the historical behavior of transactions and payments.',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

        html.Div(
        children='*PAY_AMT_STD: Standard deviation of payments for each loan.',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

        html.Div(
        children='*BILL_AMT_STD: Standard deviation of movements of each loan.',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

     html.H3(
        children='Results:',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),

      html.Div(
        children='The results for the Silhouette score for the K-means algorithm are presented below:',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

     html.Embed(  src ="https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/Silhoute_score.html", 
                style={'width': '100%', 'height': 420,'float': 'center', 'padding-left':'5%','display': 'inline-block',}), 

   html.Div(
        children="*Remarks: We have the best score for n_cluster=2 (0.50), however for n_cluster=3 (0.48), so let's explore these two results in detail.",
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

    
    html.Div( " ",style={'padding': 25}),
 html.H5(
        children='Number of customers per cluster:',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),



    html.Div( " ",style={'padding': 5}),

    html.Div([
    html.Label([
          "Select the number of clusters you wish to explore:",
          dcc.Dropdown(
              id='colorscale-dropdown_4', 
              
              options=[{'label': '# cluster = 2', 'value':"2"},{'label': '# cluster = 3', 'value': "3"}, ]               
              ,value='3')])
       ], style={'color': "#9EBBDA",  'padding-left':'10%', 'display': 'inline-block','fontSize': 16, 'textAlign': 'center',} ),

    html.Embed( id="graph6",  src ="https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/cant_clients_n3.html",
                style={'width': '100%', 'height': 420,'float': 'center', 'padding-left':'5%','display': 'inline-block',}),  
    html.Div(
        children='* Remarks: The number of clients in the third cluster (769) is too small to warrant a good model.',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

         html.Div( " ",style={'padding': 25}),
        html.H5(
        children='Characterization of each cluster:',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),


        html.Div( " ",style={'padding': 5}),

    html.Div([
    html.Label([
          "Select the number of clusters you wish to explore:",
          dcc.Dropdown(
              id='colorscale-dropdown_5', 
              
              options=[{'label': '# cluster = 2', 'value':"2"},{'label': '# cluster = 3', 'value': "3"}, ]               
              ,value='3')])
       ], style={'color': "#9EBBDA",  'padding-left':'10%', 'display': 'inline-block','fontSize': 16, 'textAlign': 'center',} ),

    html.Embed( id="graph7",  src ="https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/mean_var_cluster_3.html",
                style={'width': '100%', 'height': 420,'float': 'center', 'padding-left':'5%','display': 'inline-block',}),  
    html.Div(
        children='* Remarks: For 2 clusters we have that there are quite different variables, for example the amount of quota of cluster 1 is much larger and we also have that their payment habit is higher with respect to the other cluster.',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),


           html.Div( " ",style={'padding': 25}),
        html.H4(
        children='Because the scoring and balancing on the data is better for 2 clusters I have decided to make two classification models.',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),
    ])

   
#######################################################################################################################################

    if tab == 'tab-4':
            return html.Div([html.Div( " ",style={'padding': 45}), html.H1(
            children='Variable selection: Mutual information',
            style={
                'textAlign': 'center',
                'color': "#69797A"
            }
        ), 
       html.Embed(src='https://media.giphy.com/media/xTiTnwqkkEtj3hm6DS/giphy.gif',
               style={'width': '35%', 'float': 'center', 'display': 'inline-block','padding-left':'35%', 'padding-right':'50%'}),

       html.Div( " ",style={'padding': 25}),
        html.H6(
        children='To select the most important variables in each cluster I have decided to use the concept of entropy, which is widely used in information theory. The definition of this concept in physics represents the amount of information I need to be able to fully determine the state of a system and eliminate its uncertainty. Thus, when we do not know the state of a system, we have maximum entropy. In statistics entropy is used to determine the degree of dependence between two random variables, the mathematical form of this concept is similar to the concept of the union of sets, in which we add each part separately and subtract its intercept; in this case, we add separately the Shanon entropy of each variable.',
        style={
            'textAlign': 'center',
             'color': "#69797A",  'padding-left':'10%', 'display': 'inline-block'
        }),


    html.Div( " ",style={'padding': 25}),

    html.H3(
        children='Methodology:',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),


      html.Div(
        children='* Calculamos el score MIC para cada covariable respecto a la variable objetivo.',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

      html.Div(
        children='* We chose a simple algorithm to train (for binary classification), in this case Logistic regression.',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),


      html.Div(
        children='* We use recursive elimination to determine the number of variables to use (the variables are ordered according to their MIC score).',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),
      html.Div(
        children='* We choose the number of variables that allow us to obtain the best performance of the algorithm (AUC).',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

      dcc.Link('If you want to see the process in detail, click here.', href ="https://github.com/ancastillar/Final_Project_Data_Science_Nanodegree",    style={ 'font-size' : '100%',  'padding-left':'10%', 'color': "#31B1D5"}),
    
      html.Div( " ",style={'padding': 25}),
      html.H3(
        children='Results:',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),

          html.Div(
        children='* For cluster 1: We eliminate 20 variables, leaving 66 variables',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

        html.Div(
        children='* For cluster 2: We eliminated 40 variables, leaving 46 variables',
        style={'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

      html.Div([
    html.Label([
          "Select the cluster you wish to explore:",
          dcc.Dropdown(
              id='colorscale-dropdown_6', 
              
              options=[{'label': 'cluster = 1', 'value':"1"},{'label': 'cluster = 2', 'value': "2"}, ]               
              ,value='2')])
       ], style={'color': "#9EBBDA",  'padding-left':'10%', 'display': 'inline-block','fontSize': 16, 'textAlign': 'center',} ),

    html.Embed( id="graph8",  src ="https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/mic_cluster_2.html",
                style={'width': '100%', 'height': 420,'float': 'center', 'padding-left':'5%','display': 'inline-block',}),  
    html.Div(
        children='* Remarks: For the two clusters we have that the most important variable is the average number of statuses that the customer has had historically, additionally it can be observed that for cluster 2 the variables related to transactions (BILL_AMT) have more relevance. ',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),



    ])

   
#######################################################################################################################################

    if tab == 'tab-5':
            return html.Div([html.Div( " ",style={'padding': 45}), html.H1(
            children='Model selection: K-fold',
            style={
                'textAlign': 'center',
                'color': "#69797A"
            }
        ), 
       html.Embed(src='https://upload.wikimedia.org/wikipedia/commons/4/4b/KfoldCV.gif',
               style={'width': '43%', 'float': 'center', 'display': 'inline-block','padding-left':'28%', 'padding-right':'50%'}),

       html.Div( " ",style={'padding': 25}),
        html.H6(
        children='To select the model, for each cluster, we trained 4 different binary classification models: SVM, XGB, KNN, NB (each of a different nature). To guarantee the performance of each one we used K-fold in which we partition the data 10 times. In this way we obtain a list of scores from which we can obtain some basic statistics: standard deviation, mean, average; The metrics used for the evaluation in each Fold were: AUC, F1-Score, and Accuracy. To balance the data we used SMOTE-TOMEK which creates an artificial sample according to the nearest neighbors of each point.',
        style={
            'textAlign': 'center',
             'color': "#69797A",  'padding-left':'10%', 'display': 'inline-block'
        }),
    
      html.Div( " ",style={'padding': 25}),
      html.H3(
        children='Results: Cluster 1',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),

    html.Embed(  src ="https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/comparacion_scores_4_modelos.html",
                style={'width': '100%', 'height': 720,'float': 'center', 'padding-left':'5%','display': 'inline-block',}),  
    html.Div(
        children='The best performance was achieved by the XGB model followed by KNN. The worst model was GNB with an AUC of 0.73.',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),

     html.Div( " ",style={'padding': 25}),
      html.H3(
        children='Results: Cluster 2',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),

    html.Embed(  src ="https://htmlpreview.github.io/?https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/comparacion_scores_4_modelos_cluster_22.html",
                style={'width': '100%', 'height': 720,'float': 'center', 'padding-left':'5%','display': 'inline-block',}),  
    html.Div(
        children='We obtain similar results to cluster 1, however the AUC for the XGB model is higher.',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),



    ])




#######################################################################################################################################

    if tab == 'tab-6':
            return html.Div([html.Div( " ",style={'padding': 45}), html.H1(
            children='Evaluation of results',
            style={
                'textAlign': 'center',
                'color': "#69797A"
            }
        ), 
       html.Embed(src='https://media.giphy.com/media/KCYCKOfUKl1tiFhbJG/giphy.gif',
               style={'width': '43%', 'float': 'center', 'display': 'inline-block','padding-left':'28%', 'padding-right':'50%'}),
      html.Div( " ",style={'padding': 25}),
        html.H6(
        children='To evaluate the model we used the evaluation data (these were not seen by the model in the previous phase). For the first model, we left 30% of the data for evaluation and the second 20%.',
        style={
            'textAlign': 'center',
             'color': "#69797A",  'padding-left':'10%', 'display': 'inline-block'
        }),

      html.Div( " ",style={'padding': 25}),    
      html.H3(
        children='Model loss functions: Cluster 1',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),


    html.Img(src='https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/log_loss_model_1.png',
            style={'height': '45%',
                'width': '55%',  'textAlign': 'center', 'padding-left':'25%', 'padding-right':'55%'}),
          
    html.H3(
        children='Medición de desempeño modelo: Cluster 1',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),


     html.Img(src='https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/resultados_modelo1_test.PNG',
            style={'height': '65%',
                'width': '85%',  'textAlign': 'center', 'padding-left':'10%', 'padding-right':'55%'}),
          
      
        html.H3(
        children='Importance variables  for model: Cluster 1',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),

       html.Img(src='https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/featue_impt_model_1.png',
            style={'height': '50%',
                'width': '50%',  'textAlign': 'center', 'padding-left':'25%', 'padding-right':'55%'}),
          
      

      
      html.Div( " ",style={'padding': 25}),   

      html.H3(
        children='Model loss functions: Cluster 2',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),


    html.Img(src='https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/log_loss_model_2.png',
            style={'height': '45%',
                'width': '55%',  'textAlign': 'center', 'padding-left':'25%', 'padding-right':'55%'}),

    html.H3(
        children='Performance measurement model: Cluster 2',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),


    html.Img(src='https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/resultados_modelo2_test.PNG',
            style={'height': '65%',
                'width': '85%',  'textAlign': 'center', 'padding-left':'10%', 'padding-right':'55%'}),
      
      html.H3(
        children='Importance variables  for model: Cluster 2',
        style={
           
             'color': "#9EBBDA",  'padding-left':'10%','display': 'inline-block',
        }),

       html.Img(src='https://raw.githubusercontent.com/ancastillar/Default-of-Credit-Card_/main/imgs/featue_impt_model_2.png',
            style={'height': '50%',
                'width': '50%',  'textAlign': 'center', 'padding-left':'25%', 'padding-right':'55%'}),
          
      html.Div(
        children='* Remarks: Through the loss function we can evaluate the presence of overfitting of the model (the loss function in validation begins to increase red curve), however it is not present in either case.',
                style={ 'fontSize': 16, 'color': "#69797A",  'padding-left':'10%',
        }),



    ])
            

################################################################################################################################
    if tab == 'tab-7':
            return html.Div([html.Div( " ",style={'padding': 45}), html.H1(
            children='Conclusions',
            style={
                'textAlign': 'center',
                'color': "#69797A"
            }
        ), 
    
      html.Div( " ",style={'padding': 25}),
      html.Div(
        children='* We use a clustering algorithm to find the best segmentation within the population. We find customers with relatively larger quotas who have better payment habits and the standard deviation in payments is higher than the other segment.',
                style={ 'fontSize': 18, 'color': "#69797A",  'padding-left':'10%',
        }),
      html.Div(
        children='* Strategies should be developed to reduce the non-compliance rate in small quotas $(5000,50000].',
                style={ 'fontSize': 18, 'color': "#69797A",  'padding-left':'10%',
        }),
       html.Div(
        children='* The age range with the highest rate of noncompliance (44.1%) was found to be (71-91] years.',
                style={ 'fontSize': 18, 'color': "#69797A",  'padding-left':'10%',
        }),

       html.Div(
        children='* An AUC of 0.81 was determined for model 2 and 0.78 for model 1.',
                style={ 'fontSize': 18, 'color': "#69797A",  'padding-left':'10%',
        }),


    ])
  
if __name__=='__main__':
    
    app.run_server(debug=True)

