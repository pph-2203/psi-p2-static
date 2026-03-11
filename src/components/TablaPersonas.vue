<!-- src/components/TablaPersonas.vue -->

<template>
  <!-- Contenedor principal del componente -->
  <div id="tabla-personas">
    <div v-if="!personas.length" class="alert alert-info" role="alert">
      No se han encontrado personas
    </div>
    <!-- Tabla para mostrar informacion de personas -->
    <table class="table">
      <!-- Encabezado de la tabla -->
      <thead>
        <tr>
          <!-- Columnas del encabezado -->
          <th>Nombre</th>
          <th>Apellido</th>
          <th>Email</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <!-- Cuerpo de la tabla -->
      <tbody>
        <!-- Iteracion sobre el array de personas utilizando v-for -->
        <tr v-for="persona in personas" :key="persona.id">
          <!-- Celda de datos para el nombre de la persona -->
          <td v-if="editando === persona.id">
            <input
id="persona.nombre" v-model="persona.nombre" type="text"
            class="form-control" data-cy="persona-nombre">
          </td>
          <td v-else>
            {{ persona.nombre }}
          </td>
          <!-- Celda de datos para el apellido de la persona -->
          <td v-if="editando === persona.id">
            <input
v-model="persona.apellido" type="text"
            class="form-control">
          </td>
          <td v-else>
            {{ persona.apellido }}
          </td>
          <!-- Celda de datos para el correo electronico de la persona -->
          <td v-if="editando === persona.id">
            <input
v-model="persona.email" type="email"
            class="form-control">
          </td>
          <td v-else>
            {{ persona.email }}
          </td>
          <td>
            <td v-if="editando === persona.id">
              <button 
              class="btn btn-success"
              data-cy="save-button" 
              @click="guardarPersona(persona)">&#x1F5AB; Guardar
              </button>
              <button
              class="btn btn-secondary ml-2" 
              data-cy="cancel-button" 
              @click="cancelarEdicion(persona)">&#x1F5D9; Cancelar
              </button>
            </td>
            <td v-else>
              <button
              class="btn btn-info"
              data-cy="edit-button"
              @click="editarPersona(persona)">&#x1F58A; Editar
              </button>
              <button
              class="btn btn-danger ml-2"
              data-cy="delete-button"
              @click="$emit('delete-persona', persona.id)">&#x1F5D1; Eliminar
              </button>
            </td>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref } from 'vue';
// Definicion del componente Vue
defineOptions({
  // Nombre del componente
  name: 'TablaPersonas',
});

const props = defineProps({
  personas: {type: Array, default: () => []},
});

const emit = defineEmits(['actualizar-persona', 'delete-persona']);

const editando = ref(null);
const personaEditada = ref(null);

const editarPersona = (persona) => {
  personaEditada.value = {...persona};
  editando.value = persona.id;
};

const guardarPersona = (persona) => {
  if (!persona.nombre.length || !persona.apellido.length || !persona.email.length) {
    return;
  }

  emit('actualizar-persona', persona.id, persona);
  editando.value = null;
};

const cancelarEdicion = (persona) => {
  Object.assign(persona, personaEditada.value);
  editando.value = null;
}
</script>

<style scoped>
  /* Estilos especificos del componente con el modificador "scoped" */
</style>
