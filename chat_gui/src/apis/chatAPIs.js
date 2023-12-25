import axios from "axios";

const PORT = 8080;
const URL = `http://192.168.240.131:${PORT}`;

export async function postChatMsg(msg) {
  try {
    const response = await axios.post(URL, {
      data: msg,
      timeout: 5000,
    });
    return response.data
  } catch (error) {
    if (error.code === "ECONNABORTED") {
      console.error("TIME OVER");
    } else {
      console.error("REQUEST FAILED:", error.message);
    }
  }
}
