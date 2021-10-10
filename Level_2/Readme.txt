First install requirements!

Flask app web server that user can enter new data in main page.

if there is not any image file, then leave image path field empty. 
New data will be added to database.db file, not csv.

By appending /data you in url, you can access to all data in json format.

To filter them as it is said in task such as max_age, min_age, is_image_exists
just append /data?min_age=10&max_age=20 or /data?is_image_exists=True as an example.

It uses GET method to show and filter data. 


For manually adding new data in main page, it uses POST method. 

To use, just run app.py in console.