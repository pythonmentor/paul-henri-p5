import mysql.connector
from API import cleaned_products
from mysql_connector import db_pur_beurre
from mysql_connector import dbcursor


class Product_storage:

    def __init__(self, data):

        self.data = data

    def save(self):

       save_formula = "INSERT INTO product (id, name, nutrition_grade, ingredients, url, categories, stores) VALUES (%s, %s, %s, %s, %s, %s, %s)" 
       dbcursor.executemany(save_formula, self.data)
       db_pur_beurre.commit()


Product_storage(cleaned_products).save()

