"use client"
import * as React from "react"
import { useState, useEffect } from "react"
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

interface Product {
  id: number;
  name: string;
  price: number;
  image: string;
}

function ProductList(): JSX.Element {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch('http://localhost:8000/product-list');
        const data = await response.json();
        console.log(data)
        setProducts(data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching medical products:', error);
      }
    };
    fetchProducts();
  }, []);

  return (
    <Card className="w-[350px]">
      <CardHeader>
        <CardTitle>Product List</CardTitle>
      </CardHeader>
      <CardContent>
        {loading ? (
          <p>Loading...</p>
        ) : (
          <ul>
            {products.map((product: Product) => (
              <li key={product.id}>
                <p>{product.name}</p>
                <p>Price: ${product.price}</p>
                <img src={product.image} alt={product.name} />
              </li>
            ))}
          </ul>
        )}
      </CardContent>
      <CardFooter className="flex justify-end">
        <Button variant="outline">Cancel</Button>
        <Button>Pay</Button>
      </CardFooter>
    </Card>
  )
}
export default ProductList
