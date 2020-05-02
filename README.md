# Racipe app API

## ENDPOINTS
   
Authentication scheme works by token authentication
   
Next endpoints provide all ModelViewSet actions  
**Users list and create**
URL: {service}/users  
  
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
  
**Retrieve, update and destroy User**
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
   
**List and create Tag object**  
URL: {service}/tags  
  
**Retrieve, update and destroy User**
URL: {service}/tags/{name}  
  
**List and create Tag object**  
URL: {service}/igredients  
  
**Retrieve, update and destroy User**
URL: {service}/igredients/{id}  
   
Provide additional action upload-images]
**List and create Tag object**  
URL: {service}/recipes  
  
**Retrieve, update and destroy User**
URL: {service}/recipes/{id}  
  
**Provide additional action upload-images**
URL: {service}/recipes/{id}/upload-images  
