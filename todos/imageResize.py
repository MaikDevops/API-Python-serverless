import json
import os


def imageResize(event, context, callback):{

    # create a response
    const response = {
        "statusCode": 200,
        "body": json.stringify({
        message: 'v1.0',
     })  
    }

    callback(null, response)
    
   };