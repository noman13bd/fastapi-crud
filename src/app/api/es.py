import asyncio
import os
from elasticsearch import AsyncElasticsearch

from typing import List
from fastapi import APIRouter, HTTPException, Path

router = APIRouter()
cur_dir = (os.path.dirname(__file__))

print(cur_dir)
print(os.path.join(cur_dir,'ca.cert'))
es = AsyncElasticsearch(
        ["https://elastic:changeme@es01:9200"], 
        verify_certs=False
    )


@router.get("/")
async def read_all_notes():
    resp = await es.search (
        index="demo_index",
        body={"query": {"match_all": {}}},
        size=20,
    )
    print(resp)
    return {"test": "test"}


# async def main():
#     resp = await es.search(
#         index="documents",
#         body={"query": {"match_all": {}}}
#         size=20,
#     )
#     print(resp)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())