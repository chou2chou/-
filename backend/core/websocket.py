from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from core.agent import AgentPipeline
from utils.asr_ocr import mock_asr_ocr

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, lesson_id: str):
        await websocket.accept()
        self.active_connections[lesson_id] = websocket

    def disconnect(self, lesson_id: str):
        self.active_connections.pop(lesson_id, None)

    async def send_data(self, lesson_id: str, data: dict):
        if lesson_id in self.active_connections:
            await self.active_connections[lesson_id].send_json(data)

manager = ConnectionManager()

@router.websocket("/ws/lesson/{lesson_id}")
async def websocket_lesson(websocket: WebSocket, lesson_id: str):
    await manager.connect(websocket, lesson_id)
    try:
        while True:
            data = await websocket.receive_json()
            audio = data.get("audio", "")
            board_img = data.get("board_img", "")

            raw_text = mock_asr_ocr(audio, board_img)
            result = AgentPipeline.run(raw_text)

            await manager.send_data(lesson_id, {
                "type": "lesson_stream",
                "subtitle": result["adapted_text"],
                "mind_map": result["mind_map"],
                "sign_script": result["sign_script"]
            })
    except WebSocketDisconnect:
        manager.disconnect(lesson_id)