# RecipeGenerator
In order to run, you will need to create your own consts.py file that contains the necessary constants to be imported (I did not add mine for security reasons, but contact me if you are having trouble figuring out what numbers are which).

You will need to create a Twilio account and register your cell phone number on Twilio in order for the texting portion to work. Specific directions on how to do so can be found on the Twilio website or on the website for Automate the Boring Stuff with Python Chapter 16.

Hate that feeling when you someone asks you what you want for dinner some night this week? Well worry no more with this Recipe Generator!!

This script is designed to generate a pseudo-random recipe from allrecipes.com. When the script is run, the homepage is obtained using requests and a list of scraped a from the html code, which can later be used to gather the hrefs from
the list. 

Based on this easily readable lxml, all the urls for a genre of food are accumulated into a list and one is randomly  selected.

From this genre of food, another collection of urls is  initialized containing the urls of individual recipes. From this list of urls, a random recipe url is chosen and  returned.

Finally, the individual recipe url is opened and the necessary information for the recipe (such as the title, the time, the servings, the ingredients, and the directions) is scraped from the website and compiled into a string. 

With this string, at least one of three methods can be executed: writeRecipe(), sendText(), or sendMail(). Each option is described in detail in the methods docstring.