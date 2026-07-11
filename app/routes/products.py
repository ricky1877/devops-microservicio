from fastapi import APIRouter, HTTPException
from app.schemas import Product
from app.services.product_service import (
    get_products,
    get_product,
    create_product,
    update_product,
    delete_product,
)

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
def list_products():
    return get_products()


@router.get("/{product_id}")
def find_product(product_id: int):
    product = get_product(product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return product


@router.post("/", status_code=201)
def add_product(product: Product):
    if get_product(product.id):
        raise HTTPException(
            status_code=400,
            detail="Ya existe un producto con ese ID"
        )

    return create_product(product)


@router.put("/{product_id}")
def edit_product(product_id: int, product: Product):
    updated = update_product(product_id, product)

    if updated is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return updated


@router.delete("/{product_id}")
def remove_product(product_id: int):
    deleted = delete_product(product_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return {"message": "Producto eliminado correctamente"}