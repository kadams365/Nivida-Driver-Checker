# Nivida-Driver-Checker
I hate having extra things running in the background so this script will check if there is a new driver available. However, there being no clear API or way to check if there is a new version with out having Geforce or checking by hand. Nivida's website is also not able to be web scraped like the other 90% of the internet A window does have to be opened to run javascript on their site.

Main goal was to have this check when the user wants to check if there is a new driver. Make a task through task scheduler to run. 

Things to keep in mind:
Out of the box it will run a Firefox window (Can be changed to any browser).
Waiting for pages can be faster or slowed down depending on internet speed.
