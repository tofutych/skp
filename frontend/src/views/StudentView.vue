<template>
    <div class="columns">
        <div class="column is-4 is-offset-4">
            <div class="card">
                <div class="card-content">
                    <div class="media">
                        <div class="media-left">
                            <figure>
                                <i class="fa-sharp fa-solid fa-graduation-cap"></i>
                            </figure>
                        </div>
                        <div class="media-content">
                            <p class="title is-4">{{ student.surname }} {{ student.name }}, {{ student.age }} y.o.</p>
                            <p class="subtitle is-6">group id: {{ student.group }}</p>
                        </div>
                    </div>
                </div>
            </div>
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
            <div class="control has-text-centered">
                <h1>ИЛИ УДАЛИТЬ ЭТОГО ЧЕЛОВЕЧКА</h1>
                <br>
                <button @click="deleteStudent()" class="button is-danger">DELETE</button>
            </div>
        </div>
    </div>
</template>


<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
    name: 'StudentView',
    data() {
        return {
            student: {},
            surname: '',
            name: '',
            age: '',
            group: '',
        }
    },
    mounted() {
        this.getStudent()
    },
    methods: {
        async getStudent() {
            const id = this.$route.params.id
            await axios
                .get(`/api/students/${id}`)
                .then(response => {
                    this.student = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async submitForm() {
            const formData = {
                group: this.group,
                surname: this.surname,
                name: this.name,
                age: this.age
            }
            const id = this.$route.params.id

            await axios
                .put(`/api/students/${id}/`, formData)
                .then(response => {
                    this.student.surname = response.data.surname
                    this.student.name = response.data.name
                    this.student.age = response.data.age
                    this.student.group = response.data.group

                    toast({
                        message: 'Данные были успешно обновлены!',
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
        async deleteStudent() {
            const id = this.$route.params.id
            await axios
                .delete(`/api/students/${id}/`)
                .then(response => {
                    console.log(response)

                    toast({
                        message: 'Чел стерт с лица земли!',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })
                this.$router.go(-1)
        }
    }
}
</script>