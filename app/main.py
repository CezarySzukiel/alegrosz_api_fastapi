from fastapi import FastAPI
from app.routers import routers

app = FastAPI(
    title="Inventory Management System API",
    description="API for managing inventory, including products, suppliers, and orders.",
    version="1.0.0",
)

for router in routers:
    app.include_router(router)

@app.get("/health", tags=["Health Check"])
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "oline", "message": "Inventory Management System API is running!"}





if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)