let homepage = new Vue({
    delimiters: ['[[', ']]'],
    el: '#navbar',
    data: {
        newspaperList: [{
                name: 'Daily Prothom Alo',
                content: ''
            },
            {
                name: 'Bangladesh Pratidin',
                content: ''
            },
            {
                name: 'Samakal',
                content: ''
            },
            {
                name: 'Daily Naya Diganta',
                content: ''
            },

            {
                name: 'Daily kaler kantho',
                content: ''
            },

            {
                name: 'Daily Inqilablo',
                content: ''
            }
        ],
        news: null
    },
    mounted() {
        var this_cur = this
        axios.get('/prothom-alo/')
            .then(function(response) {
                data = response.data.news;
                this_cur.newspaperList[0].content = data
            })
            .catch(function(error) {

            });
        axios.get('/bd-protidin/')
            .then(function(response) {
                data = response.data.news;
                this_cur.newspaperList[1].content = data
            })
            .catch(function(error) {

            });

        axios.get('/samakal/')
            .then(function(response) {
                data = response.data.news;
                this_cur.newspaperList[2].content = data
            })
            .catch(function(error) {

            });
        axios.get('/dailynayadiganta/')
            .then(function(response) {
                data = response.data.news;
                this_cur.newspaperList[3].content = data
            })
            .catch(function(error) {

            });
    }
})