from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI(title="Plantty IoT API")

@app.get("/")
def read_root():
    return {"status": "ok", "system": "Plantty IoT Backend"}

# testowy endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Nowe połączenie WebSocket nawiązane!")
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Otrzymano dane: {data}")
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        print("Połączenie WebSocket zostało zamknięte.")
