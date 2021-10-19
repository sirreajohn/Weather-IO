# Weather-IO
A simple Flask application to display various weather details on a webpage

Packages used:
  - flask
  - ip2geotools
  - darksky
  
To-do list:
  - [x] gurnicorn implementation
  - [ ] host it somewhere(heroku)
  - [ ] make UI more intuitive
  - [X] relax
## dev_NOTES
since flask uses local server...change the ip value to call ipad() function before implementing or expect errors 

before
```
   ip = '192.165.13.2' #some random ip
```
after
```
  ip = ipad() #funtion to get real ip of client
```
## Collaborators
---
- Tarakeswar Nallamothu
- Mahesh Patapalli 
- Koushik Gajjala
