# -*- coding: utf-8 -*-
'''
(c) Copyright 2014 Telefonica, I+D. Printed in Spain (Europe). All Rights
Reserved.

The copyright to the software program(s) is property of Telefonica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefonica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
'''
locators = {}
locators["register.username"] = ("name", "username")
locators["register.password"] = ("id", "password")
locators["register.name"] = ("id", "name")
locators["register.email"] = ("id", "email")
locators["register.place"] = ("id", "place")
locators["register.submit"] = ("id", "registerButton")
locators["register.result.message"] = ("xpath", "//div[@id='content']/div/div/div/b[2]")
