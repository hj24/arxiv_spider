#!bin/bash
nohup sea server &
nohup sea async_task beat &
nohup sea async_task worker &