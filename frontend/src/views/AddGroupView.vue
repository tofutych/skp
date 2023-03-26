<template>
    <h1 class="title has-text-centered">Add new group</h1>
    <div class="columns">
        <div class="column is-4 is-offset-4">
            <form @submit.prevent="submitForm">
                <div class="field">
                    <label>Number</label>
                    <div class="control">
                        <input type="text" class="input" v-model="number">
                    </div>
                </div>

                <div class="field">
                    <div class="control has-text-centered">
                        <button class="button is-info">Submit</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>


<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
    name: 'AddGroupView',
    data() {
        return {
            number: '',
            slug: '',
        }
    },
    methods: {
        async submitForm() {
            this.slug = this.number
            this.slug = this.slug.toString().normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim().replace(/\s+/g, '-').replace(/[^\w-]+/g, '').replace(/--+/g, '-')
            const formData = {
                number: this.number,
                slug: this.slug,
            }

            await axios
                .post('/api/groups/', formData)
                .then(response => {
                    console.log(response.data)
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

        }
    }
}
</script>