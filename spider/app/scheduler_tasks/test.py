from spider.app.scheduler_tasks import task_manager

if __name__ == '__main__':
    m = task_manager.Manager()
    jobs = m.show_jobs()
    print(jobs)