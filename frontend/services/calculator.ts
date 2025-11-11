type OpResult = { result:number};

export const calculatorApi = {
    add: (a: number, b:number) =>
        api<OpResult>(`/api/add?a=${a}&b=${b}`),
    subtract: (a:number, b:number) =>
        api<OpResult>(`/api/subtract?a=${a}&b=${b}`),
    multiply: (a:number, b:number) =>
        api<OpResult>(`/api/multiply?a=${a}&b=${b}`),
    divide: (a:number, b:number) =>
        api<OpResult>(`/api/divide?a=${a}&b=${b}`),
};

import {api} from "./apiClient";