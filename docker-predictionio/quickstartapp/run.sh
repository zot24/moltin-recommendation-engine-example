#!/bin/bash
set -e

if [ ! -f /.dockerenv ]; then
  echo "*** NOTICE: Make sure you're running this from inside the Docker container! ***"
  exit 1
fi


echo "Step 1: Making sure everything is running"
sv start /etc/service/*

echo "EventServer may take a minute to start..."
until curl http://localhost:7070; do echo "waiting for EventServer to come online..."; sleep 3; done

pio status
echo "Step 1: Passed"


echo "Step 2. Create a new Engine from an Engine Template"

# echo "n" | git clone https://github.com/apache/incubator-predictionio-template-ecom-recommender.git MyECommerceRecommendation
cd MyECommerceRecommendation

echo "Step 2: Passed"


echo "Step 3. Generate an App ID and Access Key"

echo "YES" | pio app delete moltinRecommendation
pio app new moltinRecommendation --access-key aFI4EfJJXc5W03ymMgqHWVAdV2VQN9ej5_WmMW_jWmMferm9n102SCQw0XYOXNsS

pio app list
echo "Step 3: Passed"

echo "Step 4 Import Sample Data"

python /quickstartapp/import_eventserver.py --access_key aFI4EfJJXc5W03ymMgqHWVAdV2VQN9ej5_WmMW_jWmMferm9n102SCQw0XYOXNsS

echo "Step 4: Passed"

echo "Step 5. Deploy the Engine as a Service"
sed -i "s|INVALID_APP_NAME|moltinRecommendation|" /quickstartapp/MyECommerceRecommendation/engine.json

echo "Building...  It may take some time to download all the libraries."
pio build --verbose

echo "Training..."
pio train

echo "You may now deploy engine by running: cd /quickstartapp/MyECommerceRecommendation && pio deploy --ip 0.0.0.0&"
echo "Sample REST call: curl -H \"Content-Type: application/json\" -d '{ \"user\": \"1\", \"num\": 4 }' http://localhost:8000/queries.json|jq"
