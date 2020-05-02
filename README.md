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
  
**Retrieve, update and destroy user object**  
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
method: GET  
action: list  
Success response    
   - Code: 200 OK    
   - Content: list of Tag objects  
  
**Retrieve, update and destroy Tag**  
URL: {service}/tags/{name}  
method: GET    
action: retrieve  
Success response  
   - Code: 200 OK  
   - Content: Tag object    
Error response    
   - Code: 403 FORBIDDEN
  
method: PUT  
action: update  
Success reponse  
   - Code: 200 OK  
   - Content: updated Tag object      
Error response  
   - Code: 403 FORBIDDEN
           
method: PATCH  
action: partial update
Success reponse  
   - Code: 200 OK  
   - Content: updated Tag object   
Error response  
   - Code: 403 FORBIDDEN
          
method: DELETE  
action: destroy  
Success response  
   - Code: 204 NO CONTENT    
Error response  
   - Code: 403 FORBIDDEN
  
**List and create ingredients object**  
URL: {service}/igredients  
method: GET  
action: list  
Success response    
   - Code: 200 OK    
   - Content: list of igredients objects  
  
**Retrieve, update and destroy ingredient**  
URL: {service}/igredients/{id} 
    
**List and create recipe object**  
URL: {service}/recipes  
method: GET  
action: list  
Success response    
   - Code: 200 OK    
   - Content: list of recipe objects  
   
**Retrieve, update and destroy recipe object**  
URL: {service}/recipes/{id}  
method: GET    
action: retrieve  
Success response  
   - Code: 200 OK  
   - Content: recipe object    
Error response  
   - Code: 403 FORBIDDEN
  
method: PUT  
action: update  
Success reponse  
   - Code: 200 OK  
   - Content: updated recipe object    
Error response    
   - Code: 403 FORBIDDEN
           
method: PATCH  
action: partial update
Success reponse  
   - Code: 200 OK  
   - Content: updated recipe object   
Error response    
   - Code: 403 FORBIDDEN
          
method: DELETE  
action: destroy  
Success response  
   - Code: 204 NO CONTENT    
Error response    
   - Code: 403 FORBIDDEN
    
**Provide additional upload-images action**  
URL: {service}/recipes/{id}/upload-images  
