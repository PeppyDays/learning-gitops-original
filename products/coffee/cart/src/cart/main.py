from fastapi import FastAPI

from cart.interface import router as cart_router

app = FastAPI()
app.include_router(router=cart_router, prefix="/cart")


@app.get("/")
def check_health() -> dict[str, str]:
    return {"hello": "world", "name": "cart"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app")
