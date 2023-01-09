import app from './app';
import './database.js';
import {PORT} from "./config"
app.listen(PORT);
console.log('Server on port', PORT)
