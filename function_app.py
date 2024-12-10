import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="mycontainer/ctn-kaitori",
                               connection="Connection_String",
                               source="EventGrid") 
def BlobTriggerEventGrid(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")

    file = myblob.read()
    logging.info(f"File Content: {file}")
