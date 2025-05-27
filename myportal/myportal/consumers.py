import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ReviewConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("reviews", self.channel_name)
        print("WebSocket connected")
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("reviews", self.channel_name)

    async def new_review(self, event):
        review_html = event['review_html']
        await self.send(text_data=json.dumps({
            'review_html': review_html
        }))
