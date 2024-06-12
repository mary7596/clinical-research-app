// src/components/StudyList.vue
<template>
   <div>
       <h1>Studies</h1>
       <table>
           <thead>
               <tr>
                   <th>Title</th>
                   <th>Therapeutics</th>
                   <th>Description</th>
                   <th>Status</th>
               </tr>
           </thead>
           <tbody>
               <tr v-for="study in studies" :key="study.id">
                   <td>{{ study.title }}</td>
                   <td>{{ study.therapeutics }}</td>
                   <td>{{ study.description }}</td>
                   <td>{{ study.status }}</td>
               </tr>
           </tbody>
       </table>
   </div>
</template>

<script>
import axios from 'axios';

export default {
   data() {
       return {
           studies: []
       };
   },
   created() {
       this.fetchStudies();
   },
   methods: {
       async fetchStudies() {
           try {
               const response = await axios.get('http://localhost:8000/api/studies/');
               this.studies = response.data;
           } catch (error) {
               console.error('Error fetching studies:', error);
           }
       }
   }
};
</script>