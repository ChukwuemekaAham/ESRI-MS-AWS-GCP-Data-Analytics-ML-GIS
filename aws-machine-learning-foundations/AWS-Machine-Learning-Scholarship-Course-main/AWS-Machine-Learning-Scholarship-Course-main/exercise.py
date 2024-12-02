#!/usr/bin/env python
# coding: utf-8

# # OOP Syntax Exercise - Part 2
# 
# Now that you've had some practice instantiating objects, it's time to write your own class from scratch. This lesson has two parts. In the first part, you'll write a Pants class. This class is similar to the shirt class with a couple of changes. Then you'll practice instantiating Pants objects
# 
# In the second part, you'll write another class called SalesPerson. You'll also instantiate objects for the SalesPerson.
# 
# For this exercise, you can do all of your work in this Jupyter notebook. You will not need to import the class because all of your code will be in this Jupyter notebook.
# 
# Answers are also provided. If you click on the Jupyter icon, you can open a folder called 2.OOP_syntax_pants_practice, which contains this Jupyter notebook ('exercise.ipynb') and a file called answer.py.

# # Pants class
# 
# Write a Pants class with the following characteristics:
# * the class name should be Pants
# * the class attributes should include
#  * color
#  * waist_size
#  * length
#  * price
# * the class should have an init function that initializes all of the attributes
# * the class should have two methods
#  * change_price() a method to change the price attribute
#  * discount() to calculate a discount

# In[ ]:


### TODO:
#   - code a Pants class with the following attributes
#   - color (string) eg 'red', 'yellow', 'orange'
#   - waist_size (integer) eg 8, 9, 10, 32, 33, 34
#   - length (integer) eg 27, 28, 29, 30, 31
#   - price (float) eg 9.28

### TODO: Declare the Pants Class 

### TODO: write an __init__ function to initialize the attributes

### TODO: write a change_price method:
#    Args:
#        new_price (float): the new price of the shirt
#    Returns:
#        None

### TODO: write a discount method:
#    Args:
#        discount (float): a decimal value for the discount. 
#            For example 0.05 for a 5% discount.
#
#    Returns:
#        float: the discounted price


# In[ ]:


class Pants:
    """The Pants class is a blue print that comprise of clotthing sell in a store
    """
    
    def _init_(self, color, waist_size, lenght, price):
        """The method that initialize a Pants object
        
        Args:
            color (string)
            waist_size (integer)
            lenght (integer)
            price (float)
        
        Attributes:
                color (string): color of a pants object
                waist_size (integer): waist size of a pants object
                lenght (integer): lenght of a pants object
                price (float): price of a pants object
        """
        
        self.color = color
        self.size = waist_size 
        self.lenght = lenght
        self.price = price
    
    def change_price(self, new_price):
        """The change_price method changes the price attributes of a pants object
        
        Args:
            new_price (float): the new price of a pants object
            
        Return: None
        
        """
        self.price = new_price
        
    
    def discount(self, discount):
        """The discount methods outputs a discount of a pants object
        
        Args:
            discount (float): discount in percentage for a pants object
            
        Return: 
            float: the discount price
        """
        return self.price * (1 - discount)


# # Run the code cell below to check results
# 
# If you run the next code cell and get an error, then revise your code until the code cell doesn't output anything.

# In[ ]:





# # SalesPerson class
# 
# The Pants class and Shirt class are quite similar. Here is an exercise to give you more practice writing a class. **This exercise is trickier than the previous exercises.**
# 
# Write a SalesPerson class with the following characteristics:
# * the class name should be SalesPerson
# * the class attributes should include
#  * first_name 
#  * last_name
#  * employee_id
#  * salary
#  * pants_sold
#  * total_sales
# * the class should have an init function that initializes all of the attributes
# * the class should have four methods
#  * sell_pants() a method to change the price attribute
#  * calculate_sales() a method to calculate the sales
#  * display_sales() a method to print out all the pants sold with nice formatting
#  * calculate_commission() a method to calculate the salesperson commission based on total sales and a percentage

# In[ ]:


### TODO:
#   Code a SalesPerson class with the following attributes
#   - first_name (string), the first name of the salesperson
#   - last_name (string), the last name of the salesperson
#   - employee_id (int), the employee ID number like 5681923
#   - salary (float), the monthly salary of the employee
#   - pants_sold (list of Pants objects), 
#            pants that the salesperson has sold 
#   - total_sales (float), sum of sales of pants sold

### TODO: Declare the SalesPerson Class 

### TODO: write an __init__ function to initialize the attributes
###    Input Args for the __init__ function:
#        first_name (str)
#        last_name (str)
#        employee_id (int)
# .      salary (float)
#
# You can initialize pants_sold as an empty list
# You can initialize total_sales to zero.
#
###

### TODO: write a sell_pants method:
#
#    This method receives a Pants object and appends
#    the object to the pants_sold attribute list
#
#    Args:
#        pants (Pants object): a pants object
#    Returns:
#        None

### TODO: write a display_sales method:
#    
#    This method has no input or outputs. When this method 
#    is called, the code iterates through the pants_sold list
#    and prints out the characteristics of each pair of pants
#    line by line. The print out should look something like this
#
#   color: blue, waist_size: 34, length: 34, price: 10
#   color: red, waist_size: 36, length: 30, price: 14.15
#
#
#
###

### TODO: write a calculate_sales method:
#      This method calculates the total sales for the sales person.
#      The method should iterate through the pants_sold attribute list
#      and sum the prices of the pants sold. The sum should be stored
#      in the total_sales attribute and then return the total.
#      
#      Args:
#        None
#      Returns:
#        float: total sales
#
###  


### TODO: write a calculate_commission method:
#
#   The salesperson receives a commission based on the total
#   sales of pants. The method receives a percentage, and then
#   calculate the total sales of pants based on the price,
#   and then returns the commission as (percentage * total sales)
#
#    Args:
#        percentage (float): comission percentage as a decimal
#
#    Returns:
#        float: total commission
#
#
###


# In[ ]:


### NOTE - Pants Class was implemeted in same cell with SalesPerson C:
#
#  When the code is run it generate error for check_results()
#  I notice that possibly the "SalesPerson Class" is not seen the "Pant Class"

class Pants:
    """The Pants class represents an article of clothing sold in a store
    """

    def __init__(self, color, waist_size, length, price):
        """Method for initializing a Pants object

        Args:
            color (str)
            waist_size (int)
            length (int)
            price (float)

        Attributes:
            color (str): color of a pants object
            waist_size (str): waist size of a pants object
            length (str): length of a pants object
            price (float): price of a pants object
        """

        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    def change_price(self, new_price):
        """The change_price method changes the price attribute of a pants object

        Args:
            new_price (float): the new price of the pants object

        Returns: None

        """
        self.price = new_price

    def discount(self, percentage):
        """The discount method outputs a discounted price of a pants object

        Args:
            percentage (float): a decimal representing the amount to discount

        Returns:
            float: the discounted price
        """
        return self.price * (1 - percentage)


class SalesPerson:
    """The SalesPerson class represents an employee in the store

    """

    def __init__(self, first_name, last_name, employee_id, salary):
        """Method for initializing a SalesPerson object

        Args:
            first_name (str)
            last_name (str)
            employee_id (int)
            salary (float)

        Attributes:
            first_name (str): first name of the employee
            last_name (str): last name of the employee
            employee_id (int): identification number of the employee
            salary (float): yearly salary of the employee
            pants_sold (list): a list of pants objects sold by the employee
            total_sales (float): sum of all sales made by the employee

        """
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants_object):
        """The sell_pants method appends a pants object to the pants_sold attribute

        Args:
            pants_object (obj): a pants object that was sold

        Returns: None

        """

        self.pants_sold.append(pants_object)

    def display_sales(self):
        """The display_sales method prints out all pants that have been sold

        Args: None

        Returns: None

        """

        for pants in self.pants_sold:
            print('color: {}, waist_size: {}, length: {}, price: {}'                   .format(pants.color, pants.waist_size, pants.length, pants.price))

    def calculate_sales(self):
        """The calculate_sales method sums the total price of all pants sold

        Args: None

        Returns:
            float: sum of the price for all pants sold

        """

        total = 0
        for pants in self.pants_sold:
            total += pants.price

        self.total_sales = total

        return total

    def calculate_commission(self, percentage):
        """The calculate_commission method outputs the commission based on sales

        Args:
            percentage (float): the commission percentage as a decimal

        Returns:
            float: the commission due
        """

        sales_total = self.calculate_sales()
        return sales_total * percentage 


# # Run the code cell below to check results
# 
# If you run the next code cell and get an error, then revise your code until the code cell doesn't output anything.

# In[ ]:


def check_results():
    pants_one = Pants('red', 35, 36, 15.12)
    pants_two = Pants('blue', 40, 38, 24.12)
    pants_three = Pants('tan', 28, 30, 8.12)
    
    salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
    
    assert salesperson.first_name == 'Amy'
    assert salesperson.last_name == 'Gonzalez'
    assert salesperson.employee_id == 2581923
    assert salesperson.salary == 40000
    assert salesperson.pants_sold == []
    assert salesperson.total_sales == 0
    
    salesperson.sell_pants(pants_one)
    salesperson.pants_sold[0] == pants_one.color
    
    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)
    
    assert len(salesperson.pants_sold) == 3
    assert round(salesperson.calculate_sales(),2) == 47.36
    assert round(salesperson.calculate_commission(.1),2) == 4.74
    
    print('Great job, you made it to the end of the code checks!')
    
check_results()


# ### Check display_sales() method
# 
# If you run the code cell below, you should get output similar to this:
# 
# ```python
# color: red, waist_size: 35, length: 36, price: 15.12
# color: blue, waist_size: 40, length: 38, price: 24.12
# color: tan, waist_size: 28, length: 30, price: 8.12
# ```

# In[6]:


pants_one = Pants('red', 35, 36, 15.12)
pants_two = Pants('blue', 40, 38, 24.12)
pants_three = Pants('tan', 28, 30, 8.12)

salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)

salesperson.sell_pants(pants_one)    
salesperson.sell_pants(pants_two)
salesperson.sell_pants(pants_three)

salesperson.display_sales()


# # Solution 
# 
# As a reminder, answers are also provided. If you click on the Jupyter icon, you can open a folder called 2.OOP_syntax_pants_practice, which contains this Jupyter notebook and a file called answer.py.
