from flask import Flask,render_template,request


#Search field : Including librairies
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired,Length

#Doing the scraping of the product in two websites 
from scraper import tunisia_tech,tunisianet,wiki,suggested_products

data_prod=suggested_products


#Creating the flask app 
app = Flask(__name__)


#Secret Key + Bootstrap 
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']='thisissupposedtobeasecretkey'


#Declaring SearchForm
class Searchform(FlaskForm):
    product_name=StringField('Product_Name',validators=[InputRequired(),Length(min=5,max=15)])
    
    
#Defining routes 
#For every home we have a navbar a header and a footer


#Home Page : in it we show the Search bar and we fill it with the product
#Adding POST and GET methods to the routes 
@app.route('/', methods=['GET','POST'])
def home():
    #Add the search form to the home section route
    form = Searchform()
    if(form.validate_on_submit()):
        return ('<h1>'+tunisia_tech(form.product_name.data)["Website"] +" suggested " +tunisia_tech(form.product_name.data)["Product_Name"] + "and its price is :" +tunisia_tech(form.product_name.data)["Price"]  +'<br>' +'</h1>' 
                +'<h1>'+tunisianet(form.product_name.data)["Website"] +" suggested " +tunisianet(form.product_name.data)["Product_Name"] + "and its price is :" +tunisianet(form.product_name.data)["Price"]  +'<br>' +'</h1>' 
                +'<h1>'+wiki(form.product_name.data)["Website"] +" suggested " +wiki(form.product_name.data)["Product_Name"] + "and its price is :" +wiki(form.product_name.data)["Price"]  +'<br>' +'</h1>')
    return render_template('home.html',form=form)


#About Us : this is a simple section in it we define the purpose of the website 

@app.route('/about')
def about():
    return render_template('about.html')

#Latest Searched Products 
@app.route('/searched_products')
def searched_products():
    return render_template('searched_products.html',data_prod=suggested_products)

#Return the product name from Home Page and store  it in a json file 
#While running the code the website will be shown
if (__name__ == "__main__"):
    app.run(debug=True)
    
    
  