"use client";

import { useState } from "react";
import { calculatorApi }  from "@/services/calculator";

const ops = [
    { key:"add", label:"Add" },
    { key:"subtract", label:"Subtract" },
    { key:"multiply", label:"Multiply" },
    { key:"divide", label:"Divide" }
] as const;

type OpKey = typeof ops[number]["key"];

export default function CalculatorForm() {
    const [a, setA] = useState<string>("");
    const [b, setB] = useState<string>("");
    const [op, setOp] = useState<OpKey>("add");
    const [result, setResult]  =useState<number | null>(null);
    const [error, setError] = useState<string | null>(null);
    const n = (v:string) => Number(v);

    async function onCalc() {
        setError(null);
        setResult(null);

        if (a.trim() === "" || b.trim() === ""){
            setError("Please enter both numbers.");
            return;
        }

        try{
            const A = n(a);
            const B = n(b);

            const api = {
                add: () => calculatorApi.add(A, B),
                subtract: () => calculatorApi.subtract(A, B),
                multiply: () => calculatorApi.multiply(A, B),
                divide: () => calculatorApi.divide(A, B),
            } [op];

            const data = await api();
            setResult(data.result);
        } catch (e:any) {
            setError(e.message || "An error occurred during calculation.");
        }
    }
    
    
}

