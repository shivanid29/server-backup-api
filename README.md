# Generating a compressed backup file (zip/tar)


This API helps in taking backup of the mentioned path present on the server. Have used Flask Framework for API and Paramiko module to connect to the server via SSH.



#Requirements
* Clone the repo
* Install python packages by running the requirements.txt file as:
  pip install requirements.txt ( Use pip3 if you are using pip3)

#Running the tests

1 Run the app.py file  
2 Pass the server details as query parameters, details like:
* host (IP address of the server)
* user_name 
* password to the server
* folder_name (the folder under /home/user_name for which backup is needed to be taken)
* file_name (mention the file name that you wish to save without any extension for eg: test, this will save the file as test.zip/test.tar at the end)
* file_format (mention the file format that you wish to get the backup in , there are 2 options: 'zip' or 'tar')

#Notes

* You can refer to the below sample API request and response.

Sample API call:
```ruby
curl --location --request POST 'http://127.0.0.1:5000/create-backup?host=<server_IP>&user_name=<username>&password=<password_to_the_server>&folder_name=</public_html/shivani-test>&file_name=<checking>&file_format=<zip>'
```
Sample API response:
```ruby
{
    "status": "success",
    "path": "server_IP/wikitjqd/checking.zip",
    "file_name": "checking.zip"
}
```
Response status:
```ruby
200
```