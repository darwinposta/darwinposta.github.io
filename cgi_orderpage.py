#!/usr/bin/python3

import cgi, cgitb 


form = cgi.FieldStorage() 


name = form.getvalue('name')
address = form.getvalue('address')
email = form.getvalue('email')
city = form.getvalue('city')
state = form.getvalue("state")
zipcode = form.getvalue("zipcode")
item = form.getvalue("item")
shipday = form.getvalue("freeDay")




print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<link rel='stylesheet' type='text/css' href='main.css'>")
print ('<head>')
print ("<title>Darwin's Tech Marketplace</title>")
print ('<meta charset="utf-8">')
print ("</head>")
print ('<header class="header">')
print ('<h1 class="logo"><a href="index.html">Darwins Tech Marketplace</a></h1>')
print ('<ul class="main-nav">')
print ('<li><a href="index.html">Home</a></li>')
print ('<li><a href="orderpage.html">Giveaway</a></li>')
print ('<li><a href="#">Portfolio</a></li>')
print ('<li><a href="#">Contact</a></li>')
print ('<li><div class="dropdown">')
print ('<button class="dropbtn">Products</button>')
print ('<div class="dropdown-content">')
print ('<a href="#">Link 1</a>')
print ('<a href="#">Link 2</a>')
print ('<a href="#">Link 3</a>')
print ('</div>')
print ('</div>')
print ('</li>')
print ('</ul>')
print ('</header>')

print ("<body>")
print ("<h2>Hello %s</h2>" % (name))
print ("<p1>Your entry for the %s giveaway has been received and you will be notified at %s.</p1>" % (item, email))
print ("</body>")
print ("</html>")
    


  




      
      
      
      
      
            
            
              
              
              
            
          
        
      
  
