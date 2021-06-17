from nanopool.api_calls import eth_nanopool
from gsheets.api_calls import gsheets_api

wallet = '0x56d890f48b0ce7860d5511432a970c47e7bcdf53'

updates = eth_nanopool(wallet)\
                .details().values.tolist()

gsheets_api()\
        .update_pool_info(updates)

