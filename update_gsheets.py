from nanopool.api_calls import eth_nanopool
from gsheets.api_calls import gsheets_api

wallet = '' #insert wallet

updates = eth_nanopool(wallet)\
                .details().values.tolist()

gsheets_api()\
        .update_pool_info(updates)

