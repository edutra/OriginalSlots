from fastapi import APIRouter
import random
from models.bet import Bet
import db

class Keno:
    router = APIRouter()

    @staticmethod
    def numbers():
        numbers = [x for x in range(1, 41)]

        selected_numbers = random.sample(numbers, 10)

        return selected_numbers

    @staticmethod
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

    @router.get("/keno/bet")
    async def bet(bet: Bet):
        print(bet)
        user = db.get_user(bet.username)
        if user.credit < bet.bet:
            return {"message": "Not enough credit"}

        db.update_user_credit(user.username, user.credit - bet.bet)
        selected_numbers = Keno.numbers()
        correct_numbers = [x for x in bet.numbers if x in selected_numbers]
        new_credit = user.credit + (Keno.payout(correct_numbers) * bet.bet)
        db.update_user_credit(user.username, new_credit)

        return correct_numbers
