import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="ctn-uriage",
                               connection="snowpipeuriagecsvstorage_STORAGE") 
def afunc_kaitori(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
    file = myblob.read()
    logging.info(f"File Content: {file}")