from fastapi import FastAPI
from pydantic import BaseModel, Field
import asyncio_mqtt as aiomqtt
import paho.mqtt as mqtt
import os

app = FastAPI(title='LED Pager Notify', version='0.0.1')

class Notification(BaseModel):
    id: str
    flag: int

@app.post("/notifications", status_code=201)
async def add_notification(n: Notification):
    async with aiomqtt.Client(
        hostname=os.getenv('MQTT_HOST', '127.0.0.1'),
        port=int(os.getenv('MQTT_PORT', '1883')),
        username=os.getenv('MQTT_USERNAME'),
        password=os.getenv('MQTT_PASSWORD'),
    ) as c:
        await c.publish(os.getenv('MQTT_TOPIC', 'test'), payload=n.flag, qos=1, retain=True)

    return n
