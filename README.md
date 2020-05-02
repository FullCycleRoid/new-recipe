# Racipe app API

## ENDPOINTS
   
   Authentication scheme works by token authentication
   
   - {service}/users
      Users list and create operations  
        
      method: GET  
      action: list  
      Success response    
          Code: 200 OK    
          Content: list of User objects  
     
      method: POST  
      action: create  
      Success response  
          Code: 201 Created    
          Content: User object with properties    
              id    
              name    
              firstname    
              lastname  
        
  - {service}/users/{id}  
      method: GET    
      action: retrieve  
      Success response  
         Code: 200 OK  
         Content: User object  
      Error response  
         Code: 403 FORBIDDEN
        
      method: PUT  
      action: update  
      Success reponse  
         Code: 200 OK  
         Content: updated User object  
      Error response  
         Code: 403 FORBIDDEN
           
      method: PATCH  
      action: partial update
      Success reponse  
         Code: 200 OK  
         Content: updated User object 
      Error response  
         Code: 403 FORBIDDEN
          
      method: DELETE  
      action: destroy  
      Success response  
         Code: 204 NO CONTENT  
      Error response  
         Code: 403 FORBIDDEN
   
  Available all ModelViewSet actions
  - {service}/tags
  - {service}/tags/{name}
  
  - {service}/igredients
  - {service}/igredients/{id}
   
  Available additional action upload-images
  - {service}/recipes
  - {service}/recipes/{id}
  - {service}/recipes/{id}/upload-images
   
    
    
    

