
#            visit:        https://bankapiforlink.herokuapp.com/docs

from fastapi import FastAPI
from numpy import tile
from pydantic import BaseModel
import random as rnd

class Client(BaseModel):
    id:int
    cuit:int
    name:str
    ars_account_balance:float
    usd_account_balance:float

client_api=FastAPI(title="API for management of banks accounts", description="API para la administracion de cuentas bancarias",version=0.2)

clients=[]

@client_api.get("/")
async def root():
    return {"Message":"this is the root of API for management of banks accounts,please visit /docs"}

@client_api.post("/client")
async def create_a_new_client(client:Client):
    client.id=len(clients)
    clients.append(client.dict())
    return {"Message":"a new client has been received"}

@client_api.get("/random_client")
async def create_a_random_client():
    rnd_cuit=rnd.randint(0,60000000)
    rnd_name=rnd.choice(["Juan Domingo","Carlos Saul","Juan Manuel","Jorge Rafael","Julio Argentino","Maria Estela","Raul Ricardo","Juan Bautista","Domingo Faustino","Arturo Umberto"])
    rnd_account_balance=rnd.randint(0,100000)
    rnd_usd_account=rnd.randint(0,10000)
    client=Client(id=len(clients),cuit=rnd_cuit,name=rnd_name,ars_account_balance=rnd_account_balance,usd_account_balance=rnd_usd_account)
    clients.append(client.dict())
    return {"Message":"a new client called "+client.name+" with cuit Nº "+str(client.cuit)+" has been created"}
    
@client_api.get("/all_clients")
async def get_info_about_all_clients():
    return clients

@client_api.put("/put_ars_id/{id_to_put}")
async def put_ars_in_account(id_to_put:int,ars:float):
    if (id_to_put>len(clients)) or (id_to_put<0):
        return {"Message":"id not available, try another"}
    else:
        for client in clients:
            if client["id"]==id_to_put:
                client["ars_account_balance"]=client["ars_account_balance"]+ars
                return {"Message":"the ars_account_balance of "+ client["name"]+"has been increased "+str(ars)+" ars"}

@client_api.put("/put_usd_id/{id_to_put}")
async def put_usd_in_account(id_to_put:int,usd:float):
    if (id_to_put>len(clients)) or (id_to_put<0):
        return {"Message":"id not available, try another"}
    else:
        for client in clients:
            if client["id"]==id_to_put:
                client["usd_account_balance"]=client["usd_account_balance"]+usd
                return {"Message":"the usd_account_balance of "+ client["name"]+"has been increased "+str(usd)+" usd"}

@client_api.delete("/delete/{id_to_delete}")
async def delete_a_client(id_to_delete:int):
    if (id_to_delete>len(clients)) or (id_to_delete<0):
        return {"Message":"id out of range, try another"}
    else:
        for client in clients:
            if client["id"]==int(id_to_delete):
                clients.pop(id_to_delete) 
        for index,client in enumerate(clients):
            client["id"]=index
        return  {"Message":"the client with id Nº "+str(id_to_delete)+" has been deleted"}


@client_api.put("/put_ars_cuit/{cuit_to_put}")
async def put_ars_in_account_using_cuit(cuit_to_put,ars:float):
    if len(clients)>0:
        for client in clients:
            if client["cuit"]==int(cuit_to_put):
                client["ars_account_balance"]=client["ars_account_balance"]+ars
                return {"Message":"the ars_account_balance of "+ client["name"]+"has been increased "+str(ars)+" ars"}
    return {"Message":"cuit not available, try another"}
    
@client_api.put("/put_usd_cuit/{cuit_to_put}")
async def put_usd_in_account_using_cuit(cuit_to_put,usd:float):
    if len(clients)>0:
        for client in clients:
            if client["cuit"]==int(cuit_to_put):
                client["usd_account_balance"]=client["usd_account_balance"]+usd
                return {"Message":"the usd_account_balance of "+ client["name"]+"has been increased "+str(usd)+" usd"}
    return {"Message":"cuit not available, try another"}
               


       
                
    

            
                


            
       











