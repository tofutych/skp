<template>
    <div class="columns is-multiline">
        <div class="column is-12">
            <h1 class="title is-1 has-text-centered"> Group students list </h1>
        </div>

        <StudentBox v-for="student in students" v-bind:key="student.id" v-bind:student="student">
        </StudentBox>
    </div>
</template>


<script>
import axios from "axios";
import StudentBox from "@/components/StudentBox.vue";
export default {
    name: 'GroupView',
    components: {
        StudentBox
    },
    data() {
        return {
            students: []
        }
    },
    mounted() {
        this.getStudentsByGroupSlug()
    },
    methods: {
        async getStudentsByGroupSlug() {
            const slug = this.$route.params.slug
            await axios
                .get(`/api/groups/${slug}/students`)
                .then(response => {
                    this.students = response.data
                    console.log(this.students)
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>