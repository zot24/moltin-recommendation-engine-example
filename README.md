Hackaton 8th September 2017 - E-Commerce Recommendation Engine
---

Basic recommendation engine example, using [moltin's API](https://www.moltin.com) and [PredictionIO Machine Learning Server](http://predictionio.incubator.apache.org):

- Recommend popular items, base on `view` and `buy` events
- Provide recommendation to new users who sign up after the model is trained

# Setup

## Prepare the recommendation engine
 
### Start the event server

1. `cd docker-predictionio`
2. build base image by running `./build`
3. start the container by running `./shell`
4. start `predictionio` dependencies (dashboard, eventserver, elasticsearch, hbase) by running `runsvdir-start&`
5. check dashboard is live by opening `http://localhost:9000/`
6. check event server is live by opening `http://localhost:7070`

### Build and train the engine as a service

7. `cd quickstartapp`
8. build, inject fake data and train the engine by running `./run.sh`

### Deploy the engine as a service

9. `cd /quickstartapp/MyECommerceRecommendation && pio deploy --ip 0.0.0.0&`
10. check you can access the engine service data opening 

## Prepare the example web app

1. CORS will be a problem so open Google Chrome with the following command `/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --disable-web-security --user-data-dir`
2. Open (drag&drop) `index.html` into Chrome

# Usage

1. Web example: it's self explanatory
2. HTTPie example: execute the scripts

> Note: You could try the same process with other engines from the gallery http://predictionio.incubator.apache.org/gallery/template-gallery

> Note: We'll be interacting all the time with the userId `1ca5b99a-ef88-4959-92e0-86cde3b8fc26` and our `access_key` for the recommendation engine will be `aFI4EfJJXc5W03ymMgqHWVAdV2VQN9ej5_WmMW_jWmMferm9n102SCQw0XYOXNsS`

# TODO

- [ ] Improve the data example importer script to use moltin's API data

# Resources

## Articles

- [5 Open Source Engines Templates for E-commerce Personalization Are Now Available for Download](http://blog.prediction.io/ecommerce-personalization)
- [PredictionIO: Machine Learning in E-Commerce. Complementary products based on the order history](https://hybrismart.com/2016/09/21/predictionio-machine-learning-in-e-commerce)

## Guides

- [Quick Start - E-Commerce Recommendation Engine Template](http://predictionio.incubator.apache.org/templates/ecommercerecommendation/quickstart)

## Tools

- [GitHub - Run PredictionIO inside Docker](https://github.com/mingfang/docker-predictionio)
- [GitHub - PredictionIO E-Commerce Recommendation Engine Template (Scala-based parallelized engine)](https://github.com/apache/incubator-predictionio-template-ecom-recommender)