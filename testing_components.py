from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class TokenRequest (BaseModel):
    tenant_id:str
    client_id:str
    client_secret:str

app = FastAPI()

@app.post("/getToken/")
async def getToken(token_request: TokenRequest):
    valid_tenantID="test"
    valid_clientID="test2"
    valid_clientSecret="secret"

    if (valid_clientID == token_request.client_id and 
        valid_tenantID == token_request.tenant_id and
        valid_clientSecret == token_request.client_secret):
        return {"access_token":"FakeToken"}
    else:
        raise HTTPException(status_code=400,detail="Invalid clientID or tenantID or clientSecret")



    

    
