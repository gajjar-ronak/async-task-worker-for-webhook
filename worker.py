from celery_config import celery

@celery.task
def process_webhook(data):
  # Implement your processing logic here
  print(f"Processing webhook data: {data}")

# other task definitions ...
@celery.task
def process_order(data):
    # Implement your processing logic here
    print(f"Processing order data: {data}")

@celery.task
def process_product(data):
    # Implement your processing logic here
    print(f"Processing product data: {data}")

@celery.task
def process_customer(data):
    # Implement your processing logic here
    print(f"Processing customer data: {data}")

@celery.task
def process_brand(data):
    # Implement your processing logic here
    print(f"Processing brand data: {data}")

@celery.task
def process_category(data):
    # Implement your processing logic here
    print(f"Processing category data: {data}")
