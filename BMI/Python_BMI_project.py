#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

# In[59]:


def bmi_cal(bmi):
    if bmi <= 16:
        print('Severely Underweight')
    elif bmi <= 18:
        print('Underweight')
    elif bmi <= 24.9:
        print('Normal')
    elif bmi <= 29.9:
        print('Overweight')
    elif bmi <= 34.9:
        print('Moderately Obese')
    elif bmi <= 39.9:
        print('Severely Obese')
    else:
        print('Morbidly Obese')


# In[60]:


weight = int(input('Input your weight in kgs. :'))
height1 = int(input('Input your height 1st in ft. :'))
height2 = int(input('Input your height then in inches :'))
Inches1 =  height1 * 12
height_cm = (Inches1 + height2) *0.0254
bmi= weight /(height_cm * height_cm)
print('Your Weight is '+ str(weight) + ' and your height in is ' + str(height1) +"'"+str(height2) )
print('Your BMI is ' + str(bmi) + ' and you are ')
bmi_cal(bmi)


# In[ ]:




