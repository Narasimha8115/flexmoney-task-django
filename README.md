# flexmoney-task-django


I have created a post api ,get api,view api ,update api using the django restframe work .
steps to integrate restframe work in django project 

--> "pip install djangorestframework"   in command line or in git bash

include 
'rest_framework',
in the django INSTALLED_APPS


The important note --> I have included cors headers to my django django project to access the api link form the reactJs port "http://localhost:3000/"

install using "pip install django-cors-headers"
and include "corsheaders.middleware.CorsMiddleware", above the 'django.middleware.common.CommonMiddleware', inside the MIDDLEWARE in django settings file.

This is the setup for api calling.

--->The Post api is ,


 ![Screenshot (1967)](https://user-images.githubusercontent.com/114894576/207409706-fd439f1e-31e9-4177-8664-ad527474d4b5.png)

for accesing this the link is   http://127.0.0.1:8000/create/


--->The Data is stored in the database using the api link like ,


![Screenshot (1966)](https://user-images.githubusercontent.com/114894576/207409965-3d9bc6c6-1eea-4f5b-9e78-e9f44888760c.png)


![Screenshot (1968)](https://user-images.githubusercontent.com/114894576/207409991-f0464036-af12-4070-ac7b-e72dcec03d73.png)

 
 
 
----> (**ER DIAGRAM**)
![photo_2022-12-13_23-35-07](https://user-images.githubusercontent.com/114894576/207410935-dbcdc384-bfdd-439c-81a6-84adfbf4d172.jpg)

There is two tables in this task one is for admission details and another one is for the payment details.

-->The entity realtion ship between this two tables is (**"one to many"**) ,The user has number of payments because they have to pay every month but the 
payment details belong to the onle on ID

I haven't taken a payment details into backend data base because of the mock payment i just developed if the required fields have given by user then user will automatically
popped up the "payment successful"

The "Email" and "phone number" and "id  in the admission table are "unique constraints"
The "id" is primary key in admission table and that "id is foreign key in the "payment_info" Table.

