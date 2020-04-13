Vue.component('input-field', {
    data: function () {
        return {
            username: '',
            password: '',
            content: this.value,
        }
    },
    template: `
    <div class="input-group form-group">
    <div class="input-group-prepend">
        <span class="input-group-text"><i :class="icon"></i></span>
    </div>
    <input @input="updateValue($event.target.value)" :type="inputType" class="form-control" :placeholder="placeHolderValue" :disabled="isDisable">
</div>
    `,
    props: ['placeHolderValue', 'inputType', 'icon', 'value', 'isDisable'],
    methods: {
        updateValue: function (value) {
            this.$emit('input', value)
        }
    }

})



let login = new Vue({
    delimiters: ['[[', ']]'],
    el: '#card',
    data: {
        buttonClass: {
            button: true,
            button1: true,
        },

        disabledOption:{
            username: false,
            mobileNumber: true,
            password: true,
            confirmPassword: true,
            email: true,
            age: true
        },
    
        clickedButton: 'login',
        ValidationMessage: null,
        checkErrorForDisable: true,
        user: null,
        pass: null,
        username:null,
        mobileNumber:null,
        password:null,
        confirmPassword:null,
        email:null,
        age:null
    },
    methods: {
        checkButton: function (buttonType) {
            this.clickedButton = buttonType
        },
        userValidation: function (username) {

            re = /^\w+$/;
            if (!re.test(username)) {
                this.ValidationMessage = "Username must contain only letters, numbers and underscores!"
                this.disabledOption.email= true;
                return false
            }

            if (username.length< 6){
                this.ValidationMessage = "Username must contain 6 digit"
                this.disabledOption.email= true;
                return false
            }
            if (username === " ") {
                this.ValidationMessage = "Username cannot be empty"
                this.disabledOption.email= true;
                return false
            }
            this.ValidationMessage= null
            return true


        },
        emailValidation: function(value){
            re=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
            if(!re.test(value)){
                this.ValidationMessage= 'You have entered an invalid email address!'
                return false
            }
            this.ValidationMessage= null
            return true
        },
        mobileNumberValidation: function(value){

            re=/\+?(88)?0?1[56789][0-9]{8}\b/
            if(!re.test(value)){
                this.ValidationMessage= 'You have entered an invalid number!'
                return false
            }
            this.ValidationMessage= null
            return true
        },
        passwordValidation: function (value) {
            var re = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}/;
            if(!re.test(value)){
                this.ValidationMessage= 'Invalid password,at least one number,lowercase,uppercase letter and 6 digit'
                return false
            }
            this.ValidationMessage= null
            return true

        },
        confirmPasswordValidation:function(value){
            if(this.password !== value){
                this.ValidationMessage= 'Password doesn\'t match'
                return false
            }
            this.ValidationMessage= null
            return true
        },
        ageValidation: function(value){
            var re = /^[1-9]?[0-9]{1}$|^100$/;
            if(!re.test(value)){
                this.ValidationMessage= 'Invalid age'
                return false
            }
            this.ValidationMessage= null
            return true

        },
        login: function () {
            var this_cur= this
            axios.post('/login/', {
                username: this.user,
                password: this.pass
            })
                .then(function (response) {
                    data= response.data.result;
                    this_cur.ValidationMessage= data

                })
                .catch(function (error) {

                });
        }

    },
    mounted() {

    },
    watch: {
        username: function (value) {
            usernameValidationResult = this.userValidation(value);
            if (usernameValidationResult){
                this.disabledOption.email= false
            }
        },
        email: function(value){
           emailValidationResult= this.emailValidation(value)
           if (emailValidationResult){
            this.disabledOption.mobileNumber= false
        }
        },
        mobileNumber: function(value){
            mobileNumberValidationResult= this.mobileNumberValidation(value)
            if (mobileNumberValidationResult){
                this.disabledOption.password= false
            }
        },
        password: function (value) {
            passwordValidationResult= this.passwordValidation(value)
            if (passwordValidationResult){
                this.disabledOption.confirmPassword= false
            }
        },
        confirmPassword: function(value){
            confirmPasswordValidationResult= this.confirmPasswordValidation(value)
            if (confirmPasswordValidationResult){
                this.disabledOption.age= false
            }
        },
        age: function(value){
            ageValidationResult= this.ageValidation(value)
            
            if (this.username && this.mobileNumber && this.password && this.confirmPassword && this.email && this.age && this.ValidationMessage === null){
                this.checkErrorForDisable= false
            }
        }

    },
})