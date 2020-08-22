import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

CONNECTION_STR = "Endpoint=sb://sk-event-hub-namespace.servicebus.windows.net/;SharedAccessKeyName=sk-event-hub-namespace-policy;SharedAccessKey=sFC77k1lV0jOW3Ji2FI7hOtN4RoNobDkwcVMo/X5KBY="
EVENT_HUB_NAME = "sk-event-hub"

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
 	    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(conn_str=CONNECTION_STR, eventhub_name=EVENT_HUB_NAME)
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData('{"a":"cddf"}'))


        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())