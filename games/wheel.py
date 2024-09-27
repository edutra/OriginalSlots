from fastapi import APIRouter
import random
from models.bet import WheelBet
import db

class Wheel:

    router = APIRouter()

    @staticmethod
    def payout(sectors, bet):
        pass
    @staticmethod
    def spin(sectors):
        return random.randint(1, sectors)

    @router.get("/wheel/bet")
    async def bet(bet: WheelBet):
        user = db.get_user(bet.username)

        if user.credit < bet.bet:
            return {"error": "Not enough credit"}

        db.update_user_credit(user.username, user.credit - bet.bet)

        hit = Wheel.spin(bet.sectors) == 1

        if hit:
            new_credit = user.credit + (bet.sectors * bet.bet)
            db.update_user_credit(user.username, new_credit)
            return {"message": "You won!"}
        else:
            return {"message": "You lose!"}

