import { Router } from "express";
import { renderTasks, createTask, renderTaskEdit, editTask, deleteTask, taskToggleDone } from '../controllers/tasks.controller';

const router = Router();

router.get('/', renderTasks);

router.get('/edit/:id', renderTaskEdit);

router.post('/tasks/add', createTask);

router.post('/edit/:id', editTask);

router.get('/delete/:id', deleteTask);

router.get('/toggleDone/:id', taskToggleDone);
;
export default router;