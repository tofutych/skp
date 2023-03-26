<template>
    <div class="column is-3">
        <div class="box has-text-centered">
            <h3 class="is-size-4">{{ group.number }}</h3>
            <router-link v-bind:to="group.get_absolute_url" class="button is-info mt-4">More</router-link>
            <button class="button mt-4 is-danger" @click="deleteGroup()">Delete</button>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
    name: 'GroupBox',
    props: {
        group: Object
    },
    methods: {
        async deleteGroup() {
            const id = this.group.id
            await axios
                .delete(`/api/groups/${id}/`)
                .then(response => {
                    console.log(response.data)
                    this.$router.go("/")
                    toast({
                        message: 'Группа стерта с лица земли!',
                        type: 'is-danger',
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

<style scoped>
.image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
}

.box {
    padding: .1rem;
}
</style>