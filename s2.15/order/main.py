import uvicorn
from threading import Thread
from app.job_finish_order import job_delivery_success, job_stock_fail

if __name__ == '__main__':
    t = Thread(target=job_delivery_success)
    t.start()
    t = Thread(target=job_stock_fail)
    t.start()
    uvicorn.run(app='app:app', host='0.0.0.0', port=8000, reload=True)
