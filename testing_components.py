from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/getToken/")
async def getToken(tenant_id: str, client_id:str, clientSecret: str):
    valid_tenantID="test"
    valid_clientID="test2"
    valid_clientSecret="secret"

    if valid_clientID == client_id and valid_tenantID == tenant_id and valid_clientSecret == clientSecret:
        return {"AccessToken":"FakeToken"}
    else:
        raise HTTPException(status_code=400,detail="Invalid clientID or tenantID or clientSecret")



    
