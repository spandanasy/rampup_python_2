# ramp_up_python_2
## Task 1 Python
1. Implement the calculate_area function using function overloading in Python.
2. The function should accept one or more arguments, and its behavior should change depending on the number and types 
of arguments provided.
3. Specifically, it should support the following shapes: Rectangle: If two arguments (length and width) are provided, 
calculate and return the area of a rectangle. 
4. Circle: If one argument (radius) is provided, calculate and return the area of a circle. 
5. Triangle: If three arguments (base, height, and a string "triangle") are provided, calculate and return the area of a triangle using the formula (0.5 * base * height). Ensure that the function is designed to handle these different cases


* To achieve this task of python the concept of function overloading is used with the combination of math module and args** which takes variable length as its arguements and process the results.
* This program provides the result in the format of its Area and Shape name.
* As python does'nt support traditional functional overloading like other programming languages like c++ and JAVA a string triangle is used to return the area of triangle.
* The input by the user should be in this format
        -> Circle   3
        -> Rectangle    2,3
        -> Triangle     2,3,triangle
* Exception handling is used to handle exceptions when the user had specified more number of of arguements rather than the required number of arguments, and also to handle exception when user has entered any other values rather then the number.

## Task 2 Python
1. generate unique usernames for any social media platform. In this scenario, the generator will yield unique usernames one by one.
2. Generate a random username consisting of letters and numbers.
3. Ensure the generated username is unique.

* This program generates a different usernames using random and string modules to get access to the ASCII values od alphabets and digits.Here I'm also using generator function to generate usernames one by one using yeild and next keyword.
* The program returns a set containing unique usernames one by one when user press enter it produces another username which is specified in the while loop.

## Task 3 Python
1. Using Regular Expression extract email addresses from a text document, such as an email log or a text file containing email correspondence.
* To evaluate this task the re module is used that operates on finding the match of regular expresions.
* The file is accessed from the device locally so file functions and modes are used to access files.
* This returns all the valid email addresses from the text file.

## Task 4 Python
1. Use inheritance concept.
2. Imagine you are managing a software development team at a xyz company. You have a mix of managers and developers on your team.
3. You use a Python program to maintain employee records, and you've defined two classes, Manager and Developer  which inherit from the base class Employee.
* Using the concept of inheritance the manager and developer details are printed using hierachial inheritance.
* The data is accesed using the manager and developer id , So classmethod decorator is used to access the profiles. 
