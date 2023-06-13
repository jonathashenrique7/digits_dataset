from typing import List

class Fibonacci: 

    def counter(self) -> None: 

        arr: List[int] = [
            0, 1
        ]

        x: int = 20 

        for y in range(x-2):
            arr.append( arr[-1] + arr[-2] )
            print(arr)
        pass

if __name__ == "__main__":
    result = Fibonacci()
    result.counter()


