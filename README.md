# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author

Divjot Kaur

## Assignment

Assignment 01: [Indicate the name and description of the current assignment]

Assignment 2: Object Oriented Design includes the use of Abstraction, Inheritance and Polymorphism concepts on the BankAccount class which is the superclass from where more subclasses are defined. This assignemnt also contains unit testing that though limits to verify the expected polymorphic behavior.

Assignment 03: The name of the current assignment is Design Patterns.

## Polymorphism

Polymorphism was acheived in the BankAccount class when the get_service_charges(self) function was being used. In every subclass of BankAccount class whether it was ChequingAccount, SavingsAccount or InvestmentAccount, each time the way in which the function was working varied.

## Strategy Pattern

The Strategy pattern has been used to define the attributes of the ServiceChargeStrategy class that contains various other components linked together. 

## Observer Pattern

The Observer pattern has been used to create a list of all the observers and perform attach, detach and notify features on the account types and alert them with ALERT messages if needed while storing all the data in a .txt file.

## Event-Driven Programming Paradigm

In this project, I used codes related to the Event Driven Programming Paradigm whereby I was managing Event Handling, Signals and dialog boxes which were possible with the help of the PySide6 package. I began with the load_data function and then update_data through which I was able to interact with the client data and their bank account information present in the csv files provided. Further,  I developed codes that would enable a user to look up for their account using their client number and can perform features liek any deposit and withdrawal. A little crucial part was how the balance would be updated after any transaction, but after giving it time and understanding the notes, I was able to make it work. The last thing was the signal management that allowed each part of codes from different functions to work together as an when a transaction or any task is being done.
