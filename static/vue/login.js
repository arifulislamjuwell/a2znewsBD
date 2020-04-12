Vue.component('input-field', {
    data: function () {
        return {
            username:'',
            password:'',
            content: this.value,
        }
    },
    template: `
    <div class="input-group form-group">
    <div class="input-group-prepend">
        <span class="input-group-text"><i :class="icon"></i></span>
    </div>
    <input @input="updateValue($event.target.value)" :type="inputType" class="form-control" :placeholder="placeHolderValue">
</div>
    `,
    props:['placeHolderValue','inputType', 'icon','value' ],
    methods: {
        updateValue: function (value) {
          this.$emit('input', value)
        }
      }
    
})



let login = new Vue({
    el: '#card',
    data: {
        clickedButton: 'login',
        username: null,
        password:'',
        ValidationMessage:''
    },
    methods: {
        checkButton: function(buttonType){
            this.clickedButton= buttonType
        },
        userValidation: function(username){
            console.log(username)
            if(!isNaN(username.charAt(0))){
                this.ValidationMessage= "this name start with number"
            }
      
        },
        login: function(){
            axios.post('/login/', {
                username: this.username,
                password: this.password
              })
              .then(function (response) {
                console.log(response);
              })
              .catch(function (error) {
              
              });
        }

    },
    mounted() {
        
    },
    watch: {
        username: function(value){
            this.userValidation(value);
        }
    },
})