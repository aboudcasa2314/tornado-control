# Omega Zero – Integrated Core 🖤
# Unified backend and frontend communication

import asyncio
import websockets
import json
from datetime import datetime
import random

# ---------------- Backend Core ---------------- #
class BlackVoidCore:
    def __init__(self):
        self.active_session = False
        self.market_data = {}
        self.success_rate_threshold = 99.99

    async def connect_to_client(self, websocket):
        print("🖤 Connected to frontend successfully!")
        self.active_session = True
        await self.listen_and_process(websocket)

    async def listen_and_process(self, websocket):
        while self.active_session:
            try:
                # Simulate sending data to frontend
                raw_data = {
                    "timestamp": datetime.utcnow().isoformat(),
                    "signal": random.choice(["BUY", "SELL", "HOLD"]),
                    "success": random.uniform(99.0, 100.0)
                }
                await websocket.send(json.dumps(raw_data))
                print(f"[📡 Data Sent]: {raw_data}")
                await asyncio.sleep(2)  # Send every 2 seconds
            except Exception as e:
                print(f"[⚠️ Error]: {e}")
                break

# ---------------- WebSocket Server ---------------- #
async def start_server():
    print("🖤 Omega Zero Backend Starting...")
    core = BlackVoidCore()
    async with websockets.serve(core.connect_to_client, "0.0.0.0", 8765):
        print("✅ Backend is ready and listening on port 8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    try:
        asyncio.run(start_server())
    except KeyboardInterrupt:
        print("\n🔌 Server stopped manually.")
