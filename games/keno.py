from fastapi import APIRouter
import random
import pydantic
class Keno:

    class Bet(pydantic.BaseModel):
        numbers: list[int]
        username: str
        bet: int
    router = APIRouter()

    @router.get("/keno", tags=["keno"])
    async def keno():
        return {"msg": "Keno"}

    def numbers():
        numbers = [x for x in range(1, 41)]

        selected_numbers = random.sample(numbers, 10)

        return selected_numbers

    def payout(correct_numbers):
        if(len(correct_numbers) <=3):
            return 0
        elif(len(correct_numbers) == 4):
            return 3.5
        elif(len(correct_numbers) == 5):
            return 8
        elif(len(correct_numbers) == 6):
            return 13
        elif(len(correct_numbers) == 7):
            return 63
        elif(len(correct_numbers) == 8):
            return 500
        elif(len(correct_numbers) == 9):
            return 800
        elif(len(correct_numbers) == 10):
            return 1000

    @router.post("/bet")
    async def bet(bet: Bet):
        print(bet.model_dump_json())
        user = bet.username
        users[user]['credit'] -= bet.bet
        selected_numbers = numbers()


        correct_numbers = [x for x in bet.numbers if x in selected_numbers]

        users[user]['credit'] +=  payout(correct_numbers) * bet.bet
        return correct_numbers
