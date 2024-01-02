import { createApp } from 'vue'
import App from './App.vue'

/**
 * 如何在vue3.0项目�?集成Element-plus
 * https://blog.csdn.net/weixin_47450807/article/details/123262703
 */
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)
app.use(ElementPlus)
app.mount('#app')
