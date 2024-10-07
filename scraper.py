from bs4 import BeautifulSoup
import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}


tunisia_tech=""
def tunisia_tech(product_name):
    try:
        global tunisia_tech
        #Change the form of product_name
        name1 = product_name.replace(" ","+")
        #Get the url
        tunisia_tech=f'https://tunisiatech.tn/search?s={name1}'
        #Get the html code of this result
        res = requests.get(tunisia_tech,headers=headers)
        #We do this scraping with html.parser
        soup = BeautifulSoup(res.text,'html.parser')
        #If we have the class of a is product-item-link we get the name
        if(soup.select('article')): 
            #On obtient le contenu de html de cette div,li ...
                    prod_name_in_tech = soup.select('h5')[0].getText().strip().upper()

                    #On fait le test is le nom existes dans le resulat
                    #On prend seulement le premier resultat 
                    if product_name.split(" ")[0]:
                        #On obtient le nom,prix de ce produit par le scraping
                            prod_price_in_tunisia_tech = soup.select('span.price')[0].getText().strip().upper()
                            prod_name_in_tunisia_tech = soup.select('h5')[0].getText().strip().upper()
                            print("MegaPC:")
                            print(prod_name_in_tunisia_tech)
                            print(prod_price_in_tunisia_tech)
                            print("---------------------------------")
        else:
                #Sinon le prix = 0
                prod_price_in_tunisia_tech='0' 
                        
        return {'Product_Name':prod_name_in_tunisia_tech,'Website':'tunisia_tech','Price':prod_price_in_tunisia_tech.replace("\u202f", "").replace("\xa0","")}
    except:
        print("tunisia_tech: No product found!")  
        print("---------------------------------")
        prod_price_in_tunisia_tech= '0'
        return {'Product_Name':prod_name_in_tunisia_tech,'Website':'tunisia_tech','Price':prod_price_in_tunisia_tech}
    
    
'''pr1=tunisia_tech("pc gamer")
print(pr1)'''




#Tunisianet
tunisianet=""
def tunisianet(product_name):
    try:
        global tunisianet
        #Change the form of product_name
        name1 = product_name.replace(" ","+")
        #Get the url
        tunisianet=f'https://www.tunisianet.com.tn/recherche?controller=search&s={name1}&submit_search=&categories=informatique&prix=1644-13999&processeur=amd-ryzen-5,amd-ryzen-7,amd-ryzen-9,intel-core-i3,intel-core-i5,intel-core-i5-12eme-gen,intel-core-i7,intel-core-i9,intel-core-i9-12eme-gen&order=product.price.asc'
        #Get the html code of this result
        res = requests.get(tunisianet,headers=headers)
        #We do this scraping with html.parser
        soup = BeautifulSoup(res.text,'html.parser')
        #If we have the class of a is product-item-link we get the name
        if(soup.select('article')):
            #On obtient le contenu de html de cette div,li ...
                    prod_name_in_tunisianet = soup.select('h2.h3')[0].getText().strip().upper()

                    #On fait le test is le nom existes dans le resulat
                    #On prend seulement le premier resultat 
                    if product_name[0].upper() in prod_name_in_tunisianet:
                        #On obtient le nom,prix de ce produit par le scraping
                            prod_price_in_tunisianet = soup.select('div.product-price-and-shipping')[0].getText().strip().upper()
                            prod_name_in_tunisianet = soup.select('h2.h3')[0].getText().strip().upper()
                            print("tunisianet:")
                            print(prod_name_in_tunisianet)
                            print(prod_price_in_tunisianet)
                            print("---------------------------------")
        else:
            #Sinon le prix = 0
            prod_price_in_tunisianet='0' 
        return {'Product_Name':prod_name_in_tunisianet,'Website':'Tunisia_Net','Price':prod_price_in_tunisianet.replace("\xa0","").replace("\nPRIX","")}
    
    except:
        print("tunisianet: No product found!")  
        print("---------------------------------")
        prod_price_in_tunisianet= '0'
        prod_name_in_tunisianet=''
        return {'Product_Name':prod_name_in_tunisianet,'Website':'Tunisia_Net','Price':prod_price_in_tunisianet}
    
    
'''print(tunisianet("pc gamer"))
'''
#Wiki
wiki=""
def wiki(product_name):
    try:
        global wiki
        #Change the form of product_name
        name1 = product_name.replace(" ","+")
        #Get the url
        wiki=f'https://www.wiki.tn/recherche?controller=search&orderby=position&orderway=desc&search_query={name1}&submit_search=&prix=1644-13999&processeur=amd-ryzen-5,amd-ryzen-7,amd-ryzen-9,intel-core-i3,intel-core-i5,intel-core-i5-12eme-gen,intel-core-i7,intel-core-i9,intel-core-i9-12eme-gen&order=product.price.asc'
        #Get the html code of this result
        res = requests.get(wiki,headers=headers)
        #We do this scraping with html.parser
        soup = BeautifulSoup(res.text,'html.parser')
        #If we have the class of a is product-item-link we get the name
        if(soup.select('div.ajax_block_product')):
            #On obtient le contenu de html de cette div,li ...
                    prod_name_in_wiki = soup.select('h4')[0].getText().strip().upper()

                    #On fait le test is le nom existes dans le resulat
                    #On prend seulement le premier resultat 
                    if product_name[0].upper() in prod_name_in_wiki:
                        #On obtient le nom,prix de ce produit par le scraping
                            prod_price_in_wiki = soup.select("div[class=content_price] > span")[0].getText().strip().upper()
                            prod_name_in_wiki = soup.select('h4')[0].getText().strip().upper()
                            print("Wiki:")
                            print(prod_name_in_wiki)
                            print(prod_price_in_wiki)
                            print("---------------------------------")
        else:
            #Sinon le prix = 0
            prod_price_in_wiki='0' 
        return {'Product_Name':prod_name_in_wiki,'Website':'Wiki','Price':prod_price_in_wiki.replace("\xa0","").replace("\nPRIX","")}
    
    except:
        print("Wiki: No product found!")  
        print("---------------------------------")
        prod_price_in_wiki= '0'
        prod_name_in_wiki=''
        return {'Product_Name':prod_name_in_wiki,'Website':'Wiki','Price':prod_price_in_wiki}

def suggested_products(product_name):
    return([wiki(product_name),tunisianet(product_name),tunisia_tech(product_name)])


                

