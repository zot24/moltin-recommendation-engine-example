"""
Import sample data for E-Commerce Recommendation Engine Template
"""

import predictionio
import argparse
import random
import uuid

SEED = 3

def import_events(client):
  random.seed(SEED)
  count = 0
  print(client.get_status())
  print("Importing data...")

  user_ids = ["1ca5b99a-ef88-4959-92e0-86cde3b8fc26", str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())]
  #user_ids = ["1ca5b99a-ef88-4959-92e0-86cde3b8fc26"]
  for user_id in user_ids:
    print("Set user", user_id)
    client.create_event(
      event="$set",
      entity_type="user",
      entity_id=user_id
    )
    count += 1

  # TODO: get this data from moltin's API
  # TODO: use categories data from moltin's API
  categories = ["c%s" % i for i in range(1, 7)]
  item_ids = [
    "6837058c-ae42-46db-b3c6-7f01e0c34b40",
    "a3e3c529-1027-4ace-b56c-9f93feda9185",
    "9e88dc21-4e5a-40a0-a12c-51e2f5e47bdf",
    "7ba0e32a-80d3-4319-9993-f9756a303fd3",
    "75fbeab0-75a3-4d6b-b23b-9db7455c077e",
    "dbeaabb8-3d02-4ec7-84e9-bc36a633bd0b",
    "0747e1a5-d214-4ff3-ab50-afc067ea87b0",
    "bd07d48b-b3cb-4c22-ba13-6c88029d0035",
    "b7f8d48b-d786-4105-bb7b-89b48b0a5cf8",
    "590385fe-4f19-404a-8824-b74c8874c0e5",
    "e0c62dbc-8f3a-4f58-8f83-d8d994e1080c",
    "9f0ad06a-b4ec-493a-8a37-ee709ad4834f",
    "2345c60c-2f9a-4135-85ce-bbd52000bca6",
    "57ae653b-e46b-4e5c-9125-d6da0c026c2d",
    "1ada5797-b6be-403f-8191-71dc0a17c80a",
    "9c0103a4-df5a-4d86-9c7a-290f446d8483",
    "4925e5f7-8120-4a2a-8307-d36aadd4778c",
    "4ef2b7ed-3ac9-4f18-ba98-6cad2f10c276",
    "9f496b96-0400-4cc6-a9dc-eff57d22a443",
    "1baa3301-de89-4f78-914c-c65590fbd858",
    "e06b032a-2a99-4d72-bf5e-137841a877e3",
    "249d262a-94a8-4b10-beff-9dbd7509faa8",
    "456b32eb-25f2-4b79-a731-13b1f55b6f1d",
    "ccea94fe-ceda-4dbe-80ec-1f238f74d9bf",
    "e8ca08ba-f3f8-43e6-bdad-03e31f06882e",
    "33917eab-de64-4ff4-94ac-ce4ed5ad370b",
    "ee5ed600-cab7-4e56-8c76-7ec12e248203",
    "c2fae67c-850d-43ee-8c36-d07ec1c9f61f",
    "bce835d0-d8f8-4eda-b3a0-418408667f3c",
    "6859195c-606c-4a67-a171-2d4e58ce6d48",
    "f1fbabce-a440-4d06-8593-76f946bd6bfb",
    "f88d0fe7-d6e1-434a-99b0-1ac82613c1b1",
    "90ddfe7c-bc3a-42f9-ac3d-23784acaffb4",
    "66e435f8-df34-4d92-a080-602b3902152e",
    "7a471409-cd31-4d94-9de1-06f815510cb8",
    "16276490-daa1-4cce-a854-b71c95d9b45b",
    "38d8c968-1902-4314-bbc1-9444ff96c574",
    "5f73da11-77dc-43f7-9e46-4822dcfffe13",
    "1548a0ed-2e8f-4186-82df-5925664e5064",
    "6f8a2976-6e26-4174-a447-e0a53aa041dd",
    "524d7358-2353-40ec-bd28-cc82807f1bf4",
    "f58ff42e-777a-491f-abe2-e7d04c198e22",
    "91b449c9-6aa7-4382-b8f9-bb716f63f728",
    "4397bb06-82d4-47b7-b8b8-647e88d1967d",
    "0b48b027-0055-4a7f-9fa6-96415cee2d3a",
    "15c6fb1a-a99a-47bb-ab3b-661bfdc8a910",
    "1fe3ef0e-8dcc-4d33-b831-7e2ee3b8748f",
    "a8e030af-69a3-416e-9c48-245dbd64dda0",
    "12a99cc5-3fee-4314-ad06-de18959fbae9",
    "bc006246-969d-49e1-b2ec-b3fc954c55f1"
  ]
  for item_id in item_ids:
    print("Set item", item_id)
    client.create_event(
      event="$set",
      entity_type="item",
      entity_id=item_id,
      properties={
        "categories" : random.sample(categories, random.randint(1, 4))
      }
    )
    count += 1

  # each user randomly viewed 10 items
  for user_id in user_ids:
    for viewed_item in random.sample(item_ids, 10):
      print("User", user_id ,"views item", viewed_item)
      client.create_event(
        event="view",
        entity_type="user",
        entity_id=user_id,
        target_entity_type="item",
        target_entity_id=viewed_item
      )
      count += 1
      # randomly buy some of the viewed items
      if random.choice([True, False]):
        print("User", user_id ,"buys item", viewed_item)
        client.create_event(
          event="buy",
          entity_type="user",
          entity_id=user_id,
          target_entity_type="item",
          target_entity_id=viewed_item
        )
        count += 1

  print("%s events are imported." % count)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="Import sample data for e-commerce recommendation engine")
  parser.add_argument('--access_key', default='invald_access_key')
  parser.add_argument('--url', default="http://localhost:7070")

  args = parser.parse_args()
  print(args)

  client = predictionio.EventClient(
    access_key=args.access_key,
    url=args.url,
    threads=5,
    qsize=500)
  import_events(client)