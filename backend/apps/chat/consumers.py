from djangochannelsrestframework.generics import GenericAsyncAPIConsumer


class ChatConsumer(GenericAsyncAPIConsumer):
    def __init__(self, *args, **kwargs):
        self.room_name = None
        self.group_name = None
        super().__init__(*args, **kwargs)

    async def connect(self):
        await self.accept()



