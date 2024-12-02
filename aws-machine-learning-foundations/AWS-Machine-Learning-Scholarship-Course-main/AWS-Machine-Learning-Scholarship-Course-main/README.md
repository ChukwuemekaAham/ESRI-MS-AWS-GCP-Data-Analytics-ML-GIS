# AWS-Machine-Learning-Scholarship-Course
# What is the AWS Machine Learning Scholarship Program?
  AWS and Udacity are collaborating to educate developers of all skill levels to get started with ML. This scholarship is open to all applicants interested in expanding their       https://aws.amazon.com/machine-learning/ AWS ML expertise.

  In this dual scholarship program, all eligible students who complete the free https://www.udacity.com/scholarships/aws-machine-learning-scholarship-program AWS Machine Learning   Foundations course earn a course completion certificate from Udacity and have the opportunity to take a high-bar knowledge test.

# Practical Module & Excercise On Engineering Best Practices Part 1
   # Module 1 - Refactor: Wine Quality Analysis
    In this exercise, you'll refactor code that analyzes a wine quality dataset taken from the UCI Machine Learning Repository https://archive.ics.uci.edu/ml/datasets/wine+quality
    Each row contains data on a wine sample, including several physicochemical properties gathered from tests, as well as a quality rating evaluated by wine experts.
    The code in notebook/Python IDE first renames the columns of the dataset and then calculates some statistics on how some features may be related to quality ratings. Can you     refactor this code to make it more clean and modular?
   
  # Module 2 - Code Optimization: Common Books
    Here's the code your coworker wrote to find the common book ids in books_published_last_two_years.txt and all_coding_books.txt to obtain a list of recent coding books.
    Solution Tip #1: Use vector operations over loops when possible
    Use numpy's intersect1d method to get the intersection of the recent_books and coding_books arrays.
    
    Solution Tip #2: Know your data structures and which methods are faster
    Use the set's intersection method to get the common elements in recent_books and coding_books.
   
    Hint: Looks like using sets to compute the intersection is indeed most efficient in this case!
   
  # Module 3 - Optimizing Code: Holiday Gifts
    In the last example, you learned that using vectorized operations and more efficient data structures can optimize your code. Let's use these tips for one more example.
    
    Say your online gift store has one million users that each listed a gift on a wish list. You have the prices for each of these gifts stored in gift_costs.txt. 
    For the holidays,   you're going to give each customer their wish list gift for free if it is under 25 dollars. 
    Now, you want to calculate the total cost of all gifts under 25 dollars to see how much you'd spend on free gifts. 
  
 # Module 4 - Project Documentation
    Project documentation is essential for getting others to understand why and how your code is relevant to them, whether they are potentials users of your project or         developers who may contribute to your code. 
    A great first step in project documentation is your README file. It will often be the first interaction most users will have with   your project. 
    Here are a few READMEs from some popular projects:
    https://github.com/twbs/bootstrap
    https://github.com/scikit-learn/scikit-learn
    https://github.com/jjrunner/stackoverflow

# Practical Module & Excercise On Engineering Best Practices Part 2
   # Task/Module: Testing and Data Science, Test Driven Development and Data Science & Tips for Conducting a Code Review
    ```
    pip install -U pytest
    ```
    Then, to run pytest, just enter:
    ```
    pytest
    ```
    Right now, not all of the tests should pass. Fix the function to pass all its tests! Once all your tests pass, try writing some additional unit tests of your own!
 # Tips for Conducting a Code Review
    Now that we know what we are looking for, let's go over some tips on how to actually write your code review. 
    When your coworker finishes up some code that they want to merge to the team's code base, they might send it to you for review. 
    You provide feedback and suggestions, and then they may make changes and send it back to you. 
    When you are happy with the code, you approve and it gets merged to the team's code base.

    As you may have noticed, with code reviews you are now dealing with people, not just computers. 
    So it's important to be thoughtful of their ideas and efforts. 
    You are in a team and there will be differences in preferences. 
    The goal of code review isn't to make all code follow your personal preferences, but a standard of quality for the whole team.
    
   # Tip: Use a code linter
    This isn't really a tip for code review, but can save you lots of time from code review! 
    Using a Python code linter like pylint can automatically check for coding standards and PEP 8 guidelines for you! 
    It's also a good idea to agree on a style guide as a team to handle disagreements on code style, 
    whether that's an existing style guide or one you create together incrementally as a team.
    
  # Tip: Explain issues and make suggestions
    Rather than commanding people to change their code a specific way because it's better, 
    it will go a long way to explain to them the consequences of the current code and suggest changes to improve it. 
    They will be much more receptive to your feedback if they understand your thought process and are accepting recommendations, 
    rather than following commands. They also may have done it a certain way intentionally, and framing it as a suggestion promotes a constructive discussion, 
    rather than opposition 
    
  
# Practical Module & Excercis On OOP Syntax Practice - Part 1
# Use the Shirt Class
    You've seen what a class looks like and how to instantiate an object. Now it's your turn to write code that insantiates a shirt object.

# Explanation of the Code
    This Jupyter notebook is inside of a folder called 1.OOP_syntax_shirt_practice. 
    You can see the folder if you click on the "Jupyter" logo above the notebook. Inside the folder are three files:

    shirt_exercise.py, which your current file at
    answer.py containing answers to the exercise
    tests.py, tests for checking your code - you can run these tests using the last code cell at the bottom of this notebook

# Your Task
    The shirt_exercise.py file, which you are currently looking at if you are reading this, 
    has an exercise to help guide you through coding with an object in Python.


# Practical Module & Excercise On OOP Syntax Exercise - Part 2
    Now that you've had some practice instantiating objects, it's time to write your own class from scratch. 
    This lesson has two parts. In the first part, you'll write a Pants class. 
    This class is similar to the shirt class with a couple of changes. Then you'll practice instantiating Pants objects

    In the second part, you'll write another class called SalesPerson. You'll also instantiate objects for the SalesPerson.

    For this exercise, you can do all of your work in this Jupyter notebook. 
    You will not need to import the class because all of your code will be in this Jupyter notebook.

    Answers are also provided. If you click on the Jupyter icon, you can open a folder called 2.OOP_syntax_pants_practice, 
    which contains this Jupyter notebook ('exercise.py') and a file called answer.py.
   
# Pants class
    Write a Pants class with the following characteristics:

    the class name should be Pants
    the class attributes should include
    color
    waist_size
    length
    price
    the class should have an init function that initializes all of the attributes
    the class should have two methods
    change_price() a method to change the price attribute
    discount() to calculate a discount
    
# Gaussian Code Exercise
    Read through the code below and fill out the TODOs. You'll find a cell at the end of the Jupyter notebook/Python containing unit tests. 
    After you've run the code cell with the Gaussian class, you can run the final cell to check that your code functions as expected.

# Magic Methods
    Below you'll find the same code from the previous exercise except two more methods have been added: 
    an add method and a repr method. Your task is to fill out the code and get all of the unit tests to pass. 
    You'll find the code cell with the unit tests at the bottom of this Jupyter notebook.

    As in previous exercises, there is an answer key that you can look at if you get stuck. 
    Click on the "Jupyter" icon at the top of this notebook, and open the folder 4.OOP_code_magic_methods. 
    You'll find the answer.py file inside the folder.
    This exercise includes a file called 'numbers.txt', which you can see if you click on the 'Jupyter' 
    icon at the top of the workspace and then go into the folder titled 3.OOP_code_gaussian_class. 
    The 'numbers.txt' file is read in by the read_data_file() method. 
    There is also a solution in the 3.OOP_code_gaussian_class folder in a file called answer.py.
  
# Inheritance Exercise Clothing
    The following code contains a Clothing parent class and two children classes: Shirt and Pants.

    Your job is to code a class called Blouse. Read through the code and fill out the TODOs. 
    Then check your work with the unit tests at the bottom of the code.
  
# Exercise 1: Making a Package and Pip Installing, Exercise 2: Binomial Class, Exercise 3: Gaussian Class, & Exercise 4: Upload to PyPi
    Following the instructions from the previous video, convert the modularized code into a Python package. 

    You can put your code into the 3a_python_package folder in the workspace. Inside the 3a_python_package folder, you'll need to create a few folders and files:
    * a setup.py file, which is required in order to use pip install
    * a folder called 'distributions', which is the name of the Python package
    * inside the 'distributions' folder, you'll need the Gaussiandistribution.py file, Generaldistribution.py and an __init__.py file.

    Once everything is set up, open a new terminal window in the workspace by clicking 'NEW TERMINAL'. Then type:
    cd 3a_python_package.
