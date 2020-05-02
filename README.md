# Racipe app API

## ENDPOINTS
   
Authentication scheme works by token authentication
   
URL: {service}/users  
Users list and create operations  
  
method: GET  
action: list  
Success response    
   - Code: 200 OK    
   - Content: list of User objects  
     
method: POST  
action: create  
Success response  
   - Code: 201 Created    
   - Content: User object with properties    
      - id    
      - name    
      - firstname    
      - lastname  
        
URL: {service}/users/{id}  
  
method: GET    
action: retrieve  
Success response  
   - Code: 200 OK  
   - Content: User object  
Error response  
   - Code: 403 FORBIDDEN
  
method: PUT  
action: update  
Success reponse  
   - Code: 200 OK  
   - Content: updated User object  
Error response  
   - Code: 403 FORBIDDEN
           
method: PATCH  
action: partial update
Success reponse  
   - Code: 200 OK  
   - Content: updated User object 
Error response  
   - Code: 403 FORBIDDEN
          
method: DELETE  
action: destroy  
Success response  
   - Code: 204 NO CONTENT  
Error response  
   - Code: 403 FORBIDDEN
   
Available all ModelViewSet actions
URL: {service}/tags
URL: {service}/tags/{name}
  
URL: {service}/igredients
URL: {service}/igredients/{id}
   
Available additional action upload-images
URL: {service}/recipes
URL: {service}/recipes/{id}
URL: {service}/recipes/{id}/upload-images
   
    
    
    

