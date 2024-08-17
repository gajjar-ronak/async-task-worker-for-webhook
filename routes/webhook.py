from fastapi import APIRouter, BackgroundTasks
from schemas import WebhookPayload
from worker import process_webhook, process_product, process_brand, process_category, process_customer

router = APIRouter(prefix="/webhook")

@router.post("/")
async def handle_webhook(payload: WebhookPayload, background_tasks: BackgroundTasks):
    scope = payload.scope
    data = payload.data

    # Dispatch the webhook data to the appropriate task based on the scope
    if scope == "store/product/created":
        background_tasks.add_task(process_product, data)
    elif scope == "store/brand/created":
        background_tasks.add_task(process_brand, data)
    elif scope == "store/category/created":
        background_tasks.add_task(process_category, data)
    elif scope == "store/customer/created":
        background_tasks.add_task(process_customer, data)
    else:
        background_tasks.add_task(process_webhook, data)  # Default task for other scopes

    return {"status": "Webhook received and processing started"}