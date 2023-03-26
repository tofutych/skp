<template>
    <div class="column is-3">
        <div class="box has-text-centered">
            <h3 class="is-size-4">{{ student.surname }} {{ student.name }}, {{ student.age }}yo</h3>
            <router-link v-bind:to="student.get_absolute_url" class="button is-info is-light mt-4">More</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'StudentBox',
    props: {
        student: Object
    }
}
</script>

<style scoped>
.box {
    padding: .1rem;
    background-color: rgba(152, 201, 235, 0.1)
}
</style>