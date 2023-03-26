<template>
    <h1 class="title has-text-centered">Add new student</h1>
    <div class="columns">
        <div class="column is-4 is-offset-4">
            <br>
            <form @submit.prevent="submitForm">
                <div class="field">
                    <label>Surname</label>
                    <div class="control">
                        <input type="text" class="input" v-model="surname">
                    </div>
                </div>

                <div class="field">
                    <label>Name</label>
                    <div class="control">
                        <input type="text" class="input" v-model="name">
                    </div>
                </div>

                <div class="field">
                    <label>Age</label>
                    <div class="control">
                        <input type="numger" class="input" v-model="age">
                    </div>
                </div>

                <div class="field">
                    <label>Group id</label>
                    <div class="control">
                        <input type="numger" class="input" v-model="group">
                    </div>
                </div>

                <div class="field">
                    <div class="control has-text-centered">
                        <button class="button is-info">Submit</button>
                    </div>
                </div>
                <hr>
            </form>
        </div>
    </div>
</template>


<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
    name: 'AddStudentView',
    data() {
        return {
            surname: '',
            name: '',
            age: '',
            group: '',
        }
    },
    methods: {
        async submitForm() {
            const formData = {
                group: this.group,
                surname: this.surname,
                name: this.name,
                age: this.age
            }

            await axios
                .post('/api/students/', formData)
                .then(response => {
                    toast({
                        message: 'Данные были успешно добавлены!',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
    }
}
</script>