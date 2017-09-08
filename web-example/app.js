function uuidv4() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}

new Vue({
    el: '#app',
    data: {
        userId: '1ca5b99a-ef88-4959-92e0-86cde3b8fc26',
        events: [],
        products: [],
        recommendations: []
    },
    created() {
        Moltin = moltin.gateway({
            client_id: 'umRG34nxZVGIuCSPfYf8biBSvtABgTR8GMUtflyE'
        });
        
        Moltin.Products.Limit(50).All()
            .then(response => this.products = response.data);
        
        axios.get(`http://localhost:7070/events.json?accessKey=aFI4EfJJXc5W03ymMgqHWVAdV2VQN9ej5_WmMW_jWmMferm9n102SCQw0XYOXNsS`)
            .then(response => this.events = response.data);
            
        axios.post(`http://localhost:8000/queries.json`, {
            user: this.userId, num: 5
        }).then(response => this.recommendations = response.data.itemScores);
    },
    methods: {
        view: function (productId, event) {
            axios.post(`http://localhost:7070/events.json?accessKey=aFI4EfJJXc5W03ymMgqHWVAdV2VQN9ej5_WmMW_jWmMferm9n102SCQw0XYOXNsS`, {
                "event" : "view",
                "entityType" : "user",
                "entityId" : this.userId,
                "targetEntityType" : "item",
                "targetEntityId" : productId
            })
            .then(function (response) {
                console.log(response.data);
            })
            .catch(function (error) {
                console.log(error);
            });
        },
        buy: function (productId, event) {
            axios.post(`http://localhost:7070/events.json?accessKey=aFI4EfJJXc5W03ymMgqHWVAdV2VQN9ej5_WmMW_jWmMferm9n102SCQw0XYOXNsS`, {
                "event" : "buy",
                "entityType" : "user",
                "entityId" : this.userId,
                "targetEntityType" : "item",
                "targetEntityId" : productId
            })
            .then(function (response) {
                console.log(response.data);
            })
            .catch(function (error) {
                console.log(error);
            });
        }
    }
})