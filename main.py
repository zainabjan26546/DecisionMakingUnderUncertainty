#!/usr/bin/env python
# coding: utf-8

# In[118]:


import pandas as pd
import Algorithm


def ReadFile(filename):
    data = open(filename, "r")
    rows = data.readlines()
    Dataset1 = []
    for i in range(0, len(rows)):
        Dataset1.append(rows[i].split())

    states = Dataset1[0][1:]
    alternatives = []
    Matrix = []
    for j in range(1, len(Dataset1)):
        matrix = []
        for k in range(0, len(Dataset1[j])):
            if k == 0:
                alternatives.append(Dataset1[j][k])
            else:
                matrix.append(int(Dataset1[j][k]))
        Matrix.append(matrix)
    return Matrix, alternatives, states


# In[119]:


def Input_payoff_matrix():
    try:
        Events = []
        Alternatives = []
        data = []
        nevents = int(input("please input number of events: "))
        nalternatives = int(input("please input number of alternatives: "))
        for i in range(0, nevents):
            m = input("Please Enter event : ")
            Events.append(m)

        for i in range(0, nalternatives):
            n = input("Please Enter Alternatives : ")
            Alternatives.append(n)

        for k in range(0, len(Alternatives)):
            lis = []
            for h in range(0, len(Events)):
                print("please enter data for " + Events[h] + "  " + Alternatives[k])
                payoff = input(" ")
                lis.append(int(payoff))
            data.append(lis)
        return Events, Alternatives, data
    except:
        print("Invalid Input!  ")


# In[120]:


def Input_likelihood_matrix():
    try:
        Events = []
        Alternatives = []
        data = []
        nevents = int(input("please input number of events: "))
        nalternatives = int(input("please input number of alternatives: "))
        for i in range(0, nevents):
            m = input("Please Enter event : ")
            Events.append(m)

        for i in range(0, nalternatives):
            n = input("Please Enter Alternatives : ")
            Alternatives.append(n)

        for k in range(0, len(Alternatives)):
            lis = []
            for h in range(0, len(Events)):
                print("please enter Likelihood  for " + Events[h] + "  " + Alternatives[k])
                payoff = input(" ")
                lis.append(int(payoff))
            data.append(lis)
        return Events, Alternatives, data
    except:
        print("Invalid Input!  ")


# In[121]:


def Select_Rules(Matrix, alternatives, states):
    print("                   Please Select a Rule: ")
    print("                    1) Ranking with TOPSIS")
    print("                    2) Minimax Regret")
    print("                    3)  Maximax         ")
    print("                    4) Maximin")
    print("                    5) Hurwicz")
    print("                    6) Laplace        ")
    print("                    7) Exit!      ")
    choice = input("please enter choice: ")
    while choice != '7':
        obj = Algorithm.Decision_Algorithm()
        if choice == "1":
            try:
                obj.Rankwithtopsis(Matrix, alternatives, states)
            except:
                print("Sorry Invalid data for this method")
        elif choice == "2":
            obj.minimax_regret(Matrix, alternatives, states)
        elif choice == "3":
            obj.maximax(Matrix, alternatives, states)
        elif choice == "4":
            obj.maximin(Matrix, alternatives, states)
        elif choice == "5":
            obj.hurwicz(Matrix, alternatives, states)
        elif choice == "6":
            obj.laplace(Matrix, alternatives, states)
        else:
            print("Invalid output")
        print("                   Please Select a Rule: ")
        print("                    1) Ranking with TOPSIS")
        print("                    2) Minimax Regret")
        print("                    3)  Maximax         ")
        print("                    4) Maximin")
        print("                    5) Hurwicz")
        print("                    6) Laplace        ")
        print("                    7) Exit!      ")
        choice = input("please enter choice: ")


# In[122]:


def data_analysis_menu():
    print("                    Please select a Option from Menu   ")
    print("                    a) Input new payoff matrix")
    print("                    b) Enter the Likelihood of Events! ")
    print("                    c) Selection Rules         ")
    print("                    d) Exit")
    choice = input("please enter choice : ")
    flag = 0
    while choice != "d":
        if choice == "a":
            Events, Alternatives, data = Input_payoff_matrix()
            obj1 = Algorithm.Decision_Algorithm()
            obj1.add(data, Alternatives, Events)
            flag = 1
        elif choice == "b":
            Events, Alternatives, data = Input_likelihood_matrix()
            obj2 = Algorithm.Decision_Algorithm()
            obj2.add(data, Alternatives, Events)
            flag = 2
        elif choice == "c":
            if flag == 1:
                Select_Rules(obj1.Matrix, obj1.alternatives, obj1.states)
            elif flag == 2:
                Select_Rules(obj2.Matrix, obj2.alternatives, obj2.states)
            else:
                Matrix, alternatives, states = ReadFile("data.txt")
        else:
            print("Invalid choice")
        print("                    Please select a Option from Menu   ")
        print("                    a) Input new payoff matrix")
        print("                    b) Enter the Likelihood of Events! ")
        print("                    c) Selection Rules         ")
        print("                    d) Exit")
        choice = input("please enter choice : ")


# In[129]:


def generate_report():
    print("                             ")
    print("                1) Generate Report from Database")
    print("                2) Input likelihood matrix")
    print("                3) Input Payoff Matrix")
    print("                4) exit")
    choice = input("please enter choice:  ")
    while choice != "4":
        flag = 0
        if choice == "1":
            Matrix, alternatives, states = ReadFile("Data/data.txt")
            obj = Algorithm.Decision_Algorithm()
            obj.add(Matrix, alternatives, states)
            try:
                obj.Rankwithtopsis(Matrix, alternatives, states)
            except:
                pass
            print("  ")
            obj.minimax_regret(Matrix, alternatives, states)
            print("  ")
            obj.maximax(Matrix, alternatives, states)
            print(" ")
            obj.maximin(Matrix, alternatives, states)
            print(" ")
            obj.hurwicz(Matrix, alternatives, states)
            print(" ")
            obj.laplace(Matrix, alternatives, states)
        elif choice == "2":
            states, alternatives, Matrix = Input_payoff_matrix()
            obj = Algorithm.Decision_Algorithm()
            obj.add(Matrix, alternatives, states)
            try:
                obj.Rankwithtopsis(Matrix, alternatives, states)
            except:
                pass
            print("  ")
            obj.minimax_regret(Matrix, alternatives, states)
            print("  ")
            obj.maximax(Matrix, alternatives, states)
            print(" ")
            obj.maximin(Matrix, alternatives, states)
            print(" ")
            obj.hurwicz(Matrix, alternatives, states)
            print(" ")
            obj.laplace(Matrix, alternatives, states)
        elif choice == "3":
            states, alternatives, Matrix = Input_likelihood_matrix()
            obj = Algorithm.Decision_Algorithm()
            obj.add(Matrix, alternatives, states)
            try:
                try:
                    obj.Rankwithtopsis(Matrix, alternatives, states)
                except:
                    pass
                print("  ")
                obj.minimax_regret(Matrix, alternatives, states)
                print("  ")
                obj.maximax(Matrix, alternatives, states)
                print(" ")
                obj.maximin(Matrix, alternatives, states)
                print(" ")
                obj.hurwicz(Matrix, alternatives, states)
                print(" ")
                obj.laplace(Matrix, alternatives, states)
            except:
                print("Invalid input")
        else:
            print("Invalid Input")
        print("                1) Generate Report from Database")
        print("                2) Input likelihood matrix")
        print("                3) Input Payoff Matrix")
        print("                4) exit")
        choice = input("please enter choice:  ")


# In[130]:


## print("                    Welcome to this Application             ")
print("                    Please select a Option from Menu   ")
print("                    1) Data Analysis Menu")
print("                    2) Report Generation for all Methods! ")
print("                    3) Exit")
choice = input("Please enter choice: ")
while choice != "3":
    if choice == "1":
        data_analysis_menu()
    elif choice == "2":
        generate_report()
    print("                    Welcome to this Application             ")
    print("                    Please select a Option from Menu   ")
    print("                    1) Data Analysis Menu")
    print("                    2) Report Generation for all Methods! ")
    print("                    3) Exit")
    choice = input("Please enter choice: ")

# In[ ]:




