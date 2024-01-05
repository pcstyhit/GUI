<template>
  <div class="container">
    <!-- Left Card -->
    <el-card class="left-card">
      <!-- Content for the left card goes here -->

      <!-- New Chat Button -->
      <el-button class="new-chat-button" type="text" @click="newChat">
        New Chat
      </el-button>
    </el-card>

    <!-- Right Card -->
    <el-card class="right-card">
      <!-- Message Input -->
      <el-row class="right-card-input">
        <el-input
          style="width: 95%; height: 10%"
          v-model="inputText"
          placeholder="Please input your question ..."
        ></el-input>
        <el-button style="width: 5%; height: 10%" type="primary" @click="sendContent">Send</el-button>
      </el-row>
    </el-card>
  </div>
</template>

<script>
import {postChatMsg} from '../../apis/chatAPIs.js'
export default {
  name: "HomePage",
  data() {
    return {
      inputText: "",
    };
  },
  methods: {
    newChat() {
      // Handle the "New Chat" button click event
      console.log("New Chat button clicked");
    },

    async sendContent() {
      var msg = this.inputText;
      this.inputText = "";
      var res = await postChatMsg(msg);
      console.log(res,'xxx')
      
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  height: 98vh; /* Full height of the viewport */
  margin-top: 5px;
  margin-left: 0;
}

.left-card {
  flex: 0 0 15%; /* 15% width */
  width: 15%;
  height: 100%;
  background-color: black;
}

.new-chat-button {
  position: absolute;
  top: 10px; /* Adjust the top position as needed */
  left: 10px; /* Adjust the left position as needed */
  background-color: transparent;
  color: white;
  font-size: 2.5vh;
  border: 0.2px solid gray;
  width: 14%;
}

.right-card {
  width: 85%;
  height: 100%;
  background-color: white;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}

.right-card .right-card-input {
  width: 100%;
  padding: 10px;
}
</style>
