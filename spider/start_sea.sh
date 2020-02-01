#!bin/bash
nohup sea server > sea.log 2>&1 &
nohup sea async_task beat > beat.log 2>&1 &
nohup sea async_task worker > worker.log 2>&1 &

