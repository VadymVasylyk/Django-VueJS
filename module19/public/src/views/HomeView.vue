<script>
import axios from 'axios';

export default {
  data() {
    return {
      items: [],
      selectedItem: null,
    };
  },
  async mounted() {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/items/?format=json');
      this.items = res.data;
    } catch (error) {
      console.log(error);
    }
  },
  methods: {
    showForm(item) {
      if (this.selectedItem !== item){
        this.selectedItem = item;
      } else{
        this.selectedItem = null;
      }     
    },
    async sendData(item) {
    try {
      const data = {
        'slug': item.slug,
        'title': item.title,
        'image': item.image,
        'desc': item.desc,
        'price': item.price
      };

      await axios.put(`http://127.0.0.1:8000/api/edit-items/`, data);
    } catch (error) {
      console.error(error);
    }
  }
  },
};
</script>

<template>
  <main>
    <div class="items">
        <div class="item" v-for="el in items" :key="el.slug">
            <img :src="'/img/' + el.image" :alt="el.title">
            <h3>{{ el.title }}</h3>
            <p>{{ el.desc }}</p>
            <div class="bottom">
                <span>{{ el.price }}$</span>
            </div>
            <button class="btn-edit" @click="showForm(el)">Edit</button>
            <form v-if="selectedItem===el">
              <input type="text" v-model="el.image" placeholder="Image">
              <input type="text" v-model="el.title" placeholder="Title">
              <input type="textarea" v-model="el.desc" placeholder="Description">
              <input type="number" v-model="el.price" placeholder="Price">
              <button type="submit" class="btn-edit" @click="sendData(el)">Confirm</button>
            </form>
        </div>
    </div>
  </main>
</template>

<style scoped>
.items {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    flex-wrap: wrap;
}

.items .item {
    margin-bottom: 100px;
    width: 350px;
    padding: 15px;
    background: #F4F4F4;
}

.items .item img:first-child {width: 100%;}

.items .item h3 {
    margin: 12px 0;
    font-size: 20px;
}

.items .item p {
    margin: 10px 0;
    font-size: 15px;
    width: 90%;
}

.items .item .bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}

.items .item .bottom span {
    font-weight: 600;
    color: #216E5B;
}

.items .item .btn-edit {
  width: 100%;
  height: 40px;
  background-color: #2b9a7e;
  color: white;
  border: none;
  border-radius: 5px;
}

form {
    margin-top: 10px;
}

form input {
    width: 300px;
    padding: 10px 15px;
    border: 1.5px solid #575d61;
    border-radius: 2px;
    margin-bottom: 10px;
    display: block;
    outline: none;
    font-size: 15px;
}

form input::placeholder {
    color: rgba(64, 64, 64, 0.531);
}

form input:focus {
    border-color: #242424;
}
</style>