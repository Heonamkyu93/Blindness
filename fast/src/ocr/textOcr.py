from fastapi import FastAPI, WebSocket, APIRouter
import easyocr
import numpy as np
import cv2
import base64
from starlette.websockets import WebSocketDisconnect
import asyncio

app = FastAPI()
ocr_router = APIRouter(prefix="/ocr")

# Initialize the OCR reader with desired languages
reader = easyocr.Reader(['ko', 'en'])

@ocr_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Wait for the next image data from the client
            data = await websocket.receive_text()
            
            # Decode the base64 encoded image data
            img_data = base64.b64decode(data)
            nparr = np.frombuffer(img_data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # Process the image and extract text
            results = reader.readtext(img)
            extracted_texts = " ".join([text for _, text, _ in results])
            
            # Print the extracted texts to the server console for verification
            print("Extracted Texts:", extracted_texts)
            
            # Send the extracted text back to the client
            await websocket.send_text(extracted_texts)
            
            # Wait for 3 seconds before processing the next image
            await asyncio.sleep(3)
    except WebSocketDisconnect:
        print("Client disconnected")

# Include the OCR router in the FastAPI application
app.include_router(ocr_router)
