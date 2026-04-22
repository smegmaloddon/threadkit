import threadkit.Thread as Thread

def Print(
    number : int
) -> None:
    
    print(number)

Thread.Thread(
    func=Print,
    items=[
        {"number": 1},
        {"number": 2},
        {"number": 3}
    ]
)